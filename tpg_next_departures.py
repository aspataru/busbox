import requests
from bs4 import BeautifulSoup

TPG_VRDO_URL = 'https://m.tpg.ch/stopDisplay.htm?mnemo=VRDO'


def extract_time_tags(content):
    soup = BeautifulSoup(content, 'html.parser')
    tags = soup.find_all("span", {"class": "timeText"})
    time_strings = [tag.text for tag in tags]
    return time_strings


def parse_minutes(the_list):
    minutes = []
    for elem in the_list:
        elem_str = str(elem)
        # todo ~ should be handled differently
        if elem_str != '':
            minutes.append(int(elem_str.replace('\'', '').replace('~', '')))
    return minutes


def retrieve_next_departures(page_url):
    r = requests.get(page_url)
    time_tags = extract_time_tags(r.content)
    return parse_minutes(time_tags)


if __name__ == '__main__':
    print(retrieve_next_departures(TPG_VRDO_URL))
