pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('deps') {
            steps {
                sh '''
                    python -m pip install --upgrade pipenv wheel
                    cd app_python
                    pipenv install --deploy --dev
                '''
                parallel 'linting':{
                    sh 'pipenv run lint'
                }, 'testing':{
                    sh 'pipenv run test'
                }
            }
        }
    }
}
