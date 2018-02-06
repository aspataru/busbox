import unittest
from digit_image_generator import DigitImageGenerator
from PIL import Image


class TestImageGenerator(unittest.TestCase):
    TESTDATA_DIR = 'test-resources/images/'

    def test_should_compose_expected_image(self):
        generator = DigitImageGenerator()
        imageData = generator.generate_4_digit_image([12,23])
        imageData.save(self.TESTDATA_DIR + 'out.bmp')
        expectedImage = Image.open(self.TESTDATA_DIR + 'expected.bmp').convert("RGBA")
        self.assertEqual(list(expectedImage.getdata()), list(imageData.getdata()))

    def test_should_handle_2_digits_or_none(self):
        """TODO"""

if __name__ == '__main__':
    unittest.main()
