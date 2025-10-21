🧠 HomeMindAI
AI-Powered Smart Home Safety & Care System

Autonomous monitoring, intelligent alerts, and agentic control — powered by AWS SageMaker, Bedrock, and IoT.

🌍 Project Overview

HomeMindAI is an AI surveillance and assistance system that continuously watches over your home environment, detects critical and daily-life events, and takes autonomous actions through AI agents.

It’s designed especially for:

Elderly care and safety
Student activity monitoring
Visitor and anomaly detection
Smart appliance control

Built as part of the AWS AI Agent Hackathon, this project demonstrates SageMaker Vision inference, Bedrock reasoning logic, and IoT + SNS automation — integrated into a beautiful unified dashboard.

🏗️ Architecture Overview
🔹 Core Flow
CCTV / NFC / Audio Inputs
        ↓
AWS SageMaker Vision / Rekognition  →  Event classification
        ↓
AWS Bedrock (Head Robo) → Context reasoning
        ↓
Assist Robo (backend & IoT agent)
        ↓
Dashboard Timeline + Alerts (voice, SMS, IoT control)

🔹 AWS Services Used
AWS Service	Role
SageMaker / Rekognition	Vision inference (detect events, faces, fire, etc.)
Bedrock AgentCore	LLM reasoning and voice interaction
SNS	Notifications to caregivers and users
IoT Core	Device control (turning plugs off, lights on)
Lambda	Event orchestration and processing
CloudFormation	Infrastructure as code
S3	Data and media storage
CloudFront	Public dashboard hosting
Elastic Beanstalk / ECS	Backend API hosting
🔍 Event Detection Catalog
#	Event Name	Detection Method	AI / Sensor Input	Action Triggered
1	Celebration Detected	CCTV Vision + Audio pattern	Birthday / social gathering scene	Dashboard “pulse” + ambient label
2	Fall Detected	Vision Pose Estimation	Elderly person falls	Alert → caregiver SMS + voice prompt
3	Visitor Verified	Face Recognition + Vision	Person at door	Ask purpose, match known faces
4	Unknown Visitor	Face mismatch	Entry attempt	Sends alert + optional lock
5	Fire / Smoke Anomaly	Vision + Color threshold	Kitchen smoke, sparks	IoT plug-off + dashboard alert
6	Chaotic Motion	Motion Vector AI	Multiple sudden movements	“Disturbance Detected” alert
7	Student NFC Entry/Exit	NFC Scan	Bag tag or gate reader	Logs attendance to dashboard
8	Academic Update Received	Teacher API / SMS webhook	Notifications from school	Adds to student timeline
9	Medication Reminder	Scheduled AI rule	Voice TTS alert	Reminds elderly to take medicine
10	Missed Confirmation	Timeout rule	No tablet scan or voice response	Escalates to caregiver
11	Emergency Escalation	Multi-condition AI	Fall + no response + smoke	Triggers emergency call
12	System Health	IoT + heartbeat	Device uptime check	Alerts if sensors offline
🖥️ Dashboard Features

The HomeMindAI Dashboard is your control center.

It displays:

🎥 Live CCTV feeds (or uploaded demo videos)
🧩 Event Timeline — color-coded event cards (auto-refresh)
🔔 Real-time notifications (pop-up + voice)
📦 NFC & Student Logs
🧭 IoT Device Control Panel (e.g., switch plugs)
📊 System Health Summary

Dashboard Actions:
Action	Description
Upload Video	Upload CCTV clip to run SageMaker inference manually
Timeline View	Shows events detected automatically
Event Replay	Play back recorded events
Device Control	Switch off/on appliances
Voice Alerts	Text-to-Speech or notification tones
Reports Export	Generate daily activity reports for family/caregivers
🤖 AI Agents in the System
🧠 Head Robo (Reasoning Layer)

Runs on AWS Bedrock AgentCore (or Together.ai LLM)

Interprets events (“fall” → “elderly distress”)
Decides what actions to take (alert caregiver, trigger plug, etc.)

⚙️ Assist Robo (Action Layer)

Executes tasks (IoT, voice, dashboard updates)
Calls SageMaker for detections and updates event logs

