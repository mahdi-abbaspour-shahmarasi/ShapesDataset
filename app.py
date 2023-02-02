from random import random
import sys
import os
from  modules import createCircleImage, createSquareImage, createRectangleImage,createTrangleleImage,createPolygonImage
from tqdm import tqdm
import random

#Clear thescreen
os.system('cls' if os.name=='nt' else 'clear')

#Get passed arguments, name of program file, count of classes, count of samples,color type of samples, dimentions of samples
#python app.py 2 500 binary 100*100  
arguments=sys.argv

#Check intered argumentcount
if len(arguments)<5 or len(arguments)>5:
    print("Count of interedarguments is not valid")
    print("Send only 4 argument{CountOfClasses, SampleCount, SamplesColorType, Dimentions}")
    print("ex: python app.py 2 500 binary 100*100")
    exit()

#Parsearguments 
dataSetFolderName= 'dataset'
countOfClass=int(arguments[1])
countOfSamples=int(arguments[2])
samplesColorType=arguments[3]
[samplesWidth, samplesHeight]=[int(arguments[4].split('*')[0]),int(arguments[4].split('*')[1])]

#Listof shapes
samplesType=['Circle','Square','Rectangle','Triangle','Polygon','Oval','Diamond','Parallelogram','Trapezoid','Pentagon','Hezagon']

if not os.path.exists(dataSetFolderName):
    os.makedirs(dataSetFolderName)
else:
    os.system('RMDIR '+dataSetFolderName+' /S /Q' if os.name=='nt' else "rm -rf "+dataSetFolderName)


countOfClassCounter = 0
while True:
    if countOfClassCounter >= countOfClass:
        break
    #create cirules
    if not os.path.exists(dataSetFolderName+"/Circule"):
        os.makedirs(dataSetFolderName+"/Circule")
    for i in tqdm(range(countOfSamples)):
        fileName=dataSetFolderName+"/Circule/"+str(i+1)+".png"
        r=random.randint(10,int(samplesWidth/2))
        x=random.randint(0, samplesWidth-2*r)
        y=random.randint(0, samplesHeight-2*r)
        createCircleImage(fileName, samplesWidth, samplesHeight, x, y, r)

    countOfClassCounter+=1
    if countOfClassCounter >= countOfClass:
        break

    #create square
    if not os.path.exists(dataSetFolderName+"/Square"):
        os.makedirs(dataSetFolderName+"/Square")
    for i in tqdm(range(countOfSamples)):
        fileName=dataSetFolderName+"/Square/"+str(i+1)+".png"
        r=random.randint(10,int(samplesWidth/2))
        x=random.randint(0, samplesWidth-2*r)
        y=random.randint(0, samplesHeight-2*r)
        createSquareImage(fileName, samplesWidth, samplesHeight, x, y, r)

    countOfClassCounter+=1
    if countOfClassCounter >= countOfClass:
        break
    
    #create rectangle
    if not os.path.exists(dataSetFolderName+"/Rectangle"):
        os.makedirs(dataSetFolderName+"/Rectangle")
    for i in tqdm(range(countOfSamples)):
        fileName=dataSetFolderName+"/Rectangle/"+str(i+1)+".png"
        w=random.randint(10,int(samplesWidth/2))
        h=random.randint(10,int(samplesWidth/2))
        x=random.randint(0, samplesWidth-2*r)
        y=random.randint(0, samplesHeight-2*r)
        createRectangleImage(fileName, samplesWidth, samplesHeight, x, y, w,h)
    
    countOfClassCounter+=1
    if countOfClassCounter >= countOfClass:
        break
    
    #create Triangle
    if not os.path.exists(dataSetFolderName+"/Triangle"):
        os.makedirs(dataSetFolderName+"/Triangle")
    for i in tqdm(range(countOfSamples)):
        fileName=dataSetFolderName+"/Triangle/"+str(i+1)+".png"
        
        x1=random.randint(0,int(samplesWidth))
        y1=random.randint(0,int(samplesHeight))
        
        x2=random.randint(1,int(samplesWidth))
        y2=random.randint(1,int(samplesHeight))

        x3=random.randint(2,int(samplesWidth))
        y3=random.randint(2,int(samplesHeight))
        createTrangleleImage(fileName, samplesWidth,samplesHeight, x1,y1,x2,y2,x3,y3)

    countOfClassCounter+=1
    if countOfClassCounter >= countOfClass:
        break
    
    #create Polygon
    if not os.path.exists(dataSetFolderName+"/Polygon"):
        os.makedirs(dataSetFolderName+"/Polygon")
    for i in tqdm(range(countOfSamples)):
        fileName=dataSetFolderName+"/Polygon/"+str(i+1)+".png"
        
        x1=random.randint(0,int(samplesWidth))
        y1=random.randint(0,int(samplesHeight))
        
        x2=random.randint(1,int(samplesWidth))
        y2=random.randint(1,int(samplesHeight))

        x3=random.randint(2,int(samplesWidth))
        y3=random.randint(2,int(samplesHeight))

        x4=random.randint(2,int(samplesWidth))
        y4=random.randint(2,int(samplesHeight))

        x5=random.randint(2,int(samplesWidth))
        y5=random.randint(2,int(samplesHeight))
        createPolygonImage(fileName, samplesWidth,samplesHeight, x1,y1,x2,y2,x3,y3,x4,y5,x5,y5)
