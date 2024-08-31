import shutil
from pathlib import Path 
from watchdog.events import FileSystemEventHandler, FileSystemEvent

from file_organizer.fileCategorize import FileCategorize
from file_organizer.notification  import Notification


class Handler(FileSystemEventHandler):
   def __init__(self, config_loader:dict) -> None:
      self.__file_categorize = FileCategorize(config_loader)

   def on_created(self, event:FileSystemEvent) -> None:
      self.move_file(event.src_path)


   def move_file(self, path:str) -> None:
      destination_file = self.__file_categorize.get_destination_file(path)

      if not destination_file:
         return

      Path(destination_file).mkdir(parents=True, exist_ok=True)

      filename = Path(path).name
      
      try:
         shutil.move(path, destination_file)
         
      except Exception:
         raise ValueError("It's not possible to move the file!")

      notification = Notification("File Organizer", f'O arquivo "{filename}" foi movido para o diretorio: {destination_file}.')
      notification.show()
