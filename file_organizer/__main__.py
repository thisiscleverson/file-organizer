import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from handler import Handler
from configLoader import ConfigLoader
from pathlib import Path


def run(directory:str, handler:Handler) -> None:
   observer = Observer()

   observer.schedule(
      handler, 
      directory, 
      recursive=False
   )
   observer.start()

   print(f'\n* Watcher Running in {directory}/\n')

   try:
      while True:
         time.sleep(1)
   except:
      observer.stop()
   observer.join()



config_loader = ConfigLoader('config.json')
handler       = Handler(config_loader)

if __name__=="__main__":
   directory = config_loader.json_data.get('monitoringDirectory')

   run(
      directory=directory if directory != None else str(Path.home()) + '/Downloads',
      handler=handler,
   )