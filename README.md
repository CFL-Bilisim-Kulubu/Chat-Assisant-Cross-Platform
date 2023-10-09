# Chat-Assisant-Cross-Platform
 A simple chat assisant made with Llama 2 and Whisper

Before using : 
 
Install llama.cpp into project folder if you want to use llama locally 
```
pip install -r requirements.txt
 ```
# About Llama.cpp & Downloading Model

## Linux
 ```
git clone https://github.com/ggerganov/llama.cpp  
cd llama.cpp
make 
cd models
wget https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf
```

If you want to use 13B parameters version you can use this one but you can use any gguf formatted llama AI
```
wget https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q2_K.gguf
```
## Windows
To Install Llama.cpp
1) You can use cmake method 
2) You can use makefile method

For more information to build on windows please visit [Llama.cpp Github Page](https://github.com/ggerganov/llama.cpp)

Next download gguf model you want to use [This One Is Reccomended](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf) and move it to `llama.cpp/models` folder

Also you can download reccomended 13B parameters version from here: https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q2_K.gguf

Response times tested on Intel Core i5-10200H is varies around 2 minutes to 5 seconds, the app sends an notification when response generated so you don't need to wait for response on web browser

Don't forget to configure ``` config.json ```
