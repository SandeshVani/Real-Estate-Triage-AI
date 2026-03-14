pipeline {
    agent any
    stages {
        stage('1. Get Code from GitHub') {
            steps {
                git 'https://github.com/SandeshVani/Real-Estate-Triage-AI.git'
            }
        }
        stage('2. Build Docker Image') {
            steps {
                sh 'docker build -t real-estate-image:latest .'
            }
        }
        stage('3. Deploy App via Ansible') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml'
            }
        }
    }
}
