pipeline {
	agent {
		docker { image 'python:3.9.6' }
	}
	stages {
		stage('build') {
			steps {
				sh 'python --version'
			}
		}
	}
}
