import requests

chatgpt_endpoint = "https://api.openai.com/v1/chat"

# Set up the API call parameters
api_key = "YOUR_API_KEY"
model = "chat"
prompt = "Hello, how are you today?"

# Make the API call
response = requests.post(
    chatgpt_endpoint,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": model,
        "prompt": prompt,
    },
)

# Print the response from the API
print(response.json())


