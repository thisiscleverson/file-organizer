#!/bin/bash

# 1. Definir variáveis
VENV_DIR=".venv"
PROJECT_DIR=$(pwd)
PYINSTALLER_OUTPUT_DIR="./dist"
ENTRY_POINT="file_organizer/__main__.py"
ENVIRONMENT_NAME="file-organizer"
POETRY_VENV_PATH="$HOME/.cache/pypoetry/virtualenvs/$ENVIRONMENT_NAME-LioAqKyK-py3.12"
FILENAME="File Organizer"
CONFIG_DIR="$HOME/.file-organizer/config"
AUTOSTART_DIR="$HOME/.config/autostart"
DESKTOP_FILE="$HOME/.config/autostart/$FILENAME.desktop"
ICON_FILE="$HOME/.file-organizer/assets/icons/icon.png"
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

# 2. Criar o ambiente virtual
if [ ! -d "$VENV_DIR" ]; then
    echo "🌱 Criando ambiente virtual..."
    python3 -m venv $VENV_DIR
fi

# 3. Ativar o ambiente virtual
source $VENV_DIR/bin/activate

echo "📦 Instalando dependências com pip..."
pip install .

# 4. Verificar se o pacote desktop_notifier foi instalado corretamente
DESKTOP_NOTIFIER_RESOURCES_PATH="$VENV_DIR/lib64/python$PYTHON_VERSION/site-packages/desktop_notifier/resources"
if [ ! -d "$DESKTOP_NOTIFIER_RESOURCES_PATH" ]; then
    echo "❌ Erro: Caminho para desktop_notifier/resources não encontrado!"
    exit 1
fi

# 5. Executar PyInstaller para empacotar o aplicativo
echo "🚀 Empacotando com PyInstaller..."
pyinstaller --onefile --name="$FILENAME" --add-binary="$DESKTOP_NOTIFIER_RESOURCES_PATH:desktop_notifier/resources" $ENTRY_POINT

# 6. Mover o binário gerado para a pasta dist
if [ -f "$PYINSTALLER_OUTPUT_DIR/$FILENAME" ]; then
    echo "✅ Empacotamento concluído com sucesso! Binário disponível em $PYINSTALLER_OUTPUT_DIR."
else
    echo "❌ Erro: Não foi possível gerar o executável."
    exit 1
fi

# 7. Criar diretório de configuração
mkdir -p "$CONFIG_DIR"

# 8. Mover o arquivo config.json para o diretório de configuração
if [ -f "config.json" ]; then
    cp "config.json" "$CONFIG_DIR/"
    echo "📄 Arquivo config.json movido para $CONFIG_DIR."
else
    echo "⚠️ Aviso: config.json não encontrado. Não foi possível mover."
fi

# 9. Copiar a pasta assets para ~/.file-organizer
if [ -d "assets/" ]; then
    cp -r "assets/" "$HOME/.file-organizer/"
    echo "📁 Pasta assets copiada para ~/.file-organizer."
else
    echo "⚠️ Aviso: assets/ não encontrado. Não foi possível copiar."
fi

# 10. Copiar a pasta dist para ~/.file-organizer
if [ -d "$PYINSTALLER_OUTPUT_DIR" ]; then
    cp -r "$PYINSTALLER_OUTPUT_DIR" "$HOME/.file-organizer/"
    echo "📦 Pasta dist copiada para ~/.file-organizer."
else
    echo "⚠️ Aviso: dist/ não encontrado. Não foi possível copiar."
fi

# 11. Criar diretório autostart se não existir
mkdir -p "$AUTOSTART_DIR"

# 12. Criar o arquivo .desktop para inicialização automática
echo "[Desktop Entry]" > "$DESKTOP_FILE"
echo "Version=2.0" >> "$DESKTOP_FILE"
echo "Type=Application" >> "$DESKTOP_FILE"
echo "Name=\"$FILENAME\"" >> "$DESKTOP_FILE"
echo "Exec=\"$HOME/.file-organizer/dist/$FILENAME\"" >> "$DESKTOP_FILE"
echo "StartupNotify=true" >> "$DESKTOP_FILE"
echo "Terminal=false" >> "$DESKTOP_FILE"
echo "Icon=\"$ICON_FILE\"" >> "$DESKTOP_FILE"
echo "Categories=Utility;" >> "$DESKTOP_FILE"

# 13. Definindo permissões de execução
chmod +x "$DESKTOP_FILE"

echo "💻 Arquivo .desktop criado para inicialização automática em $DESKTOP_FILE."

# 14. Desativar o ambiente virtual
deactivate

echo "🎉 Instalação concluída."
