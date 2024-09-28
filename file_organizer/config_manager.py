import json
import sys
from pathlib import Path



def get_config_path(filename:str) -> Path:
    """
    Retorna o caminho do arquivo de configuração com base no ambiente e no nome do arquivo fornecido.

    - Se o aplicativo estiver rodando como um binário empacotado (verificado via `sys.frozen`),
      o arquivo será armazenado no diretório `~/.file-organizer/config/`.
    - Se o aplicativo estiver em ambiente de desenvolvimento, o arquivo será armazenado
      no diretório local `./` com o **filename**.

    Se o diretório onde o arquivo deve ser armazenado não existir, ele será criado automaticamente.

    Args:
        filename (str): O nome do arquivo de configuração a ser utilizado no ambiente empacotado.

    Returns:
        Path: O caminho completo para o arquivo de configuração.
    """

    if getattr(sys, 'frozen', False):
        config_path = Path.home() / '.file-organizer' / 'config'
        config_dir  = Path(config_path)
        config_file = config_dir / filename
    else:
        config_file = Path(filename)
    
    
    if not config_file.parent.exists():
        config_file.parent.mkdir(parents=True, exist_ok=True)
    
    return config_file



class ConfigManager:
    def __init__(self, filename:str = 'config.json') -> None:
        self.__config_path = get_config_path(filename)
        self.__config_data = None
        self.load_config()


    def load_config(self) -> None:
        if not Path(self.__config_path).exists():
            raise FileNotFoundError(f"O arquivo de configuração {self.__config_path} não foi encontrado.")

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
