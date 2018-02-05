import unittest
from digit_image_generator import DigitImageGenerator
from PIL import Image

class TestImageGenerator(unittest.TestCase):
    """TODO"""
    TESTDATA_DIR = 'test-resources/images/'

    def test_should_compose_expected_image(self):
        generator = DigitImageGenerator()
        imageData = generator.generate_4_digit_image([1,2,3,4])
        #imageData.save(self.TESTDATA_DIR + 'out.bmp')
        expectedImage = Image.open(self.TESTDATA_DIR + 'expected.bmp').convert("RGBA")
        self.assertEqual(list(expectedImage.getdata()), list(imageData.getdata()))


if __name__ == '__main__':
    unittest.main()
