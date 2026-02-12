## Image Panorama Assignment (OpenCV)

This repository contains your solution for the IE Computer Vision assignment: building an image panorama using OpenCV inside a self‑contained Jupyter notebook.

### Goal

- **Create a panorama** from **exactly 3 photos** you captured inside the IE Tower.
- All three images are embedded in the notebook as **base64 strings**, decoded back to OpenCV images, and then stitched into a single panorama.

### Repository structure

- `main.ipynb` – main notebook with all code, embedded images, and visualizations.
- `conversion_script.py` – utility script to convert 3 image files into resized base64 strings and write them into `embedded_images.py`.
- `embedded_images.py` – auto‑generated file containing `IMG_1`, `IMG_2`, `IMG_3` base64 strings.
- `IE_CV_Panorama_Assignment.pdf` – original assignment description.
- `requirements.txt` – Python dependencies for running the notebook.

### Environment setup

1. **Create and activate a virtual environment** (optional but recommended).
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Embedding your images

1. Place your three photos (e.g. `img1.jpg`, `img2.jpg`, `img3.jpg`) in an `images/` folder.
2. Ensure there are **exactly 3 images** in that folder with extensions `.jpg`, `.jpeg`, or `.png`.
3. Run:

   ```bash
   python conversion_script.py
   ```

4. The script will resize the images, encode them as base64, and write them into `embedded_images.py` as `IMG_1`, `IMG_2`, and `IMG_3`.
5. The notebook imports and decodes these strings back to OpenCV images and uses them in the stitching pipeline.

### Running the notebook

1. Run all cells from top to bottom. The notebook will:
   - Decode the base64 image strings into OpenCV `BGR` images.
   - Display the three input images.
   - Run the panorama stitching pipeline using OpenCV.
   - Display the final stitched panorama.

### Notes

- Make sure the three photos have **30–50% overlap** between consecutive shots and are captured by **rotating** the camera (no translation).
- If stitching is slow or unstable, downsampling (already done in `conversion_script.py`) helps robustness and speed.
