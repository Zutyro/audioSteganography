from time import sleep
from pydub import AudioSegment
from io import BytesIO
import numpy as np



def encode(cover_file, secret_file):
    print("lsb encoding")
    secret = open(secret_file, 'rb')
    audio = AudioSegment.from_wav(cover_file)
    samples = audio.get_array_of_samples()
    for i,x in enumerate(samples):
        samples[i] += 1
    new_audio = audio._spawn(samples)
    print(new_audio._data)
    # new_audio.export("secret.wav", format="wav")
    bits = map(bin, new_audio.raw_data)
    for x in bits:
        print(x)
    return "success"




def decode(file):
    print("lsb decoding")
    secret = open(file, 'r')
    secret = secret.read()
    bits = bit_text(secret)
    for x in bits:
        for y in x:
            print(y)
    return "success"



def bit_text(text):
    bits = map(bin, bytearray(text, encoding='utf-8'))
    return bits