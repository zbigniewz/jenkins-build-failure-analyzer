# jenkins-build-failure-analyzer
Analyze jenkins failures and report them to graphite server

## usage
```
➜  jenkins-build-failure-analyzer python analyzer.py -h
usage: analyzer.py [-h]
                   jenkins_host jenkins_user jenkins_pass statsd_host
                   statsd_port graphite_key

Analyze jenkins failures and report them to graphite server

positional arguments:
  jenkins_host
  jenkins_user
  jenkins_pass
  statsd_host
  statsd_port
  graphite_key

optional arguments:
  -h, --help    show this help message and exit
```
