import json
import shutil
from pathlib import Path 


class FileCategorize:

   def __init__(self, json_data:dict) -> None:
      self.__json_data = json_data
      self.__user_home_directory = str(Path.home())


   def get_destination_file(self,file_path:str) -> str:
      extension = self.__get_extension_file(file_path)
      type_file = self.__get_type_file(extension=extension)

      if extension == None or type_file == None: return

      file_categories            = self.__json_data.get('fileCategories')
      file_destination_directory = file_categories[type_file].get('destinationDirectory')
      destination_file           = self.__user_home_directory + file_destination_directory
      
      return destination_file


   def __get_type_file(self, extension:str) -> str:
      file_categories = self.__json_data.get('fileCategories')

      for c in file_categories:
         type_file = file_categories.get(c)
         if extension in type_file.get('extensions'):
            return c
      return 


   def __get_extension_file(self, file_path:str) -> str:
      extensions_list = Path(file_path).suffixes
      if extensions_list == []: return

      return extensions_list[-1].replace('.','')


