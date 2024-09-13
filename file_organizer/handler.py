import shutil
from pathlib import Path
from functools import partial
from watchdog.events import FileSystemEventHandler, FileSystemEvent

from file_organizer.fileCategorize import FileCategorize
from file_organizer.notification  import Notification
from file_organizer.button_action import open_folder, replace_file
from file_organizer.icon_path import IconsPath


class Handler(FileSystemEventHandler):
   def __init__(self, config_loader:dict) -> None:
      self.__file_categorize = FileCategorize(config_loader)

      
   def on_created(self, event:FileSystemEvent) -> None:
      self.move_file(event.src_path)

      
   def move_file(self, path:str) -> None:
      destination_file = self.__file_categorize.get_destination_file(path)
      
      if not destination_file:
         return

      foldername       = self.__get_foldername(destination_file)
      filename         = Path(path).name
      
      if self.__check_if_file_exists(path, destination_file, filename):
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

      
   def __get_foldername(self, destination_file:str) -> str:
      return destination_file.split("/")[-1]


   def __check_if_file_exists(self, path:str, destination_file:str, filename:str) -> bool:
      foldername = self.__get_foldername(destination_file)
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
