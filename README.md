# Vidhai Bot: Automated AI Content Engine for LinkedIn 🚀

**Vidhai Bot** is a fully automated, full-stack AI agent designed to manage personal branding and professional presence on LinkedIn. 

Built with **Python**, **Google Gemini 2.5**, and the **LinkedIn REST API**, this tool functions as an autonomous social media manager. It generates context-aware content, designs photorealistic educational visuals, and publishes directly to LinkedIn without any manual intervention.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works-architecture)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Future Scope](#-future-scope)
- [Contact](#-contact)

---

## 🤖 About the Project

Managing a founder's profile or a company page requires consistency, creativity, and visual appeal. **Vidhai Bot** solves the problem of "writer's block" and manual scheduling by automating the entire pipeline.

Unlike simple text generators, this bot understands **context**. It doesn't just write a post; it selects a specific *persona* (e.g., The Storyteller, The Myth-Buster), generates a hook-based caption, and simultaneously engineers a complex image prompt to create a relevant, high-quality visual implementation of the topic.

---

## ✨ Key Features

### 1. 🎭 Dynamic Persona Engine
The bot never sounds robotic. It randomly selects from 6+ distinct writing styles for every run:
- **The Myth-Buster:** Challenges common industry misconceptions.
- **The Storyteller:** Uses narrative structures to explain complex AI concepts.
- **The Visionary:** Focuses on future trends and high-level insights.
- **The Teacher:** Educational, "Did you know?" style content.

### 2. 🧠 Dual-Prompt Generative Architecture
We use a two-step prompting strategy with **Google Gemini 2.5**:
- **Prompt A (Text):** Generates the LinkedIn caption with hooks, emojis, and hashtags.
- **Prompt B (Visual Engineering):** Generates a separate, highly detailed engineering prompt for the image generator (e.g., specifying camera angles, lighting, and "no text" constraints).

### 3. 🎨 Informative Visual Generation
Integration with **Pollinations AI** allows for the creation of seed-based, photorealistic images. The bot ensures images are **contextually accurate**—if the topic is "Python," it generates a code screen; if "Healthcare," it generates medical tech visuals.

### 4. 🚀 Native Media Upload Pipeline
Instead of sharing simple external links (which get lower reach), the bot performs a **3-stage native upload**:
1. **Register:** Handshake with LinkedIn's asset server.
2. **Upload:** Binary transfer of the high-res image.
3. **Publish:** Creation of a User Generated Content (UGC) post referencing the uploaded asset.

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **GenAI Model:** Google Gemini 2.5 Flash (via `google-genai` SDK)
- **Image Generation:** Pollinations AI API
- **Social API:** LinkedIn v2 REST API (OAuth 2.0)
- **Utilities:** `requests`, `urllib`, `os`, `json`, `random`

---

## 🏗 How It Works (Architecture)

1.  **Trigger:** The script initiates and selects a random **Topic** (from a curated list of 15+ AI domains) and a **Style**.
2.  **Ideation (Gemini):** The LLM generates the post text and a specific visual description based on the selected topic/style combination.
3.  **Visualization (Pollinations):** The script parses the visual description and fetches a high-resolution (1200x627) image, saving it locally.
4.  **Deployment (LinkedIn):**
    * The bot authenticates using the Access Token.
    * It uploads the image to LinkedIn's secure media servers.
    * It combines the uploaded image URN with the generated text to publish the final post.
5.  **Cleanup:** Local temporary files are removed to keep the environment clean.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher installed.
- A LinkedIn Developer Account with an App created.
- A Google AI Studio API Key.

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/LOGESH-28/Vidhai-Bot-Automated-AI-Content-Engine-for-LinkedIn.git](https://github.com/LOGESH-28/Vidhai-Bot-Automated-AI-Content-Engine-for-LinkedIn.git)
   cd Vidhai-Bot-Automated-AI-Content-Engine-for-LinkedIn
   
2.Create a Virtual Environment (Recommended)
Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3.Install Dependencies
Bash
pip install requests google-genai
