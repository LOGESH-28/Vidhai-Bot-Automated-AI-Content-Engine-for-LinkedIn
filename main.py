import os
import requests
import json
import urllib.parse
import random
from google import genai 

# ---------------------------------------------------------
# 1. CONFIGURATION (Unga Keys)
# ---------------------------------------------------------

# Personal ID (Logesh S)


# ---------------------------------------------------------
# 2. DATA LISTS (Topics + WRITING STYLES)
# ---------------------------------------------------------
AI_TOPICS = [
    "AI Agents assisting workflow", "Generative AI in Marketing", "Python for Automation",
    "Future of LLMs", "AI in Healthcare", "Ethical AI", "AI Tools for Students",
    "Natural Language Processing", "Computer Vision", "Small Business AI",
    "No-Code AI", "Data Visualization", "Machine Learning basics",
    "Personalized Education", "Productivity Hacks"
]

# PUDHU FEATURE: Vera vera styles la eludha solrom
POST_STYLES = [
    "The Myth-Buster (Start by challenging a common belief. Use 'Stop doing X, do Y' tone)",
    "The Storyteller (Start with 'Imagine this...' or a relatable scenario)",
    "The Minimalist (Short, punchy sentences. One powerful idea. Clean look)",
    "The Visionary (Excited tone about the future. High energy)",
    "The Teacher (Did you know? style. Educational and calm)",
    "The Questioner (Start with a provoking question. Engage the reader)"
]

# ---------------------------------------------------------
# 3. GENERATE CONTENT (Style + Emoji + Info Image)
# ---------------------------------------------------------
def generate_content():
    # 1. Pick Topic AND Style
    today_topic = random.choice(AI_TOPICS)
    today_style = random.choice(POST_STYLES)
    
    print(f"🎯 Topic: {today_topic} | 🎭 Style: {today_style}")
    print("🧠 Gemini Generating Viral Content...")
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    You are Logesh S, Founder of 'Vidhai AI Solutions'.
    Write a LinkedIn post about: '{today_topic}'.
    
    **CRITICAL WRITING STYLE:**
    Adopt this specific persona: **{today_style}**.
    
    **TEXT RULES:**
    1. **Hook:** Start with a killer first line that grabs attention immediately.
    2. **Emojis:** Use relevant emojis 🚀💡🤖 naturally (don't overdo it, make it readable).
    3. **Length:** Keep it under 80 words. Short paragraphs.
    4. **Formatting:** Use bullet points if listing things. NO Bold text (**).
    5. **Branding:** Mention 'Vidhai AI Solutions' smoothly.
    6. **Hashtags:** End with 3-4 powerful hashtags.
    
    **IMAGE PROMPT RULES:**
    At the end, add a new line starting with 'IMAGE_PROMPT:'.
    Describe a **realistic, informative scene** explaining '{today_topic}'.
    - Must look like a professional photo or high-end 3D render.
    - Example: 'A doctor holding a glowing tablet with AI DNA analysis, realistic, 8k'.
    - NO text inside the image.
    """
    
    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        text = response.text.strip().replace("**", "") # Remove bolding
        
        if "IMAGE_PROMPT:" in text:
            post_text = text.split("IMAGE_PROMPT:")[0].strip()
            image_prompt = text.split("IMAGE_PROMPT:")[1].strip()
        else:
            post_text = text
            image_prompt = f"Professional photography of {today_topic} in a modern setting, 8k, highly detailed"
            
        print(f"🖼️ Image Concept: {image_prompt}")
        return post_text, image_prompt
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return None, None

# ---------------------------------------------------------
# 4. DOWNLOAD IMAGE
# ---------------------------------------------------------
def download_image(prompt):
    print("🎨 Downloading High-Quality Image...")
    # Keywords for professional look
    safe_prompt = urllib.parse.quote(f"{prompt}, photorealistic, cinematic lighting, 8k, depth of field")
    
    seed = random.randint(1, 1000)
    image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1200&height=627&nologo=true&seed={seed}"
    
    response = requests.get(image_url)
    if response.status_code == 200:
        with open("temp_image.jpg", "wb") as f:
            f.write(response.content)
        print("✅ Image saved.")
        return "temp_image.jpg"
    else:
        print("❌ Failed to download image")
        return None

# ---------------------------------------------------------
# 5. UPLOAD & POST TO LINKEDIN
# ---------------------------------------------------------
def register_upload():
    url = "https://api.linkedin.com/v2/assets?action=registerUpload"
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}
    
    payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": LINKEDIN_USER_URN,
            "serviceRelationships": [{"relationshipType": "OWNER", "identifier": "urn:li:userGeneratedContent"}]
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        upload_url = data['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
        asset_urn = data['value']['asset']
        return upload_url, asset_urn
    else:
        print(f"❌ Register Upload Failed: {response.text}")
        return None, None

def upload_binary(upload_url, image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}"}
    response = requests.put(upload_url, headers=headers, data=image_data)
    if response.status_code == 201:
        print("✅ Image Uploaded.")
        return True
    else:
        print(f"❌ Binary Upload Failed: {response.text}")
        return False

def create_post(text, asset_urn):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}
    
    payload = {
        "author": LINKEDIN_USER_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "IMAGE", 
                "media": [
                    {
                        "status": "READY",
                        "media": asset_urn,
                        "title": {"text": "AI Insight"},
                        "description": {"text": "Generated by Vidhai Bot"}
                    }
                ]
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("\n🎉 SUCCESS! Engaging Post Published.")
    else:
        print(f"❌ Post Creation Failed: {response.text}")

# ---------------------------------------------------------
# 6. EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    text, img_prompt = generate_content()
    
    if text and img_prompt:
        image_path = download_image(img_prompt)
        if image_path:
            upload_url, asset_urn = register_upload()
            if upload_url and asset_urn:
                if upload_binary(upload_url, image_path):
                    create_post(text, asset_urn)
                    os.remove(image_path)