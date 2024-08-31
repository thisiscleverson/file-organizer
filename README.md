# File organizer

**File Organizer** é um software desenvolvido para organizar automaticamente a pasta de Downloads, movendo os arquivos baixados para diretórios apropriados.

[**Vídeo demostrativo**](https://imgur.com/1BWkeLL)

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

## To-Do List

### Observação de Arquivos
- [x] Implementar a funcionalidade de observação de arquivos no diretório especificado.

### Verificação da Extensão do Arquivo
- [x] Verificar a extensão do arquivo para determinar sua categoria.

### Movimento de Arquivo
- [x] Mover o arquivo para o diretório apropriado com base em sua categoria.

### Notificações
- [ ] Mostrar notificações para informar o usuário sobre arquivos movidos.
- [ ] Adicionar um ícone às notificações para maior clareza.
- [ ] Incluir um botão nas notificações para abrir o local do arquivo movido.
- [ ] Adicionar um som de efeito às notificações para alertas auditivos.
