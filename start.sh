#!/bin/sh

# use when you want to monitor jenkins constantly

docker build -t jenkins-build-failure-analyzer .

while true
do
        docker run -t jenkins-build-failure-analyzer https://MY.JENKINS.URL JENKINS_USER JENKINS_PASSWORD STATSD.HOST STATSD.PORT METRIC.KEY
        sleep 1800
done
