import time
import sys
import timebox_mini
import image_processing
from tpg_next_departures import retrieve_next_departures
from digit_image_generator import DigitImageGenerator
from os import listdir
from os.path import isfile, join, splitext

NB_IMAGES_PATH = 'images/nb/'


def retrieve_image_for_minutes(minutes):
    nb_files = [f for f in listdir(NB_IMAGES_PATH) if isfile(join(NB_IMAGES_PATH, f))]
    nb_files_noext = {splitext(f)[0] for f in nb_files}
    nb_files_noext_int = {int(f) for f in nb_files_noext}
    # min_file_present = min(nb_files_noext)
    max_file_present = int(max(nb_files_noext_int))
    if minutes in nb_files_noext_int:
        return NB_IMAGES_PATH + str(minutes) + '.bmp'
    elif minutes > max_file_present:
        return 'images/max.bmp'
    else:
        return 'images/min.bmp'


def send_image_from_path_to_timebox(timebox, image_path):
    image_bytes = image_processing.load_image_in_timebox_format(image_path)
    timebox.send(image_bytes)

def send_image_to_timebox(timebox, imagedata):
    image_bytes = image_processing.convert_image_in_timebox_format(imagedata)
    timebox.send(image_bytes)


def run(address):
    image_generator = DigitImageGenerator()
    timebox = timebox_mini.TimeboxMini(address)
    timebox.connect()
    i = 0

    while i < 120:
        print('Calling TPG service')
        send_image_from_path_to_timebox(timebox, "images/loading.bmp")
        minutes = retrieve_next_departures()
        img_to_send = ''
        # todo move to tpg_next_departures and test
        if minutes is None or len(minutes) == 0:
            img_to_send = "images/fail.bmp"
        else:
            print('Got', minutes, 'from TPG service')
            minutes_sorted = sorted(minutes)
            print('Next buses in', minutes_sorted, 'minutes')
            # img_to_send = retrieve_image_for_minutes(next_bus_minutes)
            img_to_send = image_generator.generate_4_digit_image(minutes_sorted)

        print('Sending image', img_to_send)
        send_image_to_timebox(timebox, img_to_send)

        i += 1
        time.sleep(5)


if __name__ == '__main__':
    run(sys.argv[1])
