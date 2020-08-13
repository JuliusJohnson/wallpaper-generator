#!/usr/bin/env
import requests, json, shutil, os, textwrap, random, json
from PIL import Image, ImageDraw, ImageFont
#from unsplash.api import Api
#from unsplash.auth import Auth
SOTD = "May the God of hope fill you will al joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit"

def getBingPic():
    #gets image line and 
    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
    image_data = json.loads(response.text)
    ymdid = image_data['images'][0]['startdate']#references location within JSON
    image_url = image_data['images'][0]['url']#references location within JSON
    title = image_data['images'][0]['title']#references location within JSON
    filename = f'{ymdid} - {title}'
    bing_url = f"https://www.bing.com{str(image_url)}"
    return bing_url, filename

def downloadImage(image_url):
    #changes working directory then downloads image
    #os.chdir("/usr/share/backgrounds")#How to locate background folder in a computer
    r = requests.get(image_url[0], stream = True)
    filename_final = f'{image_url[1]}.png'
    if r.status_code == 200:
        r.raw.decode_content = True      
        with open (filename_final,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("Image downloaded")
    else:
        print("Fix yo code")
        
def scaleImage(image):
    width, height = image.size
    if width > 1024:
        scale = (1024/width)
    else: scale = 1
    imageScaled = image.resize(resize(xfactor), resample=0) #sets new image size to the variable image2 
    return imageScaled

def darkenImage(image):
    image.point(lambda p: p * 0.8) #Darkens the image(higher the value the lighter the image)
    
def drawText(photo):
    picture = Image.open("20200808 - It's ∞ Day!.png")
    draw = ImageDraw.Draw(picture) #initialise the drawing context with; the image object as background
    font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-L.ttf', size=40)#create font object with the font file and specify
    (wImage, hImage) = (picture.size) #returns the dimensions of the given picture
    
    message = "May the God of hope fill you will all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit"  #Displays desired quotations/scripture/text
    msg = textwrap.wrap(message, width=50) #width dermines the margins 
    color = 'rgb(255, 255, 255)' # sets color to white

    current_h, pad = hImage/2, 25 #(Gets Image Height,leading)
    for line in msg: #draw the message(scripture) on the background
        (wMsg, hMsg) = draw.textsize(line, font=font)
        draw.text(((wImage-wMsg)/2, current_h), line, fill=color, font=font)
        current_h += hMsg + pad

    picture.save('test.png') #saves the image


def main():
    image = Image.open("20200808 - It's ∞ Day!.png")
    dark = darkenImage(image)
    drawImage(dark)

if __name__ == "__main__":
    pass
    #main()   
#TODO:
#Create Unsplash connection
#Integrate Darken and Text Draw functions
#Create Text Draw Position
#Create Logic for Automation
#Scape Bibleverse and quotations