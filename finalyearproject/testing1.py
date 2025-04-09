import os
import cv2  # For reading images
from groq import Groq

# Initialize Groq client
client = Groq(
    api_key="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",
)


# Function to read and preprocess an image
def read_and_preprocess_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"Image at {image_path} could not be loaded.")

    # Resize the image to a common size (e.g., 224x224 for model compatibility)
    resized_image = cv2.resize(image, (224, 224))

    # Normalize the image (convert pixel values from [0, 255] to [0, 1])
    normalized_image = resized_image / 255.0

    # Return the preprocessed image
    return normalized_image


# Example: Read and preprocess an image (replace 'path_to_image.jpg' with your actual image path)
image_path = 'image/timetable1.png'
preprocessed_image = read_and_preprocess_image(image_path)

# Now, you can integrate this into your Groq chat completion, using the image as context.
# Here, you could potentially describe the image or use the extracted text (via OCR) in the conversation.

# Assuming the image contains information related to the query
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful study organizer. My timetable is Monday: Data Mining (9am-11am), Management (11am-1pm), Network (4pm-6pm)  Tuesday: Database (1pm-3pm), Data Visualization (4pm-6pm)  Wednesday: Database (9am-11am), Data Mining (11am-1pm), Management (2pm-4pm)  Thursday: Network (2pm-4pm), Data Visualization (4pm-6pm)"
        },
        {
            "role": "user",
            "content": "Can you help me arrange my study time for every subject on friday and weekends, they can work on 6 hours at most. Avoid arranging before 9am, after 9pm, lunch and dinner. make it into a list for easy understanding",
        },

    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)
