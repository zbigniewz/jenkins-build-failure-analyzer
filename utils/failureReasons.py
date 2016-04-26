possible_reasons = [
    {
        'name': 'failed tests',
        'description': 'project\'s tests are failing or causing errors',
        'regex': [
            '\[ERROR\] Failed to execute goal org\.apache\.maven\.plugins:maven-surefire-plugin',
            '\[ERROR\] ACC test failed\. exit\(1\)',
            'Failures:',
            '-----------------------------------FAILURE LIST-----------------------------------',
            'npm ERR. Test failed.  See above for more details',
            'FAILURES!',
            '>>>>>> Class: Kitchen::ActionFailed'
        ],
        'graphite key': 'failed_tests'
    },
    {
        'name': 'missing dependencies',
        'description': 'project can\'t build because there are missing dependencies in nexus',
        'regex': [
            'Could not resolve dependencies for project'
        ],
        'graphite key': 'missing_dependencies'
    },
    {
        'name': 'sonar violations',
        'description': 'project can\'t build because it is breaking sonar rules',
        'regex': [
            '\[ERROR\] Failed to execute goal org\.sonarsource\.scanner\.maven:sonar-maven-plugin'
        ],
        'graphite key': 'sonar_violation'
    },
    {
        'name': 'failed to clone',
        'description': 'project can\'t be cloned/checked out from source repository',
        'regex': [
            'ERROR: Failed to clone',
            'ERROR: Repository not found'
        ],
        'graphite key': 'failed_clone'
    },
    {
        'name': 'failed compilation',
        'description': 'project doesn\'t compile',
        'regex': [
            '\[ERROR\] Failed to execute goal org\.apache\.maven\.plugins:maven-compiler-plugin'
        ],
        'graphite key': 'failed_compilation'
    },
    {
        'name': 'missing jacoco plugin',
        'description': 'project pom does not have jacoco plugin for code static analysis',
        'regex': [
            "\[ERROR\] No plugin found for prefix 'jacoco'"
        ],
        'graphite key': 'missing_jacoco'
    },
    {
        'name': 'npm fetch failed',
        'description': 'npm failed while fetching libs, probably problem with npm proxy or npm itself',
        'regex': [
            'npm ERR. fetch failed'
        ],
        'graphite key': 'npm_fetch'
    },
    {
        'name': 'illegal live deployment',
        'description': 'Trying to deploy app to live outside of deployment window',
        'regex': [
            'Live-Deployments are only allowed Monday - Thursday'
        ],
        'graphite key': 'illegal_live_deployment'
    },
    {
        'name': 'failed deployment',
        'description': 'Failed deployment - app not started?',
        'regex': [
            'ERROR. App has been successfully deployed but it could not be started.',
            'Fatal error. ERROR. (d|D)eployment was not successful'
        ],
        'graphite key': 'failed_deployment'
    },
    {
        'name': 'Docker container not started',
        'description': 'Docker container has not started, maybe docker daemon problem?',
        'regex': [
            'Error response from daemon. Cannot start container',
            'Cannot start container',
            'Error response from daemon. conflict. unable to delete'
        ],
        'graphite key': 'docker_cntnr_not_started'
    },
    {
        'name': 'Fastlane error',
        'description': 'Fastlane script encounter some issues.',
        'regex': [
            'OSError: \[Errno 2\] No such file or directory'
        ],
        'graphite key': 'fastlane_error'
    },
    {
        'name': 'AWS live docker error',
        'description': 'Failed to push to AWS live docker registry.',
        'regex': [
            'write tcp \d{1,3}\.152.\d{1,3}\.\d{1,3}:5000: connection reset by peer'
        ],
        'graphite key': 'aws_docker_live_error'
    },
    {
        'name': 'AWS live docker error',
        'description': 'Failed to push to AWS quality docker registry.',
        'regex': [
            'write tcp \d{1,3}\.130.\d{1,3}\.\d{1,3}:5000: connection reset by peer'
        ],
        'graphite key': 'aws_docker_quality_error'
    },
    {
        'name': 'pulp timeout',
        'description': 'Failed to download dependecies from pulp beacuse of pulp timeout',
        'regex': [
            '.*Timeout on http...pulp.*'
        ],
        'graphite key': 'pulp_timeout'
    }
]

# used when non of above is matching
unknown_reason = {
    'name': 'unknown reason',
    'description': 'console output doesn\'t match any of knonw reasons',
    'regex': [''],
    'graphite key': 'unknown'
}