🧩 Directory Structure
HomeMindAI/
├── backend/              # FastAPI + AWS SDK backend
├── dashboard/            # React + Tailwind frontend
├── lambda/               # AWS Lambda functions
├── infra/                # CloudFormation + deploy scripts
├── scripts/              # Test & upload utilities
├── docs/                 # Architecture + assets
└── README.md

⚙️ Installation (Local Setup – AlmaLinux / Windows)

Clone the repo

git clone https://github.com/yourusername/HomeMindAI.git
cd HomeMindAI


Backend Setup

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5002


Frontend Setup

cd dashboard
npm install
npm run dev


Access via http://localhost:4050

Test Upload
Open Dashboard → Upload Video → Select any synthetic clip (fall, fire, stranger)
See result displayed instantly.

☁️ AWS Deployment Steps (Public Demo)

Configure AWS CLI
aws configure


Create Artifact Bucket
aws s3 mb s3://homemindai-artifacts-yourname


Deploy Infrastructure

cd infra
aws cloudformation deploy \
  --stack-name HomeMindAI-Infra \
  --template-file homemindai-infra.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides ArtifactBucketName=homemindai-artifacts-yourname ProjectSuffix=homemind


Host Dashboard
Build: npm run build
Upload /build folder to S3
Add CloudFront for HTTPS → get public URL (for judges)

Deploy Backend

cd backend
eb init -p docker homemindai-backend
eb create homemindai-env


Connect Dashboard to Backend
Update REACT_APP_API_URL in .env.production → rebuild + re-upload frontend.

🧪 Testing the AI Pipeline
1️⃣ Upload Event Videos

Upload these demo videos (already generated):

fall_detect.mp4
fire_kitchen.mp4
visitor_unknown.mp4
celebration_home.mp4

2️⃣ SageMaker/AI Detection

Each upload triggers:
Extract key frame(s)
Send to SageMaker Vision endpoint
Get event label + confidence
Store in timeline + send alert

3️⃣ Verify on Dashboard

Event appears on timeline
Matching icon flashes
“AI Detected” overlay visible

4️⃣ (Optional) IoT Action

If “fire” detected → Smart plug OFF
If “visitor unknown” → Lock ON

🧾 Example Alerts
Event	Voice / Notification	IoT / Action
Fall Detected	“Emergency — a fall has been detected!”	Notify caregiver
Smoke Detected	“Warning — possible fire hazard.”	Smart plug off
Visitor Unknown	“Unrecognized visitor detected.”	Doorbell camera alert
Celebration Detected	“Joyful activity detected.”	Passive label only
Medication Reminder	“It’s time for your 7PM tablets.”	Voice + alert tone
🔐 Security & Privacy

No real identities — all data synthetic.
Secure IAM roles for Lambda + SageMaker access.
S3 and SNS communication protected via AWS encryption and policy controls.
No API keys exposed in frontend.

🏁 Final Output & Judge Demo

Public Dashboard URL:

https://dashboard-homemindai.cloudfront.net


Demo Flow (3-minute video):

🎂 Celebration detected → ambient classification
🧓 Fall event → caregiver alert + dashboard replay
🚪 Visitor verification → face match & remote unlock
🔥 Smoke anomaly → plug OFF + notification
🧠 Architecture & SageMaker summary screen

Judges’ Experience:

Real-time AI inference
Event cards updating dynamically
Live alerts and IoT reactions
End screen showing repository + architecture

🧰 Tools & Technologies
Category	Tech
AI & ML	AWS SageMaker, AWS Bedrock, OpenAI-compatible APIs
Frontend	React, TailwindCSS, Vite
Backend	FastAPI, Python, Boto3
Cloud	AWS CloudFormation, SNS, IoT, Lambda, CloudFront
Data Storage	Amazon S3
Voice / TTS	pyttsx3 / AWS Polly
Video Test Tools	OpenCV, SageMaker SDK
💡 Future Enhancements

Integrate real IoT sensors and smart locks
Add multilingual voice assistant
Use Bedrock AgentCore for dynamic reasoning
Enable dashboard mobile companion app
Continuous learning model for home-specific events

🧑‍💻 Authors

Team Twin Robo
Head Robo 🤖 — GPT-OSS Reasoning Agent
Assist Robo ⚙️ — Execution + IoT + Dashboard Logic

📚 License

MIT License © 2025 — for research and educational demo purposes.