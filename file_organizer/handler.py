import shutil
from pathlib import Path 
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from fileCategorize import FileCategorize


class Handler(FileSystemEventHandler):
   def __init__(self, config_loader:dict) -> None:
      self.__file_categorize = FileCategorize(config_loader)


   def on_created(self, event:FileSystemEvent) -> None:
      self.move_file(event.src_path)


   def move_file(self, path:str) -> None:
      destination_file = self.__file_categorize.get_destination_file(path)

      if destination_file is None: return

      """ if not Path(destination_file).exists():
         Path(destination_file).mkdir(parents=True, exist_ok=True) """

      Path(destination_file).mkdir(parents=True, exist_ok=True)

      try:
         shutil.move(path, destination_file)
         print(f'file: {Path(path).stem} moved!')
      
      except:
         raise Exception("It's not possible to move the file!")