📊 Personal Expense Tracker

-> A web-based Personal Expense Tracker built using Flask, Bootstrap, and AWS DynamoDB. It helps users set a monthly budget, add expenses by category, and view summaries with charts — all stored securely on AWS.

🧰 Tech Stack
| Component  | Technology                     |
| ---------- | ------------------------------ |
| Frontend   | HTML, CSS, Bootstrap, Chart.js |
| Backend    | Flask (Python)                 |
| Database   | AWS DynamoDB                   |
| Deployment | AWS EC2 (Ubuntu/CentOS)        |
| Cloud CLI  | AWS CLI + Boto3                |

 Features
✅ Monthly Budget Setup

✅ Add, View & Categorize Expenses

✅ Summary Dashboard with Charts

✅ Responsive Bootstrap UI

✅ Data stored securely in AWS DynamoDB

✅ Deployed on AWS EC2


🚀 How to Run Locally

1. Clone the Repository
->git clone https://github.com/YOUR_USERNAME/ExpenseTracker.git
->cd ExpenseTracker

2. Set Up Python Environment
->sudo apt update
->sudo apt install python3-pip python3-venv -y
->python3 -m venv venv
->source venv/bin/activate
->pip install -r requirements.txt

3. Configure AWS Credentials
->aws configure
Provide:
AWS Access Key
AWS Secret Key
Region (e.g., us-east-1)
Output format: json

DynamoDB Table Structure
Table: ExpenseTracker
| Key Name      | Type                | Example                               |
| ------------- | ------------------- | ------------------------------------- |
| `PK`          | Partition Key       | `BUDGET#2025-07` or `EXPENSE#2025-07` |
| `SK`          | Sort Key            | `INFO` or `2025-07-16#Food#timestamp` |
| `amount`      | Number              | 1500                                  |
| `category`    | String              | Food                                  |
| `description` | String              | Lunch                                 |
| `date`        | String (YYYY-MM-DD) | 2025-07-16                            |

☁️ Deploying on AWS EC2
1. Launch EC2 Instance
Ubuntu or Amazon Linux (t2.micro for Free Tier)
Create and download a .pem file

2. SSH into EC2
->ssh -i "your-key.pem" ec2-user@your-public-ip

3. Setup Flask App on EC2
->sudo yum update -y    # or sudo apt update -y
->sudo yum install git python3-pip -y

->git clone https://github.com/YOUR_USERNAME/ExpenseTracker.git
->cd ExpenseTracker

->python3 -m venv venv
->source venv/bin/activate
->pip install -r requirements.txt

4. Run the App
python3 app.py

🌐 Access the App
Visit:http://<your -ec2- public-ip4>:5000
🎬 Demo Video:https://drive.google.com/file/d/1LgtqGVY-OXToTIYJkQYwhDD08WsHzrRV/view?usp=sharing

