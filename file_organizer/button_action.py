import os
import shutil
import platform
from pathlib import Path


def open_folder(path:str) -> None:
    if not Path(path).exists():
        raise FileNotFoundError(f'O diretório "{path}" não foi encontrado.')
    
    if platform.system() == "Windows":
        os.system(f'explorer "{path}"')
        return
    
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open "{path}"')
        return

    os.system(f'xdg-open "{path}"')  # Linux and others



def replace_file(path:str, dst:str, filename:str) -> None:

    src_file = dst + "/" + filename
    
    Path(src_file).unlink() # remove file

    try:
        shutil.move(path, dst)
    except Exception:
        pass

    open_folder(dst)
