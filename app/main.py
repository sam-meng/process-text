"""
API server for demonstrating spaCy text processing.

Date: 2023/2/19
"""


import os
import logging
import datetime
import spacy
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel

# Load .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")
dir_path = os.path.dirname(os.path.realpath(__file__))

# Start the app
app = FastAPI()


@app.on_event("startup")
async def init_model():
    """Initialization."""
    logging.debug(dict(os.environ))


class Text(BaseModel):
    text: str


@app.post("/process_text")
async def process_text(request: Text):
    """Main API endpoint."""

    # Get input text
    text = request.text

    # Parse text using spaCy
    doc = nlp(text)
    results = [{"text": tok.text, "pos": tok.pos_, "dep": tok.dep_} for tok in doc]

    return JSONResponse(content=results)


@app.exception_handler(Exception)
async def handle_error(_, exc):
    """General error handler."""

    time = datetime.datetime.now().timestamp()
    response = JSONResponse(
        content={"status": "error", "message": f"{exc}", "timestamp": time},
    )
    logging.error(response.body)
    return response
