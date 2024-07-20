import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from handler import Handler
from configLoader import ConfigLoader




def run(directory:str, observer:Observer, handler:Handler) -> None:
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



observer  = Observer()
handler   = Handler()

config_loader = ConfigLoader('config.json')

if __name__=="__main__":
   directory = config_loader.json_data.get('monitoringDirectory')

   run(
      directory=directory,
      observer=observer,
      handler=handler
   )