from transformers import WhisperProcessor, WhisperForConditionalGeneration

# load model and processor

processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")

model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

model.config.forced_decoder_ids = None

def speech_to_text(audio):
    input_features = processor(audio, sampling_rate=16_000, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    return processor.batch_decode(predicted_ids, skip_special_tokens=True)
