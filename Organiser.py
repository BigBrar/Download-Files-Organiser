import sys
import time
import logging
from watchdog.observers import Observer
import os 
import shutil
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler

p = Path.home()
program_files = ['.tar', '.deb', '.bz2', '.exe','.rpm']
zip_files = ['.tar.gz', '.gz','.zip',]
document_files = ['.txt', '.docx', '.docs', '.doc', '.odt', '.rtf', '.wpd', '.tex', '.html']
image_files = ['.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png', '.eps', '.ico', '.raw', '.img']
video_files = ['.mp4', '.webm', '.wav', '.movie', '.avi', '.mpeg', '.wmv', '.mkv', '.m4v']


def on_created(event):
    file = os.listdir('/home/deepinder/Downloads/')
    for content in file:
        python_file = content.endswith('.py')
        if content.endswith(tuple(document_files)):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/Document Files')
            shutil.move(tentent, '/home/deepinder/Downloads/Document Files')
        #elif content.endswith('.tar'):
        #   tentent = ("/home/deepinder/Downloads/"+content)
        #   print(tentent)
        #   shutil.move(tentent, '/home/deepinder/Downloads/Program Files')
        elif content.endswith(tuple(program_files)):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/Program Files')
            shutil.move(tentent, '/home/deepinder/Downloads/Program Files')
        elif content.endswith(tuple(zip_files)):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/Zip Files')
            shutil.move(tentent, '/home/deepinder/Downloads/Zip Files')
        elif content.endswith('.pdf'):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/PDF Files')
            shutil.move(tentent, '/home/deepinder/Downloads/PDF Files')
        elif content.endswith(tuple(image_files)):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/Image Files')
            shutil.move(tentent, '/home/deepinder/Downloads/Image Files')
        elif content.endswith(tuple(video_files)):
            tentent = ("/home/deepinder/Downloads/"+content)
            print(content+' ==>> /home/deepinder/Downloads/Video Files')
            shutil.move(tentent, '/home/deepinder/Downloads/Video Files')

if __name__ == "__main__":
   
    event_handler = FileSystemEventHandler()
    
    event_handler.on_created = on_created

    path ="/home/deepinder/Downloads/"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("monitoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print('done')
    observer.join()