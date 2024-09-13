import json
from pathlib import Path

class ConfigManager:
   def __init__(self, config_path: str = 'config.json') -> None:
      self.__config_path = config_path
      self.__config_data = None
      self.load_config()

   def load_config(self) -> None:
      if not Path(self.__config_path).exists():
         raise FileNotFoundError(f"O arquivo de configuração {self.config_file} não foi encontrado.")

      try:
         with open(self.__config_path, 'r') as file:
            self.__config_data = json.load(file)
      except json.JSONDecodeError:
         #print(f"Error decoding JSON from {self.config_path}.")
         self.__config_data = {}

         
   def get_config(self, key:str, default=None) -> dict:
      """
      Retorna o valor de uma configuração com base em um caminho hierárquico.

      Usa um caminho separado por pontos para buscar o valor correspondente em um dicionário de configurações.
      Se a chave não for encontrada, retorna o valor padrão especificado.

      Args:
        key (str): O caminho para o valor desejado, separado por pontos (ex: 'database.host').
        default: O valor a ser retornado se a chave não for encontrada (padrão é None).

      Returns:
        dict: O valor correspondente à chave, ou o valor padrão se não for encontrada.
    
      Example:
        host = config_manager.get_config('database.host', '127.0.0.1')
      """

      self.load_config() # reload file
      
      keys = key.split('.')
      value = self.__config_data
   
      try:
         for k in keys:
            value = value[k]
      except KeyError:
         return default
      return value
