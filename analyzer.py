#!/usr/bin/python

import pprint
import re
import argparse
from datetime import datetime
from statsd import StatsClient
from utils import failureReasons, JenkinsClient


def is_build_failed(job):
    if 'lastBuild' in job and job['lastBuild'] is not None and 'result' in job['lastBuild']:
            if job['lastBuild']['result'] == 'FAILURE':
                return True
    return False


def was_built_in_last_24h(job):
    if 'lastBuild' in job:
        build_date_time = datetime.utcfromtimestamp(job['lastBuild']['timestamp'] / 1e3) # to proper timestamp
        time_diff_in_hours = (datetime.now() - build_date_time).total_seconds() / 60 / 60 # seconds to hours
        if time_diff_in_hours < 24:
            return True
    return False


def filter_jobs(all_jobs):
    failed_jobs = []
    for job in all_jobs:
        if is_build_failed(job) and was_built_in_last_24h(job):
                    failed_jobs.append(job)
    return failed_jobs


def find_failure_reason(console_output):
    for reason in failureReasons.possible_reasons:
        for regex in reason['regex']:
            match = re.search(regex, console_output)
            if match:
                return reason['name']
    return failureReasons.unknown_reason['name']


def update_results(results, reason, job):
    for entry in results:
        if entry['name'] == reason:
            entry['count'] += 1
            entry['job'].append(
                {
                    'job name': job['name'],
                    'build url': '{job_url}{build_number}/console'.format(job_url=job['url'],
                                                                          build_number=job['lastBuild']['number'])
                }
            )
            break
    return results


def analyze_jobs(filtered_jobs, jenkins_server):
    results = failureReasons.possible_reasons
    results.append(failureReasons.unknown_reason)
    for entry in results:
        entry['count'] = 0
        entry['job'] = []
    counter = 0
    for job in filtered_jobs:
        counter += 1
        print("Analyzing job {id} / {all}".format(id=counter, all=len(filtered_jobs)))
        console_output = jenkins_server.get_job_console_output(job)
        failure_reason = find_failure_reason(console_output)
        results = update_results(results, failure_reason, job)
    return results


def print_results(results):
    print('\n Full results:\n')
    pp = pprint.PrettyPrinter()
    pp.pprint(results)
    print('\n\n\n Quick summary:\n')
    for entry in results:
        print('{reason} : {count}'.format(reason=entry['name'], count=entry['count']))


def report_to_graphite(host, port, prefix, results):
    statsd = StatsClient(host=host, port=port, prefix=prefix, maxudpsize=512)
    for entry in results:
        statsd.gauge(entry['graphite key'], entry['count'])


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Analyze jenkins failures and report them to graphite server')
    parser.add_argument('jenkins_host')
    parser.add_argument('jenkins_user')
    parser.add_argument('jenkins_pass')
    parser.add_argument('statsd_host')
    parser.add_argument('statsd_port')
    parser.add_argument('graphite_key')
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()
    jenkins_server = JenkinsClient.JenkinsClient(args.jenkins_host, args.jenkins_user, args.jenkins_pass)
    all_jobs = jenkins_server.get_all_jobs()
    filtered_jobs = filter_jobs(all_jobs)
    results = analyze_jobs(filtered_jobs, jenkins_server)
    report_to_graphite(args.statsd_host, args.statsd_port, args.graphite_key, results)
    print_results(results)


if __name__ == '__main__':
    main()
