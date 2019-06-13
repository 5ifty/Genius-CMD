import requests
import json
import asyncio
import sys


class genius():
    def __init__(self):

        print("welcoмe тo тнe cυѕтoм genιυѕ cмd тool мade вy 5ιғтy!")
        print('pleaѕe тype ιn yoυr ѕearcн reqυeѕт:')
        x = input()
        url = f"https://some-random-api.ml/lyrics?title={x}"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        title = parsed["title"]

        song = parsed["lyrics"]
        artist = parsed["author"]

        print(f'\n \n Your search result best matched this title "{title}". \n This songs artist is {artist} \n \n \n \n \n \n \n ')
        print(song.replace('\\n', '\n'))
        print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
        input()


# this does the loop. Dont fucking forget it, you fat fuck (aimed at myself, not you github users. I love you<3)

if __name__ == '__main__':
    genius()
