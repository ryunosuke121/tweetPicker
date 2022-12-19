import requests
import tweetPicker
import matplotbar

key = 'AIzaSyB4iZ8c6vX_tsoZEGo8StNnEqcwBsXpm6A'
url = f'https://language.googleapis.com/v1beta2/documents:analyzeSentiment?key={key}'
header = {'Content-Type': 'application/json'}

positive = 0
negative = 0
scores = []
for i in tweetPicker.main(1603012154504118273):
    text = i
    body = {
        "document":{
            "type":"PLAIN_TEXT",
            "language": "JA",
            "content":text
        },
        "encodingType":"UTF8"
    }
    res = requests.post(url, headers=header, json=body)
    score = res.json()['documentSentiment']
    scores.append(score)

    print(text)
    print(score)
matplotbar.negaPosiBar(scores)


#body = res.json()
#print(body)

