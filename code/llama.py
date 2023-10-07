from llama_cpp import Llama
from file_operations import read_config

llm = Llama(model_path="llama.cpp/models/llama-2-7b-chat.Q2_K.gguf")

def generate_response(user_input):
    return llm(user_input, max_tokens= 400, echo=False)["choices"][0]["text"]