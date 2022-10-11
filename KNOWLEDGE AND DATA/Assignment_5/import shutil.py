import numpy as np
import soundfile as sf
from importlib_resources import path
from cltl.asr.speechbrain_asr import SpeechbrainASR

asr = SpeechbrainASR("speechbrain/asr-transformer-transformerlm-librispeech")

with path("resources", "test.wav") as wav:
    speech_array, sampling_rate = sf.read(wav, dtype=np.int16)
transcript = asr.speech_to_text(speech_array, sampling_rate)