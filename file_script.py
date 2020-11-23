import os, shutil, psutil, time
from datetime import date


desktopPath = "C:\\Users\\pedro\\OneDrive\\Desktop\\"
ist2ano2semestrePath = "C:\\Users\\pedro\\OneDrive\\Desktop\\IST\\IST- 2ºAno\\1º Semestre\\"
S0 = "Sistemas Operativos\\"
CD2 = "Cálculo 2\\"
PO = "Programação com Objetos\\"
processName = "Zoom"
os.chdir(desktopPath)
currentSubject = ""
counter = 0

def isZoomRunning():
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def manageFiles(): 
    global counter
    for file in os.listdir(desktopPath):
        if file.startswith("SO"):
            screenShotsPath = ist2ano2semestrePath + SO + "Screenshots\\"
            if not hasTodayFolder(screenShotsPath):
                createTodayFolder(screenShotsPath)
                counter = 0
            counter += 1
            newfile = renameFile(desktopPath, file)
            shutil.move(desktopPath + file, screenShotsPath + getTodayFolder())
            
        elif file.startswith("CD2"):
            print("Found")
            screenShotsPath = ist2ano2semestrePath + CD2 + "Screenshots\\"
            if not hasTodayFolder(screenShotsPath):
                createTodayFolder(screenShotsPath)
                counter = 0
            counter += 1
            newfile = renameFile(desktopPath, file)
            shutil.move(desktopPath + file, screenShotsPath + getTodayFolder())
            
        elif file.startswith("PO"):
            screenShotsPath = ist2ano2semestrePath + PO + "Screenshots\\"
            if not hasTodayFolder(screenShotsPath):
                createTodayFolder(screenShotsPath)
                counter = 0
            counter += 1
            newfile = renameFile(desktopPath, file)
            shutil.move(desktopPath + file, screenShotsPath + getTodayFolder())

def getTodayFolder():
    today = date.today()
    # dd_mm_YY
    today = today.strftime("%d_%m_%Y\\")
    return today


def hasTodayFolder(parentFolderPath):
    return os.path.isdir(parentFolderPath + getTodayFolder())


def createTodayFolder(path):
    os.mkdir(path + getTodayFolder())
    
def renameFile(path, file):
    file.replace(".jpg", "")
    newfile = file + str(counter) + ".jpg"
    os.rename(path + file, path + newfile)
    return newfile
        

while True:
    if isZoomRunning():
        manageFiles()
        print("Running...")
        time.sleep(3)
    else:
        #print("Sleeping...")
        time.sleep(300)