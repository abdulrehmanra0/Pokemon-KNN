# PokeKNN: Pokémon Image Recognition with KNN

PokeKNN is a web app that predicts the name of a Pokémon from an uploaded image using K-Nearest Neighbors (KNN). Built with Python, Flask, OpenCV, and Pandas.

## Features
- Upload an image of a Pokémon.
- Get the predicted name of the Pokémon.
- Display the uploaded image and prediction result.

## Technologies Used
- **Python**
- **Flask**
- **OpenCV**
- **Numpy**
- **Pandas**

## Getting Started

### Prerequisites
Ensure you have Python 3.x and the following packages:
- Flask
- OpenCV
- Numpy
- Pandas

### Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/pokeknn.git
   cd pokeknn

### Create a virtual environment and activate it:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install the required packages:

pip install -r requirements.txt

### Download the dataset:
The dataset is not included in this repository due to its size. You can download it from this link.
https://drive.google.com/file/d/1DdPveV7mmDeVINTyhkQ_pKHZDDTkw0Po/view?usp=sharing

### bUnzip the dataset:
After downloading, unzip the dataset. Place the training images in the Train/Images directory and the test images in the Test/Images directory.

### Running the App
Start the Flask app:


Copy code
python app.py
Navigate to:

http://127.0.0.1:5000/

