import os

def sortfiles(ext, mainDir):
    files = os.listdir(mainDir)
    print(f"this is the unsorted files: {files}")
    count = 0
    for file in files:
        if((file.split(".")[1]) == ext): 
            os.rename(mainDir+ "\\"+ file , mainDir + "\\" + str(count) + "." + ext  )
            count = count + 1



mainDir = "C:\\Users\\katte\\Documents\\Assets\\Python\\clrCutter\\dummyfiles"
files = os.listdir(mainDir)
fileTypes = set()
for file in files:
    fileTypes.add(file.split(".")[1])
print(fileTypes)

ext = input("Enter the file type to be sorted")

if(ext in fileTypes):
    sortfiles(ext,mainDir)
else:
    print("This type of File is not availabe in this Directory")
    
