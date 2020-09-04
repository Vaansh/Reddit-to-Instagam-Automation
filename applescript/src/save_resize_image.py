import urllib
from PIL import Image

def saveImage(url, filePath, fileName, currenpost):
    fullPath = filePath + fileName + '.png'
    urllib.request.urlretrieve(url, fullPath)

#Pastes image onto a white square and resizes depending on the initial size
def correctShape(fullPath, fileName, filePath, currenpost):
    img = Image.open(fullPath)    
    imgWidth, imgHeight = img.size        
    
    #two different file paths of images, to save time and size, 2400x2400 is the smaller size in this case
    if imgWidth<2400 and imgHeight<2400:
        background = ''
    else:
        background = ''
    
    bg = Image.open(background)
    
    bgWidth, bgHeight = bg.size
    imgCopy = bg.copy()
            
    width = round(bgWidth/2-imgWidth/2)
    height = round(bgHeight/2-imgHeight/2)                                

    left = round(bgWidth/2-imgHeight/2)
    right = round(bgWidth/2+imgHeight/2)
    
    upper = round(bgHeight/2-imgWidth/2)
    lower = round(bgHeight/2+imgWidth/2)
    print(width, height)
    
    imgCopyPath = filePath + fileName + str(currenpost) + '.png'

    #Algorithm to decide and reshape into a square; check in resize image examples folder
    if imgWidth>imgHeight:
        imgCopy.paste(img, (0, height))
        imgCopy.save(imgCopyPath)
        original = Image.open(imgCopyPath)                    
        finalImg = original.crop((0, upper, imgWidth, lower))
    elif imgHeight>imgWidth:     
        imgCopy.paste(img, (width, 0))   
        imgCopy.save(imgCopyPath)                                         
        original = Image.open(imgCopyPath)                    
        finalImg = original.crop((left, 0, right, imgHeight))                                                                                                   
    else:
        finalImg = Image.open(fullPath) 

    #Convert to .jpg image
    finalImgjpg = finalImg.convert('RGB')    
    imgFinalPath = filePath + fileName + str(currenpost) + 'final.jpg'                                                                
    finalImgjpg.save(imgFinalPath)   