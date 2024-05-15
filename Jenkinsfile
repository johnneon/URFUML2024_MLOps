pipeline {
    agent any
    stages {
        stage('Download the repository from git') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/johnneon/URFUML2024_MLOps.git']])
            }
        }
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
                    sh '''
                        env_name=${1:-".venv"}
                        $env_name/bin/pip3 install -e .
                        echo "Local packages are installed."
                    '''
            }
        }
        stage('Data preprocessing') {
            steps {
                    sh '''
                    .venv/bin/python3 app/ml/data_preprocessing.py
                    '''
            }
        }
        stage('Model training') {
            steps {
                    sh '''
                    .venv/bin/python3 app/ml/model_preparation.py
                    '''
            }
        }
        stage('Model testing') {
            steps {
                    sh '''
                    .venv/bin/python3 app/ml/model_testing.py
                    '''
            }
        }
        stage('Build dockers') {
            steps {
                script {
                    sh 'docker build -t urfuml2024_mlops:$BUILD_NUMBER .'     
	                echo 'Build Image Completed '
                }
            }
        }
        stage('Run dockers') {
            steps {
                script {
                    sh 'docker run --rm -i -p 8000:8000 urfuml2024_mlops:$BUILD_NUMBER'
	                echo 'Run Image Completed'
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