# Raspberry Pi Wearable Device: Voice Assistant & Fall Detection System

## Project Overview
This project is a smart wearable device based on Raspberry Pi, integrating a voice interaction assistant and real-time fall detection functionality, specifically designed for the elderly and individuals requiring special care. The device uses sensors to monitor body movement in real-time, automatically triggering an alarm when a fall is detected and enabling help-seeking through the voice assistant. It also supports voice control for weather queries, time announcements, emergency contacts, and more.

## Features

### Real-time Fall Detection: 
Identifies fall actions via accelerometer and gyroscope data

### Voice Interaction Assistant: 
Supports natural language dialogue for commands, information queries, and voice playback

### Emergency Response System: 
Automatically triggers alarms on falls and enables voice calls to preset contacts

## Hardware Requirements
Raspberry Pi 5 (mine is 16 GB version) \
Sensor	MPU6050 (6-axis accelerometer + gyroscope) \
Microphone + Speaker 

## Software Dependencies
Raspberry Pi OS \
Python 3.8

## Installation Steps

1. System Preparation
```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt install espeak # local TTS engine
```

2. Hardware Connection \
MPU6050 connection: \
`VCC → Raspberry Pi 5V` \
`GND → Raspberry Pi GND` \
`SDA → Raspberry Pi GPIO2` \
`SCL → Raspberry Pi GPIO3` \
Microphone/speaker connection

3. Clone the Project
```
git clone https://github.com/LiRongchuan/raspbot-public.git
cd raspbot
```

4. Install Dependencies
```
pip install -r requirements.txt
```

5. Configure API Key \
Get Aliyun API key by login https://bailian.console.aliyun.com/ \
Get ServerChan API key by login https://sct.ftqq.com/

6. Run Program
```
python main.py
```