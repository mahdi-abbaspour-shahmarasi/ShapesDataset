from PIL import Image, ImageDraw

def createCircleImage(fileName,width, heigh, x, y,r):
    im = Image.new('RGB', (width, heigh), (0,0,0))
    draw = ImageDraw.Draw(im)
    draw.ellipse((x, y, x+r, y+r),  outline ='white', fill='white')
    im.save(fileName, quality=95)

def createSquareImage(fileName,width, heigh, x, y, w):
    im = Image.new('RGB', (width, heigh), (0,0,0))
    draw = ImageDraw.Draw(im)
    draw.rectangle((x, y, x+w, y+w),  outline ='white', fill='white')
    im.save(fileName, quality=95)

def createRectangleImage(fileName,width, heigh, x, y, w,h):
    im = Image.new('RGB', (width, heigh), (0,0,0))
    draw = ImageDraw.Draw(im)
    draw.rectangle((x, y, x+w, y+h),  outline ='white', fill='white')
    im.save(fileName, quality=95)

def createTrangleleImage(fileName,width, heigh, x1, y1, x2,y2,x3,y3):
    im = Image.new('RGB', (width, heigh), (0,0,0))
    draw = ImageDraw.Draw(im)
    draw.polygon([(x1, y1), (x2, y2),(x3,y3)],  outline ='white', fill='white')
    im.save(fileName, quality=95)

def createPolygonImage(fileName,width, heigh, x1, y1, x2,y2,x3,y3,x4,y4,x5,y5):
    im = Image.new('RGB', (width, heigh), (0,0,0))
    draw = ImageDraw.Draw(im)
    draw.polygon([(x1, y1), (x2, y2),(x3,y3),(x4,y4),(x5,y5)],  outline ='white', fill='white')
    im.save(fileName, quality=95)