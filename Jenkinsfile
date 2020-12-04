pipeline {
    agent any
    stages {
        stage('Ansible') {
            steps {
                ansiblePlaybook credentialsId:'private-key', installation:'ansible', inventory:'inventory', playbook:'playbook.yml', disableHostKeyChecking: true
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
