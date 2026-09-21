# AWS Flask Deployment Demo

A small Flask application deployed to an Amazon EC2 instance as a hands-on AWS learning project.

## What I built

I developed a Flask application locally, pushed the code to GitHub, and deployed it to an Amazon Linux 2023 EC2 instance in the AWS Ireland Region.

The deployment used:

* **Flask** for the web application
* **Git and GitHub** for version control and transferring the code
* **Python virtual environment** for project dependencies
* **Gunicorn** to serve the Flask application
* **Nginx** to accept HTTP requests on port 80 and forward them to Gunicorn
* **systemd** to manage the Gunicorn service

## How requests reached the app

Browser → EC2 public IP (HTTP, port 80) → Nginx → Gunicorn (localhost, port 8000) → Flask

## What I learned

* Connecting securely to an EC2 instance using SSH and a private key
* Installing software and managing a Python environment on Linux
* Troubleshooting a Python-version mismatch during dependency installation
* Testing an application locally on the server before exposing it publicly
* Configuring a reverse proxy and a systemd service
* Checking for leftover AWS resources after terminating an instance

## Deployment status

**This is a completed demonstration, not a currently hosted website.** I tested the application successfully through the EC2 public IP, then terminated the instance and checked that no EBS volumes, Elastic IPs, or snapshots remained in the Ireland Region.

## Run locally

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows Git Bash**

```bash
source .venv/Scripts/activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install dependencies and run the app:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser. The local command uses Flask’s development server; it is not intended for public deployment.
