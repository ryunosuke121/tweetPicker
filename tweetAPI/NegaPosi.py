from asari.api import Sonar
import tweetPicker

sonar = Sonar()
positive = 0
negative = 0
for i in tweetPicker.main(1603525317716475905):
    res = sonar.ping(i)
    negaposi = res['top_class']
    if negaposi == 'positive':
        positive = positive + 1
    else: negative = negative + 1
    print(res['text'])
    print(negaposi)
print(positive,negative)
