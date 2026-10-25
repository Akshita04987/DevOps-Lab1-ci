pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }
        stage('Build') {
            steps {
                sh 'mkdir -p dist && cp app.py requirements.txt dist/'
                sh 'tar -czf app.tar.gz -C dist .'
                archiveArtifacts artifacts: 'app.tar.gz', fingerprint: true
            }
        }
        stage('Deploy') {
            steps {
                sh 'mkdir -p /var/lib/jenkins/deployed-app'
                sh 'cp -r dist/* /var/lib/jenkins/deployed-app/'
                echo 'Deployed to /var/lib/jenkins/deployed-app'
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
