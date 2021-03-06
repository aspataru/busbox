import unittest
from tpg_next_departures import extract_time_tags
from tpg_next_departures import parse_minutes


class TestBusSchedule(unittest.TestCase):
    TESTDATA_DIR = 'test-resources/'

    def test_should_extract_tags(self):
        file = open(self.TESTDATA_DIR + 'data.html', 'r')
        contents = file.read()
        times = extract_time_tags(contents)
        file.close()
        self.assertEquals(len(times), 2)

    def test_should_not_fail_on_nothing_found(self):
        file = open(self.TESTDATA_DIR + 'wrong-data.html', 'r')
        contents = file.read()
        times = extract_time_tags(contents)
        file.close()
        self.assertEquals(len(times), 0)

    def test_should_extract_minutes(self):
        times = ['15\'', '60\'']
        parsed_times = parse_minutes(times)
        expected_times = [15, 60]
        self.assertEquals(expected_times, parsed_times)

    def test_should_not_fail_on_non_digit(self):
        times =['15a','60\'']
        parsed_times = parse_minutes(times)
        expected_times = [60]
        self.assertEquals(expected_times, parsed_times)


if __name__ == '__main__':
    unittest.main()
