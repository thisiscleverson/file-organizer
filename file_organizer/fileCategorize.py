import json
import shutil
from pathlib import Path 


class FileCategorize:

   #TODO: separar os métodos de leitura do json
   def __init__(self, json_data:dict) -> None:
      self.__json_data = json_data
      self.__user_home_directory = str(Path.home())


   def get_destination_file(self,file_path:str) -> str:
      extension = self.__get_extension_file(file_path)
      type_file = self.__get_type_file(extension=extension)

      if extension == None or type_file == None: return

      file_type_directories = self.__json_data.get('fileTypeDirectories')
      file_directory        = file_type_directories.get(type_file)
      destination_file      = self.__user_home_directory + file_directory
      
      return destination_file


   def __get_type_file(self, extension:str) -> str:
      
      types_file = self.__json_data.get('fileCategories')

      for _type in types_file:
         if extension in types_file.get(_type):
            return _type
      return 


   def __get_extension_file(self, file_path:str) -> str:
      extensions_list = Path(file_path).suffixes
      if extensions_list == []: return

      return extensions_list[-1].replace('.','')


