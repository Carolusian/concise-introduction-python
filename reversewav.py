# reversewav.py

import array
import contextlib
import wave

def datatype(width):
    return "B" if width == 1 else "h"

def readwav(fname):
    with contextlib.closing(wave.open(fname)) as f:
        params = f.getparams()
        frames = f.readframes(params[3])
    return array.array(datatype(params[1]), frames), params

def writewav(fname, data, params):
    with contextlib.closing(wave.open(fname, "w")) as f:
        f.setparams(params)
        f.writeframes(data.tostring())
    print(fname, "written.")
    
def main():
    fname = input("Enter the name of a .wav file: ")
    data, params = readwav(fname)
    outfname = "rev" + fname
    writewav(outfname, data[::-1], params)

main()
