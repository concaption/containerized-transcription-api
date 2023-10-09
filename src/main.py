"""
FastAPI server for transcribing audio files to text using whisper library by OpenAI
"""

from tempfile import NamedTemporaryFile
from typing import List

import torch
import whisper
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = whisper.load_model("base", device=DEVICE)  # pylint: disable=invalid-name

app = FastAPI()


@app.post("/whisper")
async def handler(files: List[UploadFile] = File(...)):
    """
    Handler for transcribing audio files to text
    """
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")

    results = []
    for file in files:
        with NamedTemporaryFile(delete=True) as temp:
            with open(temp.name, "wb") as temp_file:
                temp_file.write(file.file.read())
            result = model.transcribe(temp.name)
            result_json = {
                "filename": file.filename,
                "result": result["text"],
            }
            results.append(result_json)
    return JSONResponse(content={"results": results})


@app.get("/", response_class=RedirectResponse)
async def redirect():
    """
    Redirect to docs
    """
    return "/docs"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
