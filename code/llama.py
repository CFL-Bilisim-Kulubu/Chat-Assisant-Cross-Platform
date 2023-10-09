from llama_cpp import Llama
from file_operations import read_config

path = read_config()["llm_path"]
print(path)

llm = Llama(model_path=path)


def generate_response(user_input):
    return llm(user_input, max_tokens= 400, echo=False)["choices"][0]["text"]
