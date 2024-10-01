# main.py
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from fastapi.middleware.cors import CORSMiddleware

# Define request body structure
class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 100

# Initialize FastAPI app
app = FastAPI(
    title="Text Generation API",
    description="API for generating text using a pre-trained LLM.",
    version="1.0.0"
)

# Allow CORS (will configure in the next step)
origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add your frontend URL here when deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and tokenizer at startup
@app.on_event("startup")
def load_model():
    global tokenizer, model
    model_name = 'distilgpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    model.eval()  # Set model to evaluation mode

@app.post("/generate")
def generate_text(request: TextGenerationRequest):
    prompt = request.prompt
    max_length = request.max_length

    try:
        inputs = tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                early_stopping=True
            )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"generated_text": generated_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))