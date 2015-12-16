# mandelbrot.py

from image import ImagePPM

def lerp(frac, low, high):
    return low + frac * (high - low)

def testpoint(c, maxreps):
    z = 0
    reps = 0
    while abs(z) < 2 and reps < maxreps:
        z = z ** 2 + c
        reps += 1
    frac = reps / maxreps
    return (0, 0, int(lerp(frac, 0, 255)))

def mandelbrot(xint, yint, size, maxreps):
    width, height = size
    img = ImagePPM.new(size)
    for i in range(width):
        for j in range(height):
            a = lerp(i / width, xint[0], xint[1])
            b = lerp(1 - j / height, yint[0], yint[1])
            c = complex(a, b)
            img.putpixel((i, j), testpoint(c, maxreps))
    return img

def main():
    img = mandelbrot((-2, 0.7), (-1.2, 1.2), (900, 800), 50)
    img.save("mbrot.ppm")
    
main()    
