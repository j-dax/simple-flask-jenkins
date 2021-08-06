# Simple Jenkins Project with Flask

This is a simple Flask application built with Jenkins on a linux server with the steps to setup.

# Prerequisites

(Jenkins)[https://www.jenkins.io/doc/book/installing]

(Python3)[https://www.python.org/downloads/]

(NGinx)[https://www.nginx.com/resources/wiki/start/topics/tutorials/install/]

# Procedure

## Setup your environment

```
mv flask_app.nginx /etc/nginx/sites-enabled/flask_app
unlink /etc/nginx/sites-enabled/default
```

## Plugins

Log into Jenkins and install the following plugins:

> GitHub
> Pipeline

## New Item

* Setup your new item as a pipeline.
* Scroll down to pipeline and select the Definition:
	* Pipeline script from SCM
* Set SCM to Git
* Fork this repo and point jenkins to your repo
* Provide Jenkins valid GitHub credentials
* Ensure it's pointing at the correct branch
* Hit save

