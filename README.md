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

## Make sure the following are installed on your system:

### 1. Python 3.8+  
Install Python and `pip` if not already available.

```bash
sudo apt update
sudo apt install python3 python3-pip

### 2. Ansible

Install Ansible for running deployment playbooks:

pip install ansible

Alternative:

sudo apt install ansible    # Debian/Ubuntu

## How to use

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

### 5. Creating a Fake Error to Test log_monitor.py

To verify that the log monitor detects errors:

Append a fake error message to the Nginx error log:

sudo sh -c 'echo "[error]  test error for monitoring script" >> /var/log/nginx/error.log'


Run the log monitor script if it’s not running:

sudo python3 python-scripts/log_monitor.py


You should see output like:

[ALERT] Found 'error': [error]  test error for monitoring script


<img width="1919" height="1079" alt="Screenshot 2025-09-12 115622" src="https://github.com/user-attachments/assets/d44114d8-6104-4a8d-8a7c-ce62900b8550" />
<img width="1919" height="1079" alt="Screenshot 2025-09-12 115637" src="https://github.com/user-attachments/assets/6e30cf92-b9c8-4374-bc5c-0b2d9d2bde95" />
<img width="1919" height="1079" alt="Screenshot 2025-09-12 123737" src="https://github.com/user-attachments/assets/5f8a313c-183e-4e52-9c5b-461b7b2202ac" />


