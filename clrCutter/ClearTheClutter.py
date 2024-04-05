import os

mainDir = "C:\\Users\\katte\\Documents\\Assets\\Python\\clrCutter\\dummyfiles"
ext = "png"
destDir = "C:\\Users\\katte\\Documents\\Assets\\Python\\clrCutter\\dest" 

def sortfiles(ext, mainDir, destDir):
    files = os.listdir(mainDir)
    print(f"this is the unsorted files: {files}")
    n= 0
    for file in files:
        os.rename(mainDir+ "\\"+ file , destDir + "\\" + str(n) + "." + ext  )
        n= n+1
         

sortfiles(ext, mainDir)


