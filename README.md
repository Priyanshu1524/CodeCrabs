🦀 CodeCrab – Universal Video Downloader
CodeCrab is a full-stack web application that allows users to download videos from public platforms like YouTube, Vimeo, and more. Built using Flask (Python) and yt-dlp, it provides format, resolution, and metadata extraction with a clean user interface.
🚀 Features

🎥 Download from YouTube, Vimeo, and other public video sources
📺 View available formats, resolutions, and metadata
⚙️ Modular codebase with clear separation for extraction and routing
💻 Built with Flask, Jinja2, and Python subprocess
☁️ Deployment-ready for Heroku and other cloud platforms

🧑‍💻 Getting Started
Prerequisites

Python 3.7 or higher
pip (Python package manager)
Git

Installation
1. Clone the Repository
bashgit clone https://github.com/your-username/codecrab.git
cd codecrab
2. Create and Activate a Virtual Environment
bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Run the Application
bashpython app.py
The application will be available at: http://127.0.0.1:5000

🛠️ Technology Stack

Backend: Flask (Python)
Video Processing: yt-dlp
Frontend: HTML, CSS, JavaScript
Template Engine: Jinja2

🚀 Deployment
Heroku Deployment

Create a Procfile in the root directory:

web: python app.py

Ensure your requirements.txt includes all dependencies
Deploy to Heroku:

bashheroku create your-app-name
git push heroku main
