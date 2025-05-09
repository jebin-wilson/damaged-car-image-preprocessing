# Damaged Car Image Preprocessing Pipeline using OpenCV

## Overview
This project focuses on automating the preprocessing of damaged car images using OpenCV. It's designed for use in scenarios such as insurance claims, automotive repair, quality control, and AI-powered damage detection.

## Features
- Resize and crop images to focus on damage
- Convert images between RGB, BGR, and HSV color spaces
- Apply thresholding (binary, adaptive, Otsu's)
- Interactive Streamlit web app
- Exploratory Data Analysis (EDA) on image properties

## Business Use Cases
- Insurance Claims Automation
- Repair Shop Estimate Assistance
- AI-based Damage Detection
- Vehicle Manufacturing Quality Control

## Project Structure
```
damaged-car-image-preprocessing/
├── app/
│   └── streamlit_app.py
├── notebooks/
│   └── preprocessing_pipeline.ipynb
├── data/
│   ├── sample_images/
│   └── preprocessed_images/
├── utils/
│   └── preprocessing.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/damaged-car-image-preprocessing.git
    cd damaged-car-image-preprocessing
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app/streamlit_app.py
    ```

## Deliverables
- Jupyter Notebook for preprocessing pipeline
- Streamlit Web Application
- Sample input/output images
- Documentation and EDA

## License
This project is licensed under the MIT License.
