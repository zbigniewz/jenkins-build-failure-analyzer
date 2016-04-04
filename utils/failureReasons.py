possible_reasons = [
    {
        'name': 'failed tests',
        'description': 'project\'s tests are failing or causing errors',
        'regex': [
            '\[ERROR\] Failed to execute goal org\.apache\.maven\.plugins:maven-surefire-plugin',
            '\[ERROR\] ACC test failed\. exit\(1\)',
            'Failures:',
            '-----------------------------------FAILURE LIST-----------------------------------'
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
            'Fatal error. ERROR. deployment was not successful'
        ],
        'graphite key': 'failed_deployment'
    },
    {
        'name': 'Docker container not started',
        'description': 'Docker container has not started, maybe docker deamon problem?',
        'regex': [
            'Error response from daemon. Cannot start container'
        ],
        'graphite key': 'docker_cntnr_not_started'
    }
]

# used when non of above is matching
unknown_reason = {
    'name': 'unknown reason',
    'description': 'console output doesn\'t match any of knonw reasons',
    'regex': [''],
    'graphite key': 'unknown'
}


