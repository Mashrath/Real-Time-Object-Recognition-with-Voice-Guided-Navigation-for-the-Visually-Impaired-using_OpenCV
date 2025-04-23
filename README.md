# Real-Time Object Recognition with Voice Guided Navigation for the Visually Impaired using OpenCV

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologiesused)
- [How to Use](#howtouse)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is designed to assist visually impaired individuals by integrating real-time object detection, voice assistance, and navigation features. With multilingual support and a customizable settings page, the system enhances accessibility, independence, and mobility.

## Features

Object Detection: Identifies and announces objects in the environment.

Voice Assistance: Provides real-time verbal feedback on detected objects.

Navigation: Assists users in movement by guiding them safely.

Multilingual Support: Supports multiple languages for a wider reach.

Settings Page: Allows users to personalize preferences and configurations.

## Technologies Used

Frameworks: Flask, Flask-CORS

Libraries: NumPy, OpenCV, Torch, Torchvision, Pillow, Ultralytics, pyttsx3, playsound, Transformers, gTTS

Deep Learning Models: SSD_MobileNet, IC_ResNet34, YOLOv8n, Frozen Inference Graph (GP Model)

## How to Use

git clone https://github.com/21b01a0538/Real-Time-Object-Recognition-with-Voice-Guided-Navigation.git

## Installation

### 1. Backend Setup

### Create and activate a virtual environment

python -m venv venv

source venv/bin/activate  # On macOS/Linux

venv\Scripts\activate  # On Windows

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the backend server

python app.py

### 4. Frontend Setup

Install dependencies

npm i

### 5. Start the frontend server

npm run dev

## Usage

Start both the frontend and backend servers.

Allow camera and microphone access.

The system will detect objects and provide voice guidance.

Customize settings as per your preference.

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.

For any inquiries, contact 21b01a0538@svecw.edu.in
