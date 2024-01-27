# Bringing Emotions to the Virtual World

![GitHub repo size](https://img.shields.io/github/repo-size/MuhammadWael/Face_Recognition)
![GitHub issues](https://img.shields.io/github/issues/MuhammadWael/Face_Recognition)
![GitHub stars](https://img.shields.io/github/stars/MuhammadWael/Face_Recognition)
![GitHub forks](https://img.shields.io/github/forks/MuhammadWael/Face_Recognition)
#### Video Demo:  [EmoFace Video](https://youtu.be/RHjpsNxK0Y8)
## Try It Out
Explore EmoFace with our user-friendly deployment. Visit [EmoFace Streamlit App](https://face-recognition-tf.streamlit.app/) and experience it for yourself!

## Description:
In today's digital age, our interactions often lack the depth and nuances of real-life communication. Expressing emotions, understanding reactions, and recognizing sentiments can be challenging in the virtual world. This limitation impacts various aspects of life, from education to the job market. Our project, EmoFace, tackles this issue head-on by using advanced technology to bring emotions and facial expressions to the virtual realm.

## Problem Statement

- In online education, gauging students' understanding and engagement can be challenging due to the absence of physical cues and facial expressions.

- In the job market, it's difficult to determine the popularity of products or applications in real-time, hindering decision-making and market analysis.

## Solution

EmoFace employs a Convolutional Neural Network (CNN) model built with the TensorFlow Keras framework, utilizing the Adam optimizer. Our dataset comprises nearly 34,000 photos, and we've fine-tuned our model through three stages of training with 100, 40, and 200 epochs. We progressively reduced the learning rate from 0.001 to 0.0001 to 0.00001, achieving our target accuracy of 0.7985.

To enhance the practicality and versatility of our system, we've integrated OpenCV for face recognition, allowing it to identify multiple faces within images. For a seamless user experience, we've developed a user-friendly interface using Streamlit for model deployment.

## Features

- **Emotion Recognition:** EmoFace accurately recognizes and labels human emotions in images.

- **Multi-Face Support:** The system can detect and analyze multiple faces within a single image.

- **Customizable Deployment:** Our user-friendly Streamlit interface makes it easy to deploy and utilize the model for a variety of applications.

## How to Use

1. **Clone the Repository:** Start by cloning this repository to your local machine.
   ```bash
   git clone https://github.com/MuhammadWael/Face_Recognition.git
   ```

2. **Install Dependencies:** Install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Dataset and Training:** The pre-trained model and dataset are included. However, if you wish to retrain the model, follow the instructions in the project documentation.

4. **Deployment:** Use Streamlit to deploy the model and access the user-friendly interface for emotion recognition.

## Contribution

We welcome contributions from the community to improve EmoFace further. If you have ideas, bug fixes, or enhancements to offer, please consider contributing by following these steps:

1. **Fork the Repository:** Create a fork of this repository in your own GitHub account.

2. **Create a New Branch:** Develop your features or fixes in a new branch.

3. **Testing:** Ensure your changes are thoroughly tested to maintain project reliability.

4. **Pull Request:** Create a pull request to propose your changes and improvements.

## License

EmoFace is an open-source project and is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

Join us in making virtual interactions more emotionally meaningful. EmoFace - where technology meets emotions.
