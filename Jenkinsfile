pipeline {
    agent any
    stages {
        stage('Setup virtual environment') {
            steps {
                echo 'Creating a virtual environment, if not created'
                    sh '''
                        if [ ! -d ".venv" ]; then
                            env_name=${1:-".venv"}
                            python3 -m venv "$env_name"
                            echo "Virtual environment '$env_name' has been created."
                        fi
                    '''
                    echo 'Activating the virtual environment'
                    sh '''
                        env_name=${1:-".venv"}
                        chmod +x ./$env_name/bin/activate
                        ./$env_name/bin/activate
                    '''
                    echo 'Dependency installation'
                    sh '''
                        env_name=${1:-".venv"}
                        $env_name/bin/pip3 install -r requirements.txt
                        echo "Dependencies installed."
                    '''
            }
        }
        stage('Data preprocessing') {
            steps {
                dir('/app/ml') {
                    sh '''
                    source env/bin/activate
                    python3 data_preprocessing.py
                    '''
                }
            }
        }
        stage('Model training') {
            steps {
                dir('/app/ml') {
                    sh '''
                    python3 model_preparation.py
                    '''
                }
            }
        }
        stage('Model testing') {
            steps {
                dir('/app/ml') {
                    sh '''
                    source env/bin/activate
                    python3 model_testing.py
                    '''
                }
            }
        }
    }
    post {
        always {
            echo 'The pipeline is finished!'
        }
        success {
            echo 'The build was successful!'
        }
        failure {
            echo 'The build failed.'
        }
    }
}