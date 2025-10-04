from slugify import slugify
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = Path("media")
UPLOAD_DIR.mkdir(exist_ok=True)

def generate_slug(text: str) -> str:
    return slugify(text)

async def save_upload_file(upload_file: UploadFile, sub_dir: str) -> str:
    if not upload_file or not upload_file.filename:
        return None
    ext = Path(upload_file.filename).suffix
    filename = f"{uuid4().hex}{ext}"
    dir_path = UPLOAD_DIR / sub_dir
    file_path = dir_path / filename

    content = await upload_file.read()
    with file_path.open("wb") as f:
        f.write(content)

        return str(file_path)