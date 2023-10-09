"""
sa
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi.responses import JSONResponse, RedirectResponse
import whisper
import torch
from tempfile import NamedTemporaryFile


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


app = FastAPI()
