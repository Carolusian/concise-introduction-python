# image.py

def clamp(x, a, b):
    return int(max(a, min(b, x)))              

class ImagePPM:
    @classmethod
    def new(cls, size):
        newimg = ImagePPM()
        newimg.size = size
        newimg.maxval = 255
        newimg.data = [0] * 3 * size[0] * size[1]
        return newimg

    @classmethod
    def open(cls, fname):
        newimg = ImagePPM()
        with open(fname) as f:
            header = f.readline()
            if not header.startswith("P3"):
                return None
            nextline = f.readline()
            while nextline.startswith("#"):
                nextline = f.readline()
            newimg.size = tuple(map(int, nextline.split()))
            newimg.maxval = int(f.readline())
            newimg.data = list(map(int, f.read().split()))
        return newimg
        
    def index(self, coords):
        i, j = coords
        return 3 * (j * self.size[0] + i)
    
    def getpixel(self, coords):
        k = self.index(coords)
        return tuple(self.data[k:k + 3])
    
    def putpixel(self, coords, color):
        k = self.index(coords)
        for i in range(3):
            self.data[k + i] = clamp(color[i], 0, 255)
        
    def save(self, fname):
        width, height = self.size
        with open(fname, "w") as f:
            f.write("P3\n")
            f.write(str(width) + " " + str(height) + "\n")
            f.write(str(self.maxval) + "\n")
            for i in range(3 * width * height):
                f.write(str(self.data[i]) + "\n")
        
