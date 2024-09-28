# File organizer

**File Organizer** é um software desenvolvido para organizar automaticamente a pasta de Downloads, movendo os arquivos baixados para diretórios apropriados.

[**Vídeo demostrativo**](https://imgur.com/1BWkeLL)

## Como instalar?

Para instalar o **File Organizer**, certifique-se de ter o **Python 3.11** ou superior instalado. Em seguida, execute o comando abaixo:
```bash
./install.sh
```

> ⚠️ Este instalador só funciona em ambiente Linux!

Esse script irar criar um pasta `.file-organizer` na home do sistema com a seguinte estrutura:

```
.file-organizer
├── assets
│   ├── icons
│   │   ├── error.png
│   │   ├── icon.png
│   │   └── moved.png
│   └── sounds
│       └── sound.mp3
├── config
│   └── config.json
└── dist
    └── File Organizer
```

Você pode configurar seus filtros no arquivo`config/config.json`. Veja mais como configurar os filtros na sessão [Configurando os diretórios](#configurando-os-diretórios).

O script adicionará o **File Organizer** ao `autostart` do sistema operacional, permitindo que ele seja iniciado automaticamente junto com o sistema.

## Como executar?

Para poder executar o projeto é recomendado que você tenha o `Poetry` instalado e o `Python` com a versão `3.11` ou superior.

para configurar todo o ambiente basta executar:

```bash
poetry install
```

você pode instalar usando o pip com o seguinte comando:

```bash
pip install watchdog==4.0.1 pytest==8.2.2 desktop-notifier==5.0.1 ruff==0.6.2 taskipy==1.13.0
```

> Se for usar o pip, recomendo você usar um ambiente virtual.

para executar o projeto, use o seguinte comando:

```bash
task run
```

ou 

```bash
python -m file_organizer
```

## Configurando os diretórios

No arquivo `config.json`, você pode configurar o diretório que o File Organizer irá monitorar.

```json
"monitoringDirectory": "/Downloads"
```

Abaixo estão os filtros configuráveis para categorias de arquivos, com suas respectivas extensões e diretórios de destino:

```json
"fileCategories": {
   "imagens": {
      "extensions": ["jpeg", "jpg", "img", "svg", "png", "gif"],
      "destinationDirectory": "/Pictures/Imagens"
   },
   "video": {
      "extensions": ["mov", "mp4", "avi", "flv"],
      "destinationDirectory": "/Videos/Videos"
   },
   "documents": {
      "extensions": ["docx", "xlsx", "doc", "xls", "odp", "pptx", "txt"],
      "destinationDirectory": "/Documents/Documentos"
   },
   "compressed": {
      "extensions": ["zip", "whl", "iso", "xz", "gz"],
      "destinationDirectory": "/Downloads/Zip"
   },
   "executable": {
      "extensions": ["deb", "exe"],
      "destinationDirectory": "/Downloads/Executaveis"
   },
   "music": {
      "extensions": ["mp3"],
      "destinationDirectory": "/Music/Audios"
   },
   "pdf": {
      "extensions": ["pdf"],
      "destinationDirectory": "/Documents/PDF"
   }
}
```

Você pode adicionar seus próprios filtros de arquivos utilizando a seguinte estrutura:

```json
"tipo_do_arquivo": {
   "extensions": ["xxx", "yyy", "zzz"],
   "destinationDirectory": "/diretorio/de/destino"
}
```

Substitua "tipo_do_arquivo", "xxx", "yyy", "zzz", e "diretorio/de/destino" pelos valores desejados para criar novos filtros personalizados.
