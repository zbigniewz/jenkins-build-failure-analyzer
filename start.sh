#!/bin/sh

# use when you want to monitor jenkins constantly

while true
do
        python analyzer.py URL_TO_JENKINS JENKINS_USER JENKINS_PASS STATSD_HOST STATSD_PORT GRAPHITE_KEY
        sleep 1800
done
