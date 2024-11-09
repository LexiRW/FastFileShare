from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Define folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_file(files: List[UploadFile] = File(...)):
    file_paths = []
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        # Save uploaded file to the uploads folder
        with open(file_path, "wb") as f:
            f.write(await file.read())
        file_paths.append(file_path)
    return {"file_paths": file_paths}

@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/files/")
async def list_files():
    # List all files in the uploads folder
    files = os.listdir(UPLOAD_FOLDER)
    return {"files": files}

# Run the app with `uvicorn main:app --reload` (main is the filename without `.py`)
