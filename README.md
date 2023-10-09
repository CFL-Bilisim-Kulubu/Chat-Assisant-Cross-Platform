# Chat-Assisant-Cross-Platform
 A simple LLM UI made with Llama 2 and Whisper

Before using : 
 
Install llama.cpp into project folder if you want to use llama locally 
```
pip install -r requirements.txt
 ```
# About Building Llama.cpp & Clonning Repository

## Linux
 ```
git clone https://github.com/MertKalkanci/Chat-Assisant-Cross-Platform
cd Chat-Assisant-Cross-Platform
git clone https://github.com/ggerganov/llama.cpp  
cd llama.cpp
make 
```

## Windows
You don't need to build on windows you can use prebuilded release from releases

1) Install repository
2) Install Llama.cpp into project folder
3) You can use cmake method 
4) You can use makefile method
5) 
For more information to build on windows please visit [Llama.cpp Github Page](https://github.com/ggerganov/llama.cpp)

# Downloading Llama AI

Download gguf model you want to use [This One Is Reccomended](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/) and move it to `llama.cpp/models` folder

Also you can download reccomended [13B parameters version from here](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/)

Response times tested on Intel Core i5-10200H is varies around 2 minutes to 5 seconds, on 7b model. 

The app sends an notification when response generated so you don't need to wait for response on web browser

Don't forget to configure `` config.json ``

# Configuring

open `` config.json ``

```json
{
  "llm_path": "llama.cpp/models/llama-2-7b-chat.Q2_K.gguf",
  "username": "Mert",
  "whisper_device": "cpu",
  "whisper_model": "medium.en",
}
```
Change your name

Change llm_path relative to project folder

``whisper_device`` can get values of "cpu"  or  "gpu"

``whisper_model`` can get values of "small.en",    "medium.en",   "large"
