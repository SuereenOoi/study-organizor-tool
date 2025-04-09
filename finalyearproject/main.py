import os
import cv2
import pytesseract

from groq import Groq

image_path = "timetable.png"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_GRAY2RGBA)
text = pytesseract.image_to_string(gray)
print("Extract text:")
print(text)

client = Groq(
    # This is the default and can be omitted
    api_key= "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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful study assistant."
        },
        {
            "role": "user",
            "content": "Tell me the difference between TCP and UDP",
        }
    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)