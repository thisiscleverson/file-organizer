import json


class ConfigLoader:
   def __init__(self, config_path: str = 'config.json') -> None:
      self.__config_path = config_path
      self.json_data = self.load_config()

   def load_config(self) -> dict:
      try:
         with open(self.__config_path, 'r') as file:
            return json.load(file)
      except FileNotFoundError:
         print(f"Config file {self.config_path} not found.")
         return {}
      except json.JSONDecodeError:
         print(f"Error decoding JSON from {self.config_path}.")
         return {}