Analyzing Crochet Products into Patterns Using Artificial Intelligence


Business Understanding

💡 The Problem:
We want to develop an intelligent system that can analyze crochet images and convert them into patterns automatically using artificial intelligence.
Main objectives:
✅ Improve the accuracy of recognizing shapes in crochet images
✅ Clearly extract the boundaries of elements
✅ Prepare data for later use in artificial intelligence models


2️⃣ Data Understanding
📸 The data we deal with:
Images containing crochet products in different colors and shapes.
👀 Challenges:
🔹 Diverse backgrounds that may hinder the identification of crochet
🔹 Differences in lighting and colors in the images
🔹 The need to purify the image and isolate the crochet from the background


3️⃣ Data Preparation
At this stage, we used the OpenCV library to process and denoise images, using several techniques such as:
✅ Convert the image to grayscale
✅ Improve contrast using CLAHE
✅ Convert the image to binary (Thresholding)
✅ Extract edges using Canny Edge Detection
✅ Find boundaries using cv2.findContours
📌 Tools and libraries used:
📌 OpenCV (cv2): for image processing
📌 Matplotlib: for displaying images
📌 NumPy: for processing numerical data


4️⃣ Modeling

At this stage, we have defined the boundaries using cv2.findContours(), where the crochet contour is accurately extracted, which helps in building a model later to extract the pattern automatically.
🔹 We can now improve the model using Deep Learning algorithms such as YOLO or Mask R-CNN to automatically recognize the different parts of the crochet.
5. Evaluation
Objective: Evaluate the performance of the system based on the results of the analysis and generation.


Evaluation criteria:
Accuracy of image analysis (are the details extracted accurately?).
Accuracy of pattern instructions (are the instructions executable?).
User satisfaction with the results of the displayed pattern.
Steps:
Test the system using various images.
Ensure that the interpretation and generation are accurate and realistic.

5️⃣ Evaluation

🔍 We checked the accuracy of the edge extraction by visualizing the results, and we saw that some edges need improvement.
⚡ Performance can be improved using:
✅ Adjusting the Threshold values ​​in cv2.threshold()
✅ Using advanced filtering like GaussianBlur or Bilateral Filter
✅ Adjusting the cv2.Canny() parameters to make the edges more visible



Project Overview

Business Understanding:

Objective: Define the goal of the project and explain how to achieve it.
In this project, the goal is to create a system that uses artificial intelligence to generate crochet patterns based on a text description from the user. The project also includes the ability to upload images and analyze them to automatically generate crochet patterns.

Data Understanding:

Objective: Collect and analyze data to better understand it.
In this project, the data will be either:
Textual description provided by the user (such as pattern details: stitches, size, type of yarn, etc.).
Images (if used to analyze patterns in crochet) if you intend to incorporate image analysis.
Tools used:
Python: To develop and train models.
Jupyter Notebook: An interactive environment for developing code and testing models.

Data Preparation:

Objective: Prepare the data for use in models.
At this stage, the data is cleaned and transformed to be ready for analysis or training. In this project, this may include:
Converting texts into processable formats using techniques such as Tokenization (dividing texts into words).
Image processing using techniques such as shape analysis or pattern recognition.

Modeling:
Goal: Build and train models.
In this stage, algorithms are used to build the AI model. In your project, you can use:
NLP (Natural Language Processing) model to generate the pattern based on the user's description.
Image analysis model (if you are using images) to recognize patterns in crochet.

Tools used:
OpenAI API (GPT-4) or Gemini to generate the pattern based on the description.
TensorFlow or PyTorch if you are using image analysis.

Evaluation:
Goal: Evaluate the model after it has been trained and analyzed.
In this stage, the accuracy of the model in generating the pattern based on the description or image analysis is evaluated.
You can use:
Stitch Accuracy: Compare the predicted stitches with the actual stitches.
Description Similarity: Compare the similarity between the input description and the generated pattern using techniques such as Fuzzy Matching.
Stitch Distribution: Analyze if the stitch distribution is equal or uneven.

Deployment:
Goal: Deploy the model to be usable in a real environment.
At this stage, an interactive interface is developed that allows users to enter text descriptions or upload images.
Tools used:
Flask or Django to create an interactive web interface.
GitHub to manage the code and upload updates.
Heroku or AWS to host the application.

Tools Used in This Project:
Python: The main language for developing models and extracting results.
Libraries used:
re: To process texts and extract stitches from descriptions.
fuzzywuzzy or rapidfuzz: To calculate the similarity between texts (such as description and pattern).
matplotlib and PIL: To analyze images if you are going to use image analysis.
OpenAI API (GPT-4): To generate patterns based on user description.
Jupyter Notebook: An interactive development environment for testing codes and analyzing results.
Flask/Django: To create an interactive web interface that allows users to enter data (text description or images).
GitHub: To manage the code and publish continuous updates.

Work Steps in Detail:

Define the goal of the project:
The goal is to build a tool that generates crochet patterns based on a text description or an image (if we integrate image analysis).
Collect data:
You can collect a set of text descriptions of crochet patterns or images of crochet products. It would be useful to collect a set of different descriptions and train the model to generate various patterns.
Clean and transform data:
For example, clean text descriptions, extract stitches and stitch counts, and ensure that the texts are consistent with a consistent format.
If you are using images, image processing techniques will be applied to identify the different parts of each image.
Build models:
Use GPT-4 to generate patterns based on the description.
Use other techniques if you are analyzing images to extract information from images.
Evaluate the model:
The accuracy of pattern generation is evaluated using two metrics:
Stitch accuracy.
Similarity between description and pattern.
You can also test the stitch distribution in the pattern.
Publish the model:
Develop a web interface using Flask or Django that allows users to enter a text description or upload an image.
Project Summary:

This project aims to build a system for generating crochet patterns using artificial intelligence, so that users can enter text descriptions of crochet products or upload images. Text and image processing techniques are used to generate accurate patterns. The project is based on the CRISP-DM methodology for developing and improving models step by step.
