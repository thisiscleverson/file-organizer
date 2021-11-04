import pyinotify
import time
from TypeFile import *
from notices import *
#--------------------#


namefolder = jsonList['Download Directory'] #diretorio do arquivo em que deve ser observado se algumm arquivo foi adicionado

#----------------------------------------------------------------

class MyEventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self,event):
        
        if extension_type(event.name) != 'crdownload':

            if is_type_code(event) == True:
                notifymeMoveFile(event.name, 'Code')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('code',5)
                move_to_folder(event.pathname,path_to_folder)

            elif is_type_txt(event) == True:
                notifymeMoveFile(event.name, 'Txt')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('text',2)
                move_to_folder(event.pathname,path_to_folder)

            elif is_type_pdf(event) == True:
                notifymeMoveFile(event.name, 'Pdf')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('PDF',2)
                move_to_folder(event.pathname,path_to_folder)
            
            elif is_type_video(event) == True:
                notifymeMoveFile(event.name, 'Video')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('Video',4)
                move_to_folder(event.pathname,path_to_folder)
            
            elif is_type_img(event) == True:
                notifymeMoveFile(event.name, 'Imagans')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('Imagens',3)
                move_to_folder(event.pathname,path_to_folder)

            elif is_type_documents(event) == True:
                notifymeMoveFile(event.name, 'Documents')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('Documents',2)
                move_to_folder(event.pathname,path_to_folder)
            
            elif is_type_executable(event) == True:
                notifymeMoveFile(event.name, 'Executable')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('executable',1)
                move_to_folder(event.pathname,path_to_folder)

            elif is_type_zip(event) == True:
                notifymeMoveFile(event.name, 'Zip')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('zip',1)
                move_to_folder(event.pathname,path_to_folder)
            
            elif is_type_3D(event) == True: # arquivo do tipo 3D
                notifymeMoveFile(event.name, '3D')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('3D',2)
                move_to_folder(event.pathname,path_to_folder)

            elif is_type_music(event) == True:
                notifymeMoveFile(event.name, 'Music')# mostrar notificação, mover arquivo
                path_to_folder = make_folder('music',6)
                move_to_folder(event.pathname,path_to_folder)

            if jsonList['TurnOnUnknown'] == True:
                if unknown(event) == True: #arquivo desconhecido
                    notifymeMoveFile(event.name, 'Desconhecido')# mostrar notificação, mover arquivo
                    path_to_folder = make_folder('Desconhecido',1)
                    move_to_folder(event.pathname,path_to_folder)

            '''else:
                path_to_folder = TypeFile.make_folder('Desconhecido',1)
                TypeFile.move_to_folder(event.pathname,path_to_folder)'''


#---------------------------------------------------------------->

def main():
    global jsonList
    wm = pyinotify.WatchManager()
    wm.add_watch(namefolder, pyinotify.ALL_EVENTS, rec=False)

    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    jsonList = ReadJsonConfig()
    notifier.loop()


#---------------------------------------------------------------->

try:
    notifymeActivated()# avizar que o programa foi iniciado
    main() # ativar programa
except:
    notifymeErro()# avizar que ouve erro

