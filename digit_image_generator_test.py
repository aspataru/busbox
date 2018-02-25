import unittest
from digit_image_generator import DigitImageGenerator
from PIL import Image


class TestImageGenerator(unittest.TestCase):
    TESTDATA_DIR = 'test-resources/images/'

    def test_should_compose_expected_image(self):
        generator = DigitImageGenerator()
        imageData = generator.generate_4_digit_image([12,29])
        imageData.save(self.TESTDATA_DIR + 'out.bmp')
        expectedImage = Image.open(self.TESTDATA_DIR + 'expected.bmp').convert("RGBA")
        self.assertEqual(list(expectedImage.getdata()), list(imageData.getdata()))

    def test_should_convert_to_digits(self):
        generator = DigitImageGenerator()
        numbers = [1,33,55]
        digit_list = generator.convert_multi_numbers_to_digits(numbers)
        self.assertEqual((list(digit_list)), [0,1,3,3])
        numbers = [105]
        digit_list = generator.convert_multi_numbers_to_digits(numbers)
        self.assertEqual((list(digit_list)), [9,9])


if __name__ == '__main__':
    unittest.main()
