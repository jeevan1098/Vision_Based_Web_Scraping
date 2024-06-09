from selenium import webdriver
from openai import OpenAI
import base64

driver = webdriver.Chrome()
driver.get("https://github.com/jeevan1098")
driver.save_screenshot("screenshot.png")
driver.quit()

def encode_image(image_path):
  with open(image_path, "rb") as image_file: 
    return base64.b64encode(image_file.read()).decode('utf-8') 

client = OpenAI()

base64_image = encode_image('screenshot.png')
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Your are a conversion optimization specialist. Please tell me what I can improve. "
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}" 
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Overall, the webpage looks clean and modern, but with some optimization, it could further improve user engagement and conversion rates. Here are some suggestions:\n\n1. **Cookie Consent Banner:**\n   - Move the banner to the bottom of the page to avoid blocking key content.\n   - Simplify the language and make the \"Accept\" button more prominent compared to \"Reject\" to guide users towards consenting.\n\n2. **Hero Section:**\n   - Make the CTA (Call to Action) button stand out more by using a contrasting color.\n   - Consider a more engaging headline that highlights a unique selling proposition (USP).\n\n3. **Testimonials:**\n   - Include a photo or a video testimonial of the professor to add credibility.\n   - Add a carousel format to display multiple testimonials.\n\n4. **Course Listings:**\n   - Ensure each course has a brief description and a clear CTA like \"Learn More\" or \"Enroll Now.\"\n   - Use a consistent design for all course cards, including imagery, fonts, and colors.\n\n5. **Urgency and Scarcity:**\n   - Add a countdown timer to indicate limited time offers, such as the 7-day free trial.\n   - Display how many spots are left in popular courses to create urgency.\n\n6. **Trust Elements"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)