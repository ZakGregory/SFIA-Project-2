pipeline {
    agent any
    stages {
        stage('Ansible') {
            steps {
                sh "./scripts/test.sh"
            }
        }
	stage('Test') {
            steps {
                sh "./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "./scripts/build.sh"
            }
        }
        stage('Push') {
            steps {
                sh "./scripts/push.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "./scripts/deploy.sh"
            }
        }
    }
}
