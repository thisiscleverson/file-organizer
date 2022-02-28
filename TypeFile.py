import os
import shutil
import json

#Directory = username + 'file-organizer/config.json'

usernameDirectory = os.path.expanduser("~/")
username = os.path.dirname(os.path.abspath(""))
Directory = username + '/file-organizer/config.json'


def findDirectory():
    Directory = os.getcwd() 
    output = Directory.split('/')

    for l in range(0,len(output)):
        if output[l] == 'dist':
            index = output.index('dist')
            output.pop(index)
            break

    newDirectory = ''
    for i in range(1,len(output)):
        newDirectory = newDirectory + '/' + output[i]
        
    return newDirectory

    

def ReadJsonConfig():
    #Directory = findDirectory() + '/config.json'
    fileObject = open(Directory, 'r')
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    return aList

def extension_type(event): # separar nome por tipo de arquivos
   try:
      return event[event.rindex('.') + 1:]
   except:
      #print(f'erro ao indentificar o tipo de arquivo {event}!')
      #return None
      pass
    
# type of file:

def is_type_code(event):
    if extension_type(event.name) in jsonList['code']:
        return True
    return False

def is_type_txt(event):
    if extension_type(event.name) in jsonList['txt']:
        return True
    return False
 
def is_type_pdf(event):
    if extension_type(event.name) in jsonList['pdf']:
        return True
    return False
 
def is_type_video(event):
    if extension_type(event.name) in jsonList['video']:
        return True
    return False
 
def is_type_img(event):
    if extension_type(event.name) in jsonList['imagens']:
        return True
    return False
    
def is_type_documents(event):
    if extension_type(event.name) in jsonList['documents']:
        return True
    return False

def is_type_executable(event):
    if extension_type(event.name) in jsonList['executable']:
        return True
    return False

def is_type_zip(event):
    if extension_type(event.name) in jsonList['zip']:
        return True
    return False

def is_type_3D(event):
    if extension_type(event.name) in jsonList['3D']:
        return True
    return False

def is_type_music(event):
    if extension_type(event.name) in jsonList['music']:
        return True
    return False

def unknown(event):
    if extension_type(event.name) in ('', ' '):
        return True
    return False

#----------------------------------------------------------------
def make_folder(folderName,whatDirectory):
    if whatDirectory == 1: # Downloads
        os.chdir(usernameDirectory + jsonList['Download Directory'])

    elif whatDirectory == 2: # Documents
        os.chdir(usernameDirectory + jsonList['Document Directory'])

    elif whatDirectory == 3: # Imagens
        os.chdir(usernameDirectory + jsonList['Imagens Directory'])

    elif whatDirectory == 4: # video
        os.chdir(usernameDirectory + jsonList['Video Directory'])

    elif whatDirectory == 5: # code
        os.chdir(usernameDirectory + jsonList['code Directory'])

    elif whatDirectory == 6: # music
        os.chdir(usernameDirectory + jsonList['Music Directory'])
 

    if os.path.exists(folderName) == True:
        print('Folder already exists, skipping creation')
        return os.getcwd() + os.sep + str(folderName)
    else:
        os.mkdir(str(folderName))
        return os.getcwd() + os.sep + str(folderName)

def move_to_folder(event,path_to_new_folder):
    try:
        shutil.move(event, path_to_new_folder)
    except:
        pass


#--------------------------------------------------------------------------------------------------------------------#
jsonList = ReadJsonConfig()

