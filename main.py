import os
import time
from colorama import Fore, Back, Style, init 

init(autoreset=True)

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"{Back.GREEN}{Fore.BLACK}Created Folder: {folder}{Style.RESET_ALL}")
    print()

def move(folderName, files):
   createIfNotExist(folderName)
   file_count=len(files)
   print(f"{Fore.YELLOW}Moving {Style.BRIGHT}{file_count} {Style.NORMAL}Files to {Style.BRIGHT}{folderName}...")
   for i,file in enumerate(files,1):
      os.replace(file, os.path.join(folderName, file))
      print(f"{Fore.WHITE}{Style.BRIGHT}[{i}/{file_count}] {Fore.LIGHTGREEN_EX}{Style.NORMAL}Moved {file} {Style.BRIGHT}==> {Style.NORMAL}{folderName}{Style.RESET_ALL}")
      time.sleep(2)

files=os.listdir()
files.remove("main.py")
print(f'{Fore.CYAN}{Style.BRIGHT}Files in Drectory:\n {Fore.WHITE}{Style.NORMAL}{files}\n')

imgExts=[".png", ".jpg", ".jpeg"]
imgs=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts=[".docx", ".doc", ".pdf", ".txt"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts=[".mp4", ".mp3",".flv"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

appExts=[".exe"]
apps=[file for file in files if os.path.splitext(file)[1].lower() in appExts]

others=[file for file in files if os.path.splitext(file)[1].lower() not in mediaExts + docExts + imgExts + appExts and os.path.isfile(file)]

print(f"{Fore.CYAN}{Style.BRIGHT}Organizing Your Files....")
move('Images', imgs)
move('Docs', docs)
move('Media', medias)
move('Apps' , apps)
move('Other', others)

print(f"{Fore.GREEN}{Style.BRIGHT}\nAll files have been organized successfully!{Style.RESET_ALL}")
