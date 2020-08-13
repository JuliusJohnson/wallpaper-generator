#s import required classes
import textwrap, requests, bs4, json, random
from PIL import Image, ImageDraw, ImageFont
from unsplash.api import Api #For Help: https://github.com/yakupadakli/python-unsplash
from unsplash.auth import Auth
import pdb #used for debugging

with open('C:/Users/Julius J/Documents/Technical/python/Projects/scrimages/cred.json') as t:
    data = json.load(t)

#Gets unsplash user creds
client_id = data['client_id']
client_secret = data['client_secret']
redirect_uri =""
code = ""


auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
#pdb.set_trace()
pod = str(api.photo.random(count = 1, collections = "923414")) #finds random picture
podID = pod[11:22]
URL = "https://source.unsplash.com/" + podID
print(URL)
with open("C:/Users/Julius J/Documents/Technical/python/Projects/scrimages/my_image.jpg", "wb") as img_handle: #look up code to understand what it does
    img_data = requests.get(URL)
    img_handle.write(img_data.content)

# create Image object with the input image
image = Image.open('C:/Users/Julius J/Documents/Technical/python/Projects/scrimages/my_image.jpg')

#resizes images
width, height = image.size
def resize(precentage):
    rwidth = int(width*(precentage))
    rheight = int(height*(precentage))
    return rwidth,rheight

if width > 1024:
    xfactor = (1024/width)
else:
    xfactor = 1

image2 = image.resize(resize(xfactor), resample=0) #sets new image size to the variable image2

image3 = image2.point(lambda p: p * 0.8) #Darkens the image(higher is lighter0 

# initialise the drawing context with
# the image object as background

draw = ImageDraw.Draw(image3)

# create font object with the font file and specify
# desired size

font = ImageFont.truetype('C:/Windows/Fonts/BELL.TTF', size=30)

# starting position of the message
with open('C:/Users/Julius J/Documents/Technical/python/Projects/scrimages/Crawler/data.json') as f:
    dict = json.load(f)

(wImage, hImage) = (image3.size)
verse = random.choice(list(dict.keys())) # finds a randome key in the dictionary
message = dict[verse]  #stores the key's values in the variable message
msg = textwrap.wrap(message, width=50)
color = 'rgb(255, 255, 255)' # white color

# draw the message(scripture) on the background
current_h, pad = hImage/2, 20
for line in msg:
    (wMsg, hMsg) = draw.textsize(line, font=font)
    draw.text(((wImage-wMsg)/2, current_h), line, fill=color, font=font)
    current_h += hMsg + pad
 
 # draws the source 10 pixels lower than the message
name = verse
print(verse)
wVerse = draw.textsize(verse, font=font)
#print(wVerse[0])
(x, y) = ((wImage-wVerse[0])/2), current_h+10
color = 'rgb(255, 255, 255)' # white color
draw.text((x, y), name, fill=color, font=font)

# save the edited image

image3.save('C:/Users/Julius J/Documents/Technical/python/Projects/scrimages/test2.jpg')


