from PIL import Image


class DigitImageGenerator:

    def __init__(self):
        self.imagecache = []
        for i in range(0, 9):
            self.imagecache.append(Image.open('images/nb/' + str(i) + '.bmp').convert("RGBA"))

    def generate_4_digit_image(self, digitlist):
        imageData = Image.new("RGBA", (11, 11), "black")
        imageData.paste(self.imagecache[digitlist[0]], (0, 0))
        imageData.paste(self.imagecache[digitlist[1]], (6, 0))
        imageData.paste(self.imagecache[digitlist[2]], (0, 6))
        imageData.paste(self.imagecache[digitlist[3]], (6, 6))
        return imageData
