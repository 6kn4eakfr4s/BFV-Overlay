import easyocr
import requests

class Unit:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        self.url = "https://bfvhackers.com/api/v1/is-hacker?stats=false"
    
    def getName(self, image):
        result = self.reader.readtext(image)
        return result[0][1]
    
    def getRawResponse(self, name):
        results = requests.get(self.url, params={"name": name})
        return results.json()

    def getHackScore(self, name):
        result = self.getRawResponse(name)
        # print(result)
        hackScore = result["hack_score"]
        return hackScore