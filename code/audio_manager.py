import whisper
import wave
import pyaudio
import threading
import time

model = whisper.load_model("medium.en",device="cpu")

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
        audio_writer = wave.open("audio.wav", "wb")
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
        return model.transcribe("audio.wav")["text"]
