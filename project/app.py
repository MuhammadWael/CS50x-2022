import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained face detection model (e.g., Haar Cascade)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Display my Logo 
logo_image_path = 'logo.png'
st.sidebar.image(logo_image_path, width=100)

# Load the pre-trained emotion recognition model
model = load_model('facial_recognition_model.h5')

st.title("Face Emotion Recognition")

# File uploader for the input photo
input_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if input_image is not None:
    # Read and preprocess the input photo
    input_image = cv2.imdecode(np.fromstring(input_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert the input image to grayscale
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        st.error("No faces detected in the input image.")
    else:
        for (x, y, w, h) in faces:
            # Crop the face region
            face_roi = gray[y:y + h, x:x + w]

            # Resize the cropped face to match the model's input size
            width, height = 48, 48
            face_roi = cv2.resize(face_roi, (width, height))

            # Normalize the cropped face
            face_roi = face_roi / 255.0

            # Reshape the cropped face to match the input shape expected by the model
            face_roi = np.reshape(face_roi, (1, width, height, 1))  # Use 1 channel (grayscale)

            # Make emotion predictions
            output = model.predict(face_roi)

            # Interpret the output
            emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
            predicted_emotion = emotion_labels[np.argmax(output)]

            # Draw a rectangle around the detected face
            cv2.rectangle(input_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the image with emotion label
            label = f"Emotion: {predicted_emotion}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 2
            font_thickness = 3
            label_size, _ = cv2.getTextSize(label, font, font_scale, font_thickness)

            # Calculate text position above the green square
            text_x = x + (w - label_size[0]) // 2
            text_y = y - 10

            cv2.putText(input_image, label, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
            
        # Display the modified image
        st.image(input_image, channels="BGR", use_column_width=True)