import time
from watchdog.observers import Observer
from pathlib import Path

#module
from file_organizer.handler import Handler
from file_organizer.config_manager import ConfigManager


def run(directory:str, handler:Handler) -> None:
   observer = Observer()

   observer.schedule(
      handler, 
      directory, 
      recursive=False
   )
   observer.start()

   #print(f'\n* Watcher Running in {directory}/\n')

   try:
      while True:
         time.sleep(1)
   except Exception:
      observer.stop()
   except KeyboardInterrupt:
      observer.stop()
   observer.join()



config_manager = ConfigManager('config.json')
handler        = Handler(config_manager)

if __name__=="__main__":
   user_home_directory = str(Path.home())
   
   directory = user_home_directory + config_manager.get_config("monitoringDirectory")

   run(
      directory=directory if directory is not None else str(Path.home()) + '/Downloads',
      handler=handler
   )
