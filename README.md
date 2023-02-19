# Text Processing API Using spaCy

## spaCy Language Model

This project is currently for demonstration purposes, so the `en_core_web_sm` small language model is being used for quick setup. For production, consider using the large language model `en_core_web_lg` for better accuracy.

## Local Server

To set up the API server locally, enter the following command

```bash
pip install -r requirements.txt
uvicorn --host 0.0.0.0 --port 8000 app.main:app --reload
```

## Docker

Enter the following command to build an image and set up the API server

```bash
docker-compose up --build
```

Note that `--build` can be omitted if the image has already been built.

## Example Python Script for Firing Requests

An example script is provided for sending a sample request to the API server. After running the API server (either locally or via Docker), enter the following command to get an example response

```bash
python tests/sample_request.py
```

## API Doc

After running the API server (either locally or via Docker), visit `http://0.0.0.0:8000/docs` to see the auto-generated API documentation and try them out.

Sample input:

```json
{"text": "This is a sample text"}
```

Response:

```json
[
    {"text": "This", "pos": "PRON", "dep": "nsubj"},
    {"text": "is", "pos": "AUX", "dep": "ROOT"},
    {"text": "a", "pos": "DET", "dep": "det"},
    {"text": "sample", "pos": "NOUN", "dep": "compound"},
    {"text": "text", "pos": "NOUN", "dep": "attr"}
]
```


---
Last updated: 2023/2/19
