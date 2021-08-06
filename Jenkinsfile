pipeline {
	agent {
		docker { image 'python:3.9.6' }
	}
	stages {
		stage('build') {
			steps {
				sh 'python3 --version'
				sh 'python3 -m pip install pipenv'
				sh 'python3 -m pipenv shell'
				sh 'python3 -m pip install -r requirements.txt'
				sh 'python3 src/app.py' 
			}
		}
	}
}
