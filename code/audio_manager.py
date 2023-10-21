import pprint
import whisper
import wave
import pyaudio
import threading
import time
import os
from file_operations import read_config

model = whisper.load_model(read_config()["whisper_model"],device=read_config()["whisper_device"])

class AudioRecording:
    def __init__(self):
        self.record = threading.Event()
        self.finished_recording = threading.Event()
        print(self.record.is_set())


    def recording(self):
        if self.record.is_set():
            self.stop_recording()
            self.record = threading.Event()
        else:
            self.record.set()
            self.record_thread =  threading.Thread(target=self.record_audio, args=())
            self.record_thread.start()
    
    def stop_recording(self):
        self.record = threading.Event()

        return "saved successfully"
    


    def record_audio(self):
        audio = pyaudio.PyAudio()
        frames = []
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        while (self.record.is_set()):
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        
        path = os.getcwd()
        
        print(f"{path}\\audio.wav")

        audio_writer = wave.open(f"{path}\\audio.wav", "wb")
        audio_writer.setnchannels(1)
        audio_writer.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        audio_writer.setframerate(44100)
        audio_writer.writeframes(b''.join(frames))
        audio_writer.close()
        audio.terminate()
        self.finished_recording.set()
        print("recording finished")

    

    def analyze_audio(self):
        while (not self.finished_recording.is_set()): # wait for recording to finish
            time.sleep(0.2)
        time.sleep(0.2)   
        path = os.getcwd()
        
        return model.transcribe(f"{path}\\audio.wav")["text"]
