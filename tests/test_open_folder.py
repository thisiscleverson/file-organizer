import unittest
from unittest.mock import patch, MagicMock
import platform
import os
from pathlib import Path

from file_organizer.button_action import open_folder


class TestOpenFolder(unittest.TestCase):

    @patch('os.system')
    @patch('pathlib.Path.exists')
    def test_open_folder_linux(self, mock_exists, mock_system):
        # Simulando que o diretório existe
        mock_exists.return_value = True
        # Simulando que o sistema operacional é Linux
        with patch('platform.system', return_value="Linux"):
            open_folder("/home/user/folder")
            mock_system.assert_called_with('xdg-open "/home/user/folder"')

    @patch('os.system')
    @patch('pathlib.Path.exists')
    def test_open_folder_windows(self, mock_exists, mock_system):
        mock_exists.return_value = True
        with patch('platform.system', return_value="Windows"):
            open_folder("C:\\Users\\folder")
            mock_system.assert_called_with('explorer "C:\\Users\\folder"')

    @patch('os.system')
    @patch('pathlib.Path.exists')
    def test_open_folder_mac(self, mock_exists, mock_system):
        mock_exists.return_value = True
        with patch('platform.system', return_value="Darwin"):
            open_folder("/Users/folder")
            mock_system.assert_called_with('open "/Users/folder"')

    @patch('pathlib.Path.exists')
    def test_folder_not_found(self, mock_exists):
        # Simulando que o diretório não existe
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            open_folder("/invalid/folder")
