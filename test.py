import easyocr
import requests
from unit import Unit
reader = easyocr.Reader(['en'])
unit = Unit()
result = reader.readtext('names.png')
print(result)
for i in result:
    name = i[1]
    if name[0] == "[":
        try:
            index = name.index("]")
            name = name[index+1:]
        except Exception as e:
            print("Error: " + name)
            print(e)
            continue
    
    try:
        hackScore = unit.getHackScore(name)
        print(name + " " + str(hackScore))
    except Exception as e:
        print("Error: " + name)
        print(e)