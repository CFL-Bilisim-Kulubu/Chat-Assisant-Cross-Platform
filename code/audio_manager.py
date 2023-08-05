import whisper
import wave
import pyaudio
import threading

model = whisper.load_model("small.en")


try:
        audio = pyaudio.PyAudio()
except Exception as e:
    print(e)
    

def analyze_audio():
    return model.transcribe("audio.wav")["text"]


class AudioRecording:

    def __init__(self):
        self.record = False
        self.frames = []
        self.stream = None
        self.audio = None

    def recording(self):
        if self.record:
            self.stop_recording()
            self.record = False
        else:
            self.record = True
            self.record_thread =  threading.Thread(target=self.record_audio, args=(self.record))
            self.record_thread.start()

    def record_audio(record:bool):
        frames = []
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        while (record):
            print("recording")
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        audio = wave.open("audio.wav", "wb")
        audio.setnchannels(1)
        audio.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        audio.setframerate(44100)
        audio.writeframes(b''.join(frames))
        audio.close()
        print("recording finished")

    
    def stop_recording(self):
        self.record = False

        return "saved successfully"
