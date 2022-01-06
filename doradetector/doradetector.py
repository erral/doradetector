# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.eitb.eus/eu/modulo/programacion/programacion_berria_3_col_ajax/canal"

CHANNELS = {
    1: {
        "name": "ETB-1",
        "url": f"{BASE_URL}/1/emisoras/ETB-1/fecha/",
    },
    2: {
        "name": "ETB-2",
        "url": f"{BASE_URL}/2/emisoras/ETB-2/fecha/",
    },
    3: {
        "name": "ETB-3",
        "url": f"{BASE_URL}/3/emisoras/ETB-3/fecha/",
    },
    4: {
        "name": "ETB-4",
        "url": f"{BASE_URL}/6/emisoras/ETBKTDT/fecha/",
    },
    5: {
        "name": "ETB-Basque",
        "url": f"{BASE_URL}/5/emisoras/EITBBASQUE/fecha/",
    },
}


def get_doraemon_appearances(html):
    appearances = []
    soup = BeautifulSoup(html)
    for li in soup.find_all("li", class_="expandible"):
        for a in li.find_all("a"):
            program_title = a.text
            if "doraemon" in program_title.lower():
                hours = li.find_all("p", class_="hora")
                if hours:
                    hour = hours[0].text
                else:
                    hour = ""
                appearances.append(
                    {
                        "title": program_title,
                        "hour": hour,
                    }
                )

    return appearances


def doradetector(date_string):
    appearances = []
    for channel_id, channel_data in CHANNELS.items():
        url = channel_data["url"]
        url = url + date_string
        data = requests.get(url)
        doraemon_appearances = get_doraemon_appearances(data.text)
        for appearance in doraemon_appearances:
            appearance.update(
                {"channel": channel_data["name"], "date": date_string}
            )
            appearances.append(appearance)
    return appearances


if __name__ == "__main__":
    result = doradetector("2022-01-07")
    for res in result:
        print(
            "{channel} {hour} {program_name}".format(
                channel=res["channel"],
                hour=res["hour"],
                program_name=res["title"].strip().replace("\t", ""),
            )
        )
