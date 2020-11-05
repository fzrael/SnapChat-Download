import requests
import random
import sys

CRED = '\033[91m'
CEND = '\033[0m'
CBLUEBG   = '\33[34'
CGREEN  = '\33[32m'
print  ('''


      _____ _                       _____                 
     / ____| |                     / ____|                
    | (___ | |_ ___  _ __ _   _   | (___   __ ___   _____ 
     \___ \| __/ _ \| '__| | | |   \___ \ / _` \ \ / / _ \ 
     ____) | || (_) | |  | |_| |   ____) | (_| |\ V /  __/
    |_____/ \__\___/|_|   \__, |  |_____/ \__,_| \_/ \___|
                           __/ |                          
                          |___/                           

        ## Programmed By : @81111i And @192.168.00.1 ##






''')

u = input("Username : ")
print("\n")

url = f'https://search.snapchat.com/lookupStory?id={u}'


json = requests.get(url)

if json:
    json = json.json()
else:
    print(CRED +f'{u}', ' ➝ Not Found ✘ ' + CRED)
    sys.exit()
d = json['storyTitle']

snapList = json['snapList']

snapLength = len(snapList)

print('---------------------')

print(f'User: {u}')
print(f'Title : {d}')
print('Count: ',len(snapList))

print('---------------------')


for x in snapList:
    n = random.random()

    print (x['snapUrls']['mediaUrl'])
    if x['snapUrls']['mediaUrl'].endswith(".mp4"):
      tt = format(x['snapUrls']["mediaUrl"])

      requesttry = requests.get(f'{tt}').content
      with open(f'{n}''.mp4','wb') as video:
        video.write(requesttry)

        print(CRED + "تم تنزيل الفيديو 📽 : " + CEND)
        print("\n")
    else:
        tt = format(x['snapUrls']['mediaUrl'])
        requesttry1 = requests.get(f'{tt}').content
        with open(f'{n}''.jpg', 'wb') as image:
            image.write(requesttry1)

        print( CBLUEBG +"تم تنزيل الصورة 📸 : " + CBLUEBG )
        print("\n")
        
if x ['snapIndex']+1 == snapLength:
    print("\n")
    print( CGREEN + "تم تحميل جميع سنابات  ... ( ✔ )" + CGREEN )
