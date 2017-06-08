# jenkins-build-failure-analyzer
Analyze jenkins failures and report them to graphite server

## building docker image
```
docker build -t jenkins-build-failure-analyzer .
```

## usage
```
docker run -t jenkins-build-failure-analyzer https://MY.JENKINS.URL JENKINS_USER JENKINS_PASSWORD STATSD.HOST STATSD.PORT METRIC.KEY
```
