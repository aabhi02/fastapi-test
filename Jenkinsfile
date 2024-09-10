pipeline {
    agent any
    environment {
        CONDA_ENV = "aint"
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code
                git 'https://github.com/aabhi02/jenkins-test.git'
            }
        }
        stage('Setup Conda Environment') {
            steps {
                script {
                    // Set up Conda and activate the environment
                    sh '''
                    source ~/miniconda3/etc/profile.d/conda.sh
                    conda activate $CONDA_ENV
                    '''
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh '''
                    source ~/miniconda3/etc/profile.d/conda.sh
                    conda activate $CONDA_ENV
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run your tests
                    sh '''
                    source ~/miniconda3/etc/profile.d/conda.sh
                    conda activate $CONDA_ENV
                    pytest
                    '''
                }
            }
        }
    }
    post {
        always {
            // Clean up
            sh '''
            source ~/miniconda3/etc/profile.d/conda.sh
            conda deactivate
            '''
        }
    }
}
