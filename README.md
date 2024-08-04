# Picheat

Picheat is a web application built with Flask and TensorFlow that compares two images to determine which one is "hotter" based on a MobileNetV2 model trained on the ImageNet dataset. The application provides a simple interface for uploading and comparing images, and it displays the results directly on the web page.

## Features

- **Image Upload**: Upload two images for comparison.
- **Image Analysis**: Uses MobileNetV2 to analyze and score images.
- **Result Display**: Shows which image is "hotter" based on the scores.

## Project Structure
```
picheat/
├── app.py
├── static/
│ └── uploads/
├── templates/
│ └── index.html
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Astro-Saurav/PicHeat
   cd picheat
   ```

2. Create and activate a virtual environment (optional but recommended):
  ```
 python -m venv venv
source venv/bin/activate
# On Windows use 
venv\Scripts\activate
```

3. Install the required packages: `pip install -r requirements.txt`
4. Ensure you have TensorFlow and Pillow installed:`pip install tensorflow pillow`
5. Run the Flask app: `python app.py`

Open your browser and go to `http://127.0.0.1:5000/` to use the Picheat web application.

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your browser.
2. Upload two images using the form provided.
3. Click "Compare" to analyze the images.
4. The application will display which image is "hotter" based on the MobileNetV2 model's predictions.


## Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request. Any improvements and suggestions are appreciated.


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Astro-Saurav/PicHeat/blob/main/LICENSE) file for details.

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/) for the MobileNetV2 model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Pillow](https://pillow.readthedocs.io/) for image processing.

## Contact

If you have any questions, feel free to reach out via GitHub issues or contact me directly on [email](mailto:0501saurav@gmail.com).

---

Happy coding!
