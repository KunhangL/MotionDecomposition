import base64
import requests

# OpenAI API Key
api_key = "sk-proj-06RQYAtdrIiPqD6Mz7flT3BlbkFJ6lZq6H7V8YFQRmRBoXU8"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# image_path = "test.png"
# image_paths = [
#    "./raise_arms/1.png",
#    "./raise_arms/2.png",
#    "./raise_arms/3.png",
#    "./raise_arms/4.png",
#    "./raise_arms/5.png"
# ]
image_paths = [
   "./squat/1.png",
   "./squat/2.png",
   "./squat/3.png",
   "./squat/4.png",
   "./squat/5.png",
   "./squat/6.png",
   "./squat/7.png",
   "./squat/8.png",
   "./squat/9.png",
]

# Getting the base64 string
# base64_image = encode_image(image_path)
base64_images = []
for image_path in image_paths:
    base64_images.append(encode_image(image_path))

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "This series of images show a consecutive motion. Imagine the whole motion, and choose the most effective way to describe it in a fine-grained manner (no need to describe each image), with reference to the coarse-grained description \'A man slightly squats\'. If the image conflicts with the coarse-grained description, refer to the image as the gold standard.\n\\\
                   The standard of fine-grained is: 1. State in chronological order and step by step. 2. Specify spatial position changes (including angle changes) of relevant body parts. 3. Not specify any information related to muscles."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[0]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[1]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[2]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[3]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[4]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[5]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[6]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[7]}",
            "detail": "low"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_images[8]}",
            "detail": "low"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())