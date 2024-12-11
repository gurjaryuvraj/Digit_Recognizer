# Digit_Recognizer

## Overview
This project is a real-time digit recognition system built using a Convolutional Neural Network (CNN) for multiclass classification. The application is hosted on a Streamlit-based web interface, allowing users to draw digits live on the webpage, which the trained model then identifies.

## Features
- **Live Digit Input:** Users can draw digits on the webpage.
- **Real-Time Predictions:** The model predicts the drawn digit instantly.
- **Interactive UI:** A user-friendly interface powered by Streamlit.

## Technology Stack
- **Machine Learning Framework:** TensorFlow/Keras
- **Web Framework:** Streamlit
- **Languages:** Python
- **Visualization:** Matplotlib

## How It Works
1. **Dataset:** The model was trained on the MNIST dataset, a widely used benchmark for digit recognition.
2. **Model Architecture:** The CNN is designed with convolutional, pooling, and dense layers to effectively capture and classify handwritten digits.
3. **Deployment:** The trained model is deployed on a Streamlit web application for real-time interaction.

## Setup Instructions
To run this project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/gurjaryuvraj/Digit_Recognizer.git

2. **Install Dependencies:**
Ensure you have Python and pip installed, then run:

   ```bash
    pip install -r requirements.txt
3. **Run the Application:**
Execute the following command in the terminal:

   ```bash
    streamlit run main.py
4. **Access the Application:**
Once the server starts, you will see a URL in the terminal (e.g., `http://localhost:8501`). Open this URL in a web browser to use the application.
### Web Application

- **Access the live web application here:** [DigitRecognizeByYuvraj](digitrecognizerbyyuvraj.streamlit.app)

## Project Structure
- **`main.py`:** The main Streamlit application script.
- **`model/`:** Contains the trained CNN model and any preprocessing scripts.
- **`requirements.txt`:** List of dependencies.

## Future Enhancements
- Support for additional datasets or multilingual digit recognition.
- Model improvements for better accuracy and performance.
- Deployment on cloud platforms for greater scalability.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue to discuss ideas or report bugs.


## Acknowledgments
The MNIST dataset.
TensorFlow/Keras and Streamlit for enabling the development of this project.
## Contact
If you have any questions or feedback, feel free to reach out!
