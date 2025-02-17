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
