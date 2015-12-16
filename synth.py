# synth.py

import wave
import contextlib
import array
from math import sin, pi

def clamp(x, a, b):
    return max(a, min(b, x))
               
def clampsample(value, typecode):
    a, b = (0, 255) if typecode == "B" else (-32768, 32767)
    return clamp(int(value), a, b)

def sinenote(step, sec, sampfreq):
    data = array.array("h")
    samples = int(sampfreq * sec)
    freq = 440 * 2 ** (step / 12)
    for i in range(samples):
        y = 32767 * sin(2.0 * pi * freq * i / sampfreq)
        data.append(clampsample(y, "h"))
    return data

def notes(notefn, steps, sec, sampfreq):
    data = array.array("h")
    for step in steps:
        data += notefn(step, sec, sampfreq)
    return data
    
def writewav(fname, data, params):
    with contextlib.closing(wave.open(fname, "w")) as f:
        f.setparams(params)
        f.writeframes(data.tostring())
    print(fname, "written.")
    
def main():
    sampfreq = 11025
    pisteps = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    data = notes(sinenote, pisteps, 0.4, sampfreq)
    params = [1, 2, sampfreq, len(data), "NONE", None]
    writewav("synth.wav", data , params)
    
main()
