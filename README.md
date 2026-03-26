# cloud-autoscale-project

# Local VM to Cloud Auto-Scaling (VCC Assignment)

## Overview

This project demonstrates a basic hybrid cloud setup where a local virtual machine is monitored for resource usage. When CPU or memory usage exceeds a defined threshold (75%), a new EC2 instance is launched on AWS.

The purpose is to simulate a simple auto-scaling mechanism from local environment to cloud.

---

## Tools Used

* Virtualization: UTM
* OS: Ubuntu 25.10 Desktop ARM64
* Programming: Python
* Monitoring: psutil
* Cloud: AWS EC2
* CLI Tool: AWS CLI

---

## Project Structure

```
cloud-autoscale-project/
│
├── app.py                # Sample Flask application
├── monitor.py            # Resource monitoring script
├── scale_to_cloud.sh     # Script to trigger EC2 instance
├── README.md
```

---

## Step 1: Setup Local VM

* Created Ubuntu VM using UTM
* Allocated 4GB RAM, 2 CPU cores and 128 GB ROM

---

## Step 2: Install Dependencies

```
sudo apt update
sudo apt install python3-pip python3-venv -y
```

Create virtual environment:

```
python3 -m venv myenv
source myenv/bin/activate
pip install flask psutil
```

---

## Step 3: Run Application

```
python app.py
```

Access:

```
http://localhost:5000
```

---

## Step 4: Monitoring Script

* The script checks CPU and memory usage every few seconds
* If usage exceeds 75%, it triggers AWS EC2 creation

Run:

```
python monitor.py
```

---

## Step 5: AWS Configuration

Configured AWS CLI:

```
aws configure
```

Inputs used:

* Region: ap-south-1 (Mumbai)
* Output format: json

IAM user was created with EC2 permissions and access keys.

---

## Step 6: Auto Scaling Trigger

* Script `scale_to_cloud.sh` launches EC2 instance using AWS CLI
* Trigger happens when threshold is crossed

---

## Step 7: Deployment to EC2

* Used SCP to transfer `app.py` to EC2
* Installed Flask and ran the application

```
scp -i key.pem app.py ec2-user@<public-ip>:~
ssh -i key.pem ec2-user@<public-ip>
```

---

## Architecture Flow

Local VM → Monitoring Script → Threshold Breach → AWS CLI Trigger → EC2 Instance → App Deployment

---

## Observations

* CPU load can be simulated using curl requests
* Auto scaling works but deployment is manual
* This is a basic simulation and not production-level

---

## Limitations

* No load balancer
* No automatic app deployment
* Single instance scaling only

---

## Conclusion

This project demonstrates a simple approach to hybrid cloud scaling using local VM monitoring and AWS EC2 provisioning.

---

## Plagiarism Declaration

I confirm that this project is implemented by me and no part of it is copied directly from any external source. References were used only for understanding concepts.
