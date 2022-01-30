import requests
import json
from sched import scheduler
import time
import threading


def getCollectionStats(url):

    response = requests.request("GET", url)

    mutantanatomy_data = json.loads(response.text)
        
    return mutantanatomy_data

def updateStatsInformation():
    mutantanatomy_data: dict = getCollectionStats(
        "https://api.opensea.io/api/v1/collection/mutantanatomyscienceapeclub")

    anatomy_data: dict = getCollectionStats(
        "https://api.opensea.io/api/v1/collection/anatomyscienceapeclub")

    mutant_floor_price: int = mutantanatomy_data["collection"]["stats"]["floor_price"]

    anatomy_floor_price: int = anatomy_data["collection"]["stats"]["floor_price"]

    return anatomy_floor_price, mutant_floor_price



