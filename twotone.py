# twotone.py

from image import ImagePPM

def luminance(c):
    r, g, b = c
    return 0.2 * r + 0.7 * g + 0.1 * b

def twotone(c, bright, cutoff, dark):
    return bright if luminance(c) > cutoff else dark

def f(c):
    return twotone(c, (255, 255, 255), 110, (0, 30, 70))

def applyfn(f, img):
    width, height = img.size
    for i in range(width):
        for j in range(height):
            img.putpixel((i, j), f(img.getpixel((i, j))))
                
def main():
    img = ImagePPM.open("sup.ppm")
    applyfn(f, img)
    img.save("sup2.ppm")
    
main()
