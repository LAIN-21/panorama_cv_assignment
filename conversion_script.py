import base64
from pathlib import Path

def file_to_b64(path: str) -> str:
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode("utf-8")

paths = ["img1.jpg", "img2.jpg", "img3.jpg"]  # change to your filenames
b64_strings = [file_to_b64(p) for p in paths]

for i, s in enumerate(b64_strings, 1):
    print(f"IMG_{i} = '''{s}'''\n")