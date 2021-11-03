### Organizador de arquivos 

Este programa foi feito para organizar a pasta de **Downloads**. 

**OBS:** este programa só funciona em sistema linux.

### Bibliotecas usadas no programa:

* **pyinotify**
* **notify2**
* **playsound**
* **shutil**
* **json**
* **time**
* **os**

Essa bibliotecas devem ser instaladas para o fucionamento do programa.

**Lista de bibliotecas para instalar:**

> pip3 install pyinotify

> pip3 install notify2

> pip3 install playsound

> pip3 install pyinstaller

## tranformando em execultavel

com todas a bibliotecas já instaladas com sucesso, usaremos o comando: ```"pyinstaller --noconsole --onefile File_Orfanizer.py" ``` para tansformar em um execultavel.

Depois de ter feito o execultavel, entre nas configurações no arquivo "config.json" e configure os Diretório: 

``` "Download Directory": "/home/xyz/Downloads",```

``` "Document Directory": "/home/xyz/Documents",```

``` "Video Directory":    "/home/xyz/Videos" ```

``` "Music Directory":    "/home/xyz/Music", ```

``` "Imagens Directory":  "/home/xyz/Pictures", ```

``` "code Directory":     "/home/xyz/code/Download_Programs"```

Agora abra o seu gerenciador de inicialização de aplicatovos e selencione o execultavel que você criou. Depois reinicie a sua maquina para que o programa possa ser ativado.