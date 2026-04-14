from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from settings import settings
from huggingface_hub import login

# HF login (optional but ok)
login(token=settings.hf_token)
#print(whoami())

MODEL_ID = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float32
).to("cpu")