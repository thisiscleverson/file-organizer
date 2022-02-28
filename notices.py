import os
import notify2
from playsound import playsound
from TypeFile import jsonList 
from TypeFile import username


def notifymeActivated():
    Title = "File Organizer"
    Message = "O programa foi iniciado!"

    icon = username + jsonList['iconFoleder']
    song = username + jsonList['Activated_program']

    notify2.init("File Organizer")
    n = notify2.Notification(Title,Message,icon)
    n.show()
    playsound(song)


def notifymeErro():
    Title = "File Organizer"
    Message = "Ocorreu um erro na execulção do programa!"

    icon = username + jsonList['Erroicon']
    song = username + jsonList['ErroSong']

    notify2.init("File Organizer")
    n = notify2.Notification(Title,Message,icon)
    n.show()
    playsound(song)


def notifymeMoveFile(NameFile, NameFolder):
    Title = "File Organizer"
    Message = f'O arquivo "{NameFile}" foi movido para a pasta {NameFolder}'
    icon = username + jsonList['MoverFile']
    song = username + jsonList['movefileSong']

    notify2.init("File Organizer")
    n = notify2.Notification(Title,Message,icon)
    n.show()
    playsound(song)

