pipeline {
    agent any
    stages {

       
        stage('Build') {
            steps {
                echo "...Build Done..."
                sh "python3"    
            }
        }

        stage('Test') {
            agent {
                docker { image 'devops_image' }
            }
            steps {
                echo "Executing the file..!"
                sh('python3 tests.py')
        }
    }
}
}