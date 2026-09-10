# 🚀 AUTOMATED COLAB LOCAL AI SERVER WITH KEEP-ALIVE & AUTO-TUNNEL
# This script runs Ollama with DeepSeek-Coder/Llama3 on Colab GPU with automated Ngrok tunneling.

import os
import subprocess
import time
import urllib.request
import json

print("⚡ Step 1: Installing Ollama and Tunneling Utilities...")
os.system("curl -fsSL https://ollama.com/install.sh | sh")
os.system("pip install pyngrok -q")

print("🤖 Step 2: Starting Ollama Local AI Engine in Background...")
ollama_proc = subprocess.Popen(["ollama", "serve"])
time.sleep(5)

print("📥 Step 3: Pulling DeepSeek-Coder High-Performance Model...")
os.system("ollama pull deepseek-coder:6.7b")

print("🌐 Step 4: Establishing Persistent Public Tunnel...")
from pyngrok import ngrok
# Set NGROK_AUTHTOKEN via environment variable or prompt
NGROK_TOKEN = os.environ.get("NGROK_AUTHTOKEN", "YOUR_NGROK_AUTHTOKEN")
if NGROK_TOKEN != "YOUR_NGROK_AUTHTOKEN":
    ngrok.set_auth_token(NGROK_TOKEN)

public_url = ngrok.connect(11434, "http").public_url
print(f"\n=======================================================")
print(f"✅ COLAB LOCAL AI SERVER IS LIVE & READY!")
print(f"🔗 LOCAL AI API URL: {public_url}")
print(f"=======================================================\n")

# Auto Update Configuration payload for Codespaces
config_payload = {
    "local_ai_url": public_url,
    "status": "online",
    "timestamp": time.time()
}
with open("colab_ai_status.json", "w") as f:
    json.dump(config_payload, f)

print("🔄 Step 5: Persistent Keep-Alive Loop Running (Prevents Colab Timeout)...")
while True:
    try:
        # Pings every 60 seconds to maintain active session
        urllib.request.urlopen("http://localhost:11434")
        time.sleep(60)
    except Exception as e:
        print("Re-establishing ping...")
        time.sleep(10)
