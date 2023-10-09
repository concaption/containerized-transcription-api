"""
sa
"""

from tempfile import NamedTemporaryFile
from typing import List

import torch
import whisper
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = whisper.load_model("base", device=DEVICE)

app = FastAPI()

print("   samda, asda")
