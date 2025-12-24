from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from contextlib import asynccontextmanager
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import re
tokenizer = None
model = None

class RequestBody(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True) 
    prompt: str
    max_tokens: int = 16000

@asynccontextmanager
async def lifespan(app: FastAPI):
    global tokenizer, model
    model_path = os.path.join(os.getcwd(), "Unittesting")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path,local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
    yield  
    print("Shutting down...")

app = FastAPI(title="My Safetensor LLM", lifespan=lifespan)


@app.post("/generate")
async def generate(req: RequestBody):
    user_content_string = req
    prompt =f"""
SYSTEM: You are an expert Angular developer.
Generate comprehensive Jest unit tests for the provided Angular code.
Only return ONE describe() function as output.
Do NOT include explanations or any extra text.

USER:
{user_content_string}

ASSISTANT:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
      **inputs,
      max_new_tokens=350,
      temperature=0.7,
      do_sample=True,
      top_p=0.9,)
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    assistant_part = re.split(r"ASSISTANT\s*:\s*", response, flags=re.IGNORECASE)
    if len(assistant_part) > 1:
       response = assistant_part[1].strip()
    else:
       response = response.strip()
    match = re.search(r"(describe\s*\([\s\S]*?\}\s*\);?)", response)
    if match:
        response = match.group(1)
    else:
        response = "describe('No valid output', () => {});"
    fixed = fix_describe_block(response)
    return fixed

def fix_describe_block(text: str) -> str:
    block = text
    open_paren = block.count('(')
    close_paren = block.count(')')
    open_brace = block.count('{')
    close_brace = block.count('}')

    if close_brace < open_brace:
        block += '}' * (open_brace - close_brace)
    if close_paren < open_paren:
        block += ')' * (open_paren - close_paren)

    if not block.strip().endswith(';'):
        block = block.rstrip() + ';'

    return block



@app.get("/test")
async def test():
    return {"text": "test successful."}



