"""
by: Strike-XD#0001
server: https://discord.gg/asBVRT4Vt6

this code made for lazy hummands (useless hummans like me)

"""

import os
import shutil

os.system("cls")

print("[*] Please wait you have some big files !")
print("[!] Don't turn off your pc or script before the procces completed !")

def create_folders(dir):
    try:
        os.mkdir(dir+"\\exe")
        os.mkdir(dir+"\\txt")
        os.mkdir(dir+"\\pdf")
        os.mkdir(dir+"\\scripts")
        os.mkdir(dir+"\\images")
        os.mkdir(dir+"\\videos")
        os.mkdir(dir+"\\zip")
        os.mkdir(dir+"\\Big_file")

    except:
        print("**This procces already started**")

def get_desktop():
    usr = os.getlogin()

    desktop_path = f"C:\\Users\\{usr}\\Desktop"
    
    dirs = os.listdir(desktop_path)
    
    create_folders(desktop_path)

    big_f = [".img",".iso"]
    image = [".png", ".jpg", ".jpeg", ".gif"]
    video = [".mp4",".flv",".mkv",".avi"]
    coding = [".py", ".cs", ".js", ".sh", ".bash", ".cpp", ".c", ".lua", ".html", ".css", ".php", ".xml", "jsp"] 
    zip_f = [".7z",".rar",".zip"]

    for i in dirs:
        if i.endswith(".exe"):
            shutil.move(desktop_path+"\\"+i,desktop_path+"\\exe")

        if i.endswith(".txt"):
            shutil.move(desktop_path+"\\"+i,desktop_path+"\\txt")

        if i.endswith(".pdf"):
            shutil.move(desktop_path+"\\"+i,desktop_path+"\\pdf")

        for l in image:
            if i.endswith(l):
                shutil.move(desktop_path+"\\"+i,desktop_path+"\\images")

        for k in video:
            if i.endswith(k):
                shutil.move(desktop_path+"\\"+i,desktop_path+"\\images")

        for d in coding:
            if i.endswith(d):
                shutil.move(desktop_path+"\\"+i,desktop_path+"\\scripts")

        for q in zip_f:
            if i.endswith(q):
                shutil.move(desktop_path+"\\"+i,desktop_path+"\\zip")   

        for x in big_f:
            if i.endswith(x):
                shutil.move(desktop_path+"\\"+i,desktop_path+"\\Big_file")           
get_desktop()

