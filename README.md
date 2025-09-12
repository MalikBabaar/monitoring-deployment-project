# Monitoring & Deployment Automation Project

## Project Overview
This project consolidates foundational skills in Python automation, system monitoring, Nginx deployment, file handling, and Ansible automation through a real-world example.

---

## Features

- **Log Monitoring & Alerting using Python:**  
  Continuously monitors Nginx error logs and alerts when specified keywords (e.g., "error") are found.

- **System Resource Monitoring:**  
  Checks CPU, memory, and disk usage and prints alerts if thresholds (80%) are exceeded.

- **Nginx Server Deployment:**  
  Automated deployment and start of Nginx using Ansible playbooks.

- **File Handling & OS Automation in Python:**  
  Scripts to move files, monitor logs, and automate system checks.

- **Basic Ansible Playbooks:**  
  For remote configuration, package installation, and service management.

---

## Project Structure

monitoring-deployment-project/
├── playbooks/ # Ansible playbooks for deployment & config
├── python-scripts/ # Python scripts for monitoring & automation
│ ├── log_monitor.py
│ ├── system_monitor.py
│ └── file_handler.py
├── README.md

## How to Use

### Clone the repo

https://github.com/MalikBabaar/monitoring-deployment-project.git

cd monitoring-deployment-project

### 1. Deploy Nginx Server
Run the Ansible playbook to install and start Nginx:

ansible-playbook app-install.yml

### 2. Access Nginx

Find your VM’s IP address (e.g., using ip addr show).

Access via browser: http://<VM_IP_Address>

### 3. Log Monitor

Monitors the Nginx error log for the keyword "error".

sudo python3 log_monitor.py

### 4. System Resource Monitor

Checks CPU, memory, and disk usage and alerts if usage exceeds 80%

sudo python3 system_monitor.py

### 5. 4. Creating a Fake Error to Test log_monitor.py

To verify that the log monitor detects errors:

Append a fake error message to the Nginx error log:

sudo sh -c 'echo "[error]  test error for monitoring script" >> /var/log/nginx/error.log'


Run the log monitor script if it’s not running:

sudo python3 python-scripts/log_monitor.py


You should see output like:

[ALERT] Found 'error': [error]  test error for monitoring script
