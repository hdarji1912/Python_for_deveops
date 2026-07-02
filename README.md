# 🐍 Python for DevOps

> A collection of Python automation scripts built for DevOps engineering. This repository demonstrates practical use cases such as system monitoring, file backups, and AWS S3 automation using Python.
---

## 📌 About

This repository contains hands-on Python scripts focused on solving real-world DevOps tasks through automation.

The goal of this project is to strengthen Python skills while learning infrastructure automation and cloud integration.

---

## 🚀 Projects

### 📊 System Resource Monitor (`utils.py`)

Monitor Linux/Windows system resources.

**Features**

- ✅ CPU Usage Monitoring
- ✅ Disk Usage Monitoring
- ✅ Memory Information
- ✅ Lightweight Monitoring Script

**Skills**

- Python
- os
- shutil

---

### 📦 Local Backup Automation (`backup.py`)

Automates backup creation for local directories.

**Features**

- ✅ Create compressed backup archives
- ✅ Automatic timestamped backup files
- ✅ File and directory management

**Skills**

- shutil
- os
- datetime

---

### ☁️ AWS S3 Backup Automation (`S3_backup.py`)

Uploads local backup files to Amazon S3 using the AWS SDK for Python (Boto3).

**Features**

- ✅ Create Amazon S3 Bucket
- ✅ Upload Backup Files
- ✅ List Available Buckets
- ✅ AWS Cloud Storage Automation
- ✅ Exception Handling

**Skills**

- Boto3
- AWS S3
- Python File Handling
- Cloud Automation

---

## 🛠️ Technologies Used

- Python 3
- AWS S3
- Boto3
- OS Module
- shutil
- datetime
- AWS CLI
- Git
- GitHub

---

## 📂 Repository Structure

```
Python_for_deveops/
│
├── README.md
├── backup.py
├── utils.py
└── S3_backup.py
```

---

## ⚙️ Prerequisites

- Python 3.x
- AWS Account
- AWS CLI Configured
- Boto3

Install dependencies

```bash
pip install boto3
```

Configure AWS CLI

```bash
aws configure
```

---

## ▶️ Run the Scripts

### System Monitoring

```bash
python utils.py
```

### Create Local Backup

```bash
python backup.py
```

### Upload Backup to AWS S3

```bash
python S3_backup.py
```

---

## 📖 What I'm Learning

- Python for DevOps
- Infrastructure Automation
- AWS Cloud Services
- Boto3
- Linux Automation
- Git & GitHub
- DevOps Best Practices

---


## 🤝 Contributions

Suggestions and improvements are welcome. Feel free to fork this repository and submit a pull request.


## 👨‍💻 Author

**Hardik Darji**

🌐 GitHub: https://github.com/hdarji1912

---

⭐ If you found this repository helpful, consider giving it a star!
