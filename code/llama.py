from llama_cpp import Llama
from file_operations import read_config

llm = Llama(model_path="llama.cpp/models/vicuna-7b-1.1.ggmlv3.q4_0.bin")

def generate_response(user_input):
    return llm(user_input, max_tokens= 400, echo=False)["choices"][0]["text"]