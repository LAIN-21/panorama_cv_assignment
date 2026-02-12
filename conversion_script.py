import base64
from pathlib import Path
import cv2

def resize_image(img, width=1200):
    h, w = img.shape[:2]
    scale = width / w
    return cv2.resize(img, (width, int(h * scale)))

def file_to_b64_resized(path: Path, width=1200) -> str:
    img = cv2.imread(str(path))
    img_resized = resize_image(img, width)
    _, buffer = cv2.imencode(".jpg", img_resized)
    return base64.b64encode(buffer).decode("utf-8")

image_dir = Path("images")
extensions = {".jpg", ".jpeg", ".png"}

image_paths = sorted(
    [p for p in image_dir.iterdir() if p.suffix.lower() in extensions]
)

if len(image_paths) != 3:
    raise ValueError("Expected exactly 3 images.")

with open("embedded_images.py", "w", encoding="utf-8") as f:
    for i, path in enumerate(image_paths, 1):
        b64_string = file_to_b64_resized(path, width=1200)
        f.write(f"IMG_{i} = '''{b64_string}'''\n\n")

print("Resized and encoded images written to embedded_images.py")