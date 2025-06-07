# Stop Sign Detection using OpenCV

This project detects red stop signs in images using OpenCV and HSV masking techniques.  
It highlights detected signs with a green rectangle and prints their center coordinates.

## Folder Structure
stop-sign-detection/
├── stop_sign_detection.py
├── stop_sign_dataset/
├── outputs/
└── README.md


## How to Run

1. Install dependencies:

pip install opencv-python numpy

2. Run the code:
python stop_sign_detection.py


3. Results will be saved in the `outputs/` folder.  
Detected stop sign centers will be printed in the terminal.

## Detection Logic

- Uses HSV color masking to isolate red areas  
- Filters by shape (aspect ratio)  
- Excludes orange traffic cones by hue masking  

## Limitations

Some red objects similar to stop signs may still be detected erroneously in some cases

