from pathlib import Path 
from file_organizer.config_manager import ConfigManager


class FileCategorize:

   def __init__(self, json_manager:ConfigManager) -> None:
      self.__json_manager = json_manager
      self.__user_home_directory = str(Path.home())


   def get_destination_file(self,file_path:str) -> str:
      extension = self.__get_extension_file(file_path)
      type_file = self.__get_type_file(extension=extension)

      if extension is None or type_file is None:
         return

      key_get_config = "fileCategories." + type_file + ".destinationDirectory"
      
      destination_directory = self.__json_manager.get_config(key_get_config)
      destination_file      = self.__user_home_directory + destination_directory
      
      return destination_file


   def __get_type_file(self, extension:str) -> str:
      file_categories = self.__json_manager.get_config('fileCategories')

      for c in file_categories:
         type_file = file_categories.get(c)
         if extension in type_file.get('extensions'):
            return c
      return 


   def __get_extension_file(self, file_path:str) -> str:
      extensions_list = Path(file_path).suffixes
      if extensions_list == []:
         return

      return extensions_list[-1].replace('.','')
