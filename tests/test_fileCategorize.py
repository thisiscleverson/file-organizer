import os
import unittest

from file_organizer.fileCategorize import FileCategorize
from file_organizer.configLoader import ConfigLoader


 #TODO: refatorar esse teste fazendo o watchdog observar a pasta. 
 # Além de criar o arquivo que supostamente será movido para o diretório correspondido
class TestFileCategorize(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      config_loader = ConfigLoader('config.json')
      cls.file_categorize = FileCategorize(config_loader.json_data) 


   def test_get_extension_returns_txt_when_the_file_has_a_txt_extension(self):
      file_with_single_extension = "file.txt"
      
      extension = self.file_categorize._FileCategorize__get_extension_file(file_with_single_extension)  
      
      self.assertEqual(extension, 'txt')


   def test_get_extension_returns_txt_when_the_file_has_a_example_and_txt_extension(self):
      file_with_multiple_extensions = "file.example.txt"

      extension = self.file_categorize._FileCategorize__get_extension_file(file_with_multiple_extensions)  
      
      self.assertEqual(extension, 'txt')

   
   def test_get_extension_returns_None_when_the_file_does_not_has_an_extension(self):
      file_without_extension = "file"
      
      extension = self.file_categorize._FileCategorize__get_extension_file(file_without_extension)  
      
      self.assertIsNone(extension)


   def test_get_type_file_returns_documents_if_file_has_txt_extension(self):
      file_with_single_extension = "file.txt"

      extension = self.file_categorize._FileCategorize__get_extension_file(file_with_single_extension)

      type_file = self.file_categorize._FileCategorize__get_type_file(extension)  
      
      self.assertEqual(type_file, 'documents')

   #TODO: refazer a logica do test, fazendo o assert dentro do for
   def test_get_type_file_returns_correct_file_type_of_files(self):
      list_of_files = ["file.pdf", "file.png", "file.mp3", "file.mp4","file.zip", "file.deb",'file.txt']
      list_of_type_file = []


      for _file in list_of_files:
         extension = self.file_categorize._FileCategorize__get_extension_file(_file)
         type_file = self.file_categorize._FileCategorize__get_type_file(extension)
         list_of_type_file.append(type_file)
      

      self.assertCountEqual(
         list_of_type_file, 
         ["imagens", "video", "documents", "executable", "music","compressed", "pdf"]
      )

  
   def test_get_destination_file_return_documents_directory_when_the_file_has_txt_extension(self):
      file_with_single_extension = "file.txt"
      correct_directory = os.path.expanduser("~") + "/Desktop/observer_folder/documentos"

      destination_file = self.file_categorize.get_destination_file(file_with_single_extension)
      
      self.assertEqual(destination_file, correct_directory)


   def test_get_destination_file_return_None_when_the_file_does_not_has_an_extension(self):
      file_without_extension = "file"
      correct_directory = os.path.expanduser("~") + "/Desktop/observer_folder/documentos"

      destination_file = self.file_categorize.get_destination_file(file_without_extension)
      
      self.assertIsNone(destination_file)

