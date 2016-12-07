import requests
import urllib3

class JenkinsClient:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def _do_request(self, url):
        urllib3.disable_warnings()
        return requests.get(url, auth=(self.username, self.password), verify=False)

    def get_all_jobs(self):
        jenkins_jobs_url = self.url + '/api/json?tree=jobs[name,url,lastBuild[number,result,timestamp]]'
        response = self._do_request(jenkins_jobs_url)
        return response.json()['jobs']

    def get_job_console_output(self, job):
        console_output_url = '{job_url}{build_number}/consoleText'.format(job_url=job['url'], build_number=job['lastBuild']['number'])
        response = self._do_request(console_output_url)
        return response.text
