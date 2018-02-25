from PIL import Image


class DigitImageGenerator:
    topleft = (0, 0)
    topright = (6, 0)
    bottomleft = (0, 6)
    bottomright = (6, 6)
    lineimage = None

    def __init__(self):
        self.imagecache = []
        for i in range(0, 10):
            self.imagecache.append(Image.open('images/nb/' + str(i) + '.bmp').convert("RGBA"))
        # load placeholder image
        self.lineimage = Image.open('images/line.bmp').convert("RGBA")

    def convert_multi_numbers_to_digits(self, numbers):
        """only accepts 0-2 one or two-digit numbers"""
        digits = []
        if len(numbers) > 2:
            numbers = numbers[:2]
        for nb in numbers:
            if nb < 10:
                digits.append(0)
                digits.append(nb)
            elif nb >= 99:
                digits.append(9)
                digits.append(9)
            else:
                for d in str(nb):
                    digits.append(int(d))
        return digits

    def generate_4_digit_image(self, numberlist):
        imageData = Image.new("RGBA", (11, 11), "black")
        digitlist = self.convert_multi_numbers_to_digits(numberlist)
        if len(digitlist) % 2 != 0:
            raise ValueError("Expected even number of digits to display", len(digitlist))

        if len(digitlist) == 0:
            imageData.paste(self.lineimage, self.topleft)
            imageData.paste(self.lineimage, self.topright)
            imageData.paste(self.lineimage, self.bottomleft)
            imageData.paste(self.lineimage, self.bottomright)

        if len(digitlist) == 2:
            imageData.paste(self.imagecache[digitlist[0]], self.topleft)
            imageData.paste(self.imagecache[digitlist[1]], self.topright)
            imageData.paste(self.lineimage, self.bottomleft)
            imageData.paste(self.lineimage, self.bottomright)

        if len(digitlist) == 4:
            imageData.paste(self.imagecache[digitlist[0]], self.topleft)
            imageData.paste(self.imagecache[digitlist[1]], self.topright)
            imageData.paste(self.imagecache[digitlist[2]], self.bottomleft)
            imageData.paste(self.imagecache[digitlist[3]], self.bottomright)

        return imageData
