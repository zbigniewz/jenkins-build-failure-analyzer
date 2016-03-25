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
    }
]

# used when non of above is matching
unknown_reason = {
    'name': 'unknown reason',
    'description': 'console output doesn\'t match any of knonw reasons',
    'regex': [''],
    'graphite key': 'unknown'
}


