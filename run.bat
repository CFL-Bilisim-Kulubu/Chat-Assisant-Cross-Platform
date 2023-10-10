echo off

call %cd%\venv\Scripts\activate.bat

echo By pressing any key you accept the license of the llama version you have downloaded. Be aware of usage license of it. 
echo For more detail follow Llama-2 License page: https://ai.meta.com/llama/license/
pause
py %cd%\code\main.py