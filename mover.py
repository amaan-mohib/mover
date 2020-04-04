import os
import time
from watchdog.observers import Observer #install watchdog
from watchdog.events import FileSystemEventHandler

path=r'C:\Users\[USER NAME]\Downloads'

def application():  
    files=os.listdir(path)
    for file in files:
        name,ext=os.path.splitext(file)
        ext=ext[1:]
        
        if ext=='':
            continue
        if ext in ['exe','msi','dll','EXE','MSI','DLL']:
            if os.path.exists(path+'/'+'Setups'):
                os.rename(path+'/'+file,path+'/'+'Setups/'+file)
                
            else:
                os.makedirs(path+'/'+'Setups')
                os.rename(path+'/'+file,path+'/'+'Setups/'+file)
        
        if ext in ['jpg','png','gif','webp','PNG','jpeg','JPG','JPEG','GIF','ico','ICO']:
            if os.path.exists(path+'/'+'Images'):
                os.rename(path+'/'+file,path+'/'+'Images/'+file)
                
            else:
                os.makedirs(path+'/'+'Images')
                os.rename(path+'/'+file,path+'/'+'Images/'+file)

        if ext in ['zip','rar','7z','ZIP','RAR']:
            if os.path.exists(path+'/'+'Compressed Files'):
                os.rename(path+'/'+file,path+'/'+'Compressed Files/'+file)
                
            else:
                os.makedirs(path+'/'+'Compressed Files')
                os.rename(path+'/'+file,path+'/'+'Compressed Files/'+file)
        
        if ext == 'pdf':
            if os.path.exists(path+'/'+'PDFs'):
                os.rename(path+'/'+file,path+'/'+'PDFs/'+file)
                
            else:
                os.makedirs(path+'/'+'PDFs')
                os.rename(path+'/'+file,path+'/'+'PDFs/'+file)

        if ext == 'dft':
            if os.path.exists(path+'/'+'CAED'):
                os.rename(path+'/'+file,path+'/'+'CAED/'+file)
                
            else:
                os.makedirs(path+'/'+'CAED')
                os.rename(path+'/'+file,path+'/'+'CAED/'+file)

        if ext == 'torrent':
            if os.path.exists(path+'/'+'Torrents'):
                os.rename(path+'/'+file,path+'/'+'Torrents/'+file)
                
            else:
                os.makedirs(path+'/'+'Torrents')
                os.rename(path+'/'+file,path+'/'+'Torrents/'+file)

        if ext == 'mp3':
            os.rename(path+'/'+file,r'C:\Users\amaan\Music/'+file)
    print("Done\n")


application()

class Handler(FileSystemEventHandler):
    # def on_created(self,event):
    #     time.sleep(1)
    #     application()
    
    def on_modified(self,event):
        time.sleep(1)
        application()

observer=Observer()
event_handler=Handler()
observer.schedule(event_handler,path,recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
