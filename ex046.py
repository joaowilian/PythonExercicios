#import emoji
from time import sleep
from emoji import emojize

for c in range(5,0,-1):
    print(c)
    sleep(0.5)

print(emojize('BUM! BUM! POOOW! :sunglasses:',use_aliases=True))