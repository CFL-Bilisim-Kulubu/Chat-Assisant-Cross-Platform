echo off
call %cd%\venv\Scripts\activate.bat
echo .
echo .
echo By pressing any key you accept the licenses of Meta Llama 2 usage license & ChatGPT API usage API
echo Llama-2 License: https://ai.meta.com/llama/license/
echo Terms of Usage OpenAI API https://openai.com/policies/terms-of-use
pause
py %cd%\code\main.py