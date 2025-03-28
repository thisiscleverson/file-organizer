import shutil
import time
from pathlib import Path
from functools import partial
from watchdog.events import FileSystemEventHandler, FileSystemEvent

from file_organizer.fileCategorize import FileCategorize
from file_organizer.notification  import Notification
from file_organizer.button_action import open_folder, replace_file
from file_organizer.icons_path import IconsPath


class Handler(FileSystemEventHandler):
   def __init__(self, config_loader:dict) -> None:
      self.file_categorize = FileCategorize(config_loader)
      self.start_size = -1
      self.src_path = ''


   def on_created(self, event:FileSystemEvent) -> None:
      self.src_path = event.src_path

      
   def on_modified(self, event:FileSystemEvent) -> None:
      src_path = Path(event.src_path)

      download_competed = self.check_download_has_completed(src_path)
      
      if download_competed == True  and self.src_path != '':
         self.move_file(self.src_path)
         self.src_path = ''

      
   def move_file(self, path:str) -> None:
      destination_file = self.file_categorize.get_destination_file(path)
      
      if not destination_file:
         return

      foldername = self.get_foldername(destination_file)
      filename = Path(path).name
      
      if self.check_if_file_exists(path, destination_file, filename):
         return

      Path(destination_file).mkdir(parents=True, exist_ok=True)

      try:
         shutil.move(path, destination_file)
         
      except Exception:
         notification = Notification(
            icon=IconsPath.ERROR.value,
            title="Erro",
            message=f'Não foi povivel mover o arquivo "{filename}" para a pasta "{foldername}".'
         )
         
         notification.show()
         return


      notification = Notification(
         icon=IconsPath.MOVED.value,
         title="Arquivo movido",
         message=f'O arquivo "{filename}" foi movido para a pasta "{foldername}".',
      )
      
      notification.set_button(
         title="Exibir o arquivo na pasta",
         action=partial(open_folder, destination_file),
      )
      
      notification.show()

   def check_download_has_completed(self, src_path:Path) -> bool:

      if src_path.is_dir():
         return False

      file_size = src_path.stat().st_size if src_path.exists() else 0

      if file_size > self.start_size:
         self.start_size = file_size
         time.sleep(2)
         return False
   
      self.start_size = -1
      return True

      
   def get_foldername(self, destination_file:str) -> str:
      return destination_file.split("/")[-1]


   def check_if_file_exists(self, path:str, destination_file:str, filename:str) -> bool:
      foldername = self.get_foldername(destination_file)
      file_src   = destination_file + "/" + filename
      
      if Path(file_src).exists():
         notification = Notification(
            icon=IconsPath.ICON.value,
            title="Arquivo existente",
            message=f'O arquivo "{filename}" já existe na pasta "{foldername}".'
         )

         notification.set_button(title="Substituir e exibir arquivo na pasta", action=partial(replace_file, path, destination_file, filename))
         notification.set_button(title="Ignorar")
         
         notification.show()
         return True
      
      return False
