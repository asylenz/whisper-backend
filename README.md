# Image Extractor Backend

This backend is a simple Flask application that provides an API to extract images from PDF, DOCX, and PPTX files.

## Setup

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install Flask Flask-Cors
    ```

    **Note for DOCX/PPTX:** This script uses `unzip`. On macOS and most Linux distributions, this is pre-installed. If you are deploying on a minimal environment, ensure `unzip` is installed.

## Running the Server

To start the Flask development server, run:
```bash
python app.py
```

The server will start on `http://127.0.0.1:5001` by default.

## API Endpoint

### `POST /extract-images`

Upload a file to extract images.

-   **Form Data:**
    -   `file`: The PDF, DOCX, or PPTX file.

-   **Success Response (200):**
    ```json
    {
      "images": [
        "base64-encoded-image-string-1",
        "base64-encoded-image-string-2",
        ...
      ]
    }
    ```

-   **Error Response (400, 500):**
    ```json
    {
      "error": "Error message description"
    }
    ```
