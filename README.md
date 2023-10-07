# Chat-Assisant-Cross-Platform
 A simple chat assisant made with Llama 2 and Whisper

Before using : 
```
pip install -r requirements.txt
huggingface-cli login
 ```
 
 Install llama.cpp into project folder if you want to use llama locally 

## Linux
 ```
git clone https://github.com/ggerganov/llama.cpp  
cd llama.cpp
make 
cd models
wget https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q8_0.gguf 
```
## Windows
To Install Llama.cpp
1) You can use cmake method 
2) You can use makefile method

For more information to build on windows please visit [Llama.cpp Github Page](https://github.com/ggerganov/llama.cpp)

Next download gguf model you want to use [This One Is Reccomended](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q8_0.gguf ) and move it to `llama.cpp/models` folder


Don't forget to configure ``` config.json ```
