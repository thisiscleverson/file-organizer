import asyncio
from pathlib import Path
from desktop_notifier import DesktopNotifier, Button, Urgency, Icon, Sound
from typing import Callable
from file_organizer.icon_path import IconsPath

def get_absolute_path(path:str) -> str | None:
    absolute_path = Path(path).absolute()

    if absolute_path.exists():
        return absolute_path
    return None



class Notification(DesktopNotifier):
    def __init__(self,title:str, message:str, icon:str) -> None:
        super().__init__(
            app_name="File Organizer",
            notification_limit=10,
            app_icon=Icon(path=get_absolute_path(IconsPath.ICON.value))
        )

        self.__icon       = icon
        self.__title      = title
        self.__message    = message
        self.__button     = []
        self.__stop_event = asyncio.Event()

        
    def set_button(self, title:str, action:Callable=None) -> None:        
        self.__button.append(
            Button(
                title=title,
                on_pressed=lambda: [
                    action() if action else None,
                    self.__stop_event.set()
                ],
            )
        )

        
    async def __notification(self) -> None:        
        await self.send(
            icon = Icon(path=get_absolute_path(self.__icon)),
            title=self.__title,
            message=self.__message,
            urgency=Urgency.Critical,
            buttons=self.__button,
            on_clicked=lambda: self.__stop_event.set(),
            on_dismissed=lambda: self.__stop_event.set(),
            sound=Sound(name=get_absolute_path("./assets/sounds/sound.mp3")),
        )
        
        await self.__stop_event.wait()

        
    def show(self) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        task = loop.create_task(self.__notification())
        loop.run_until_complete(task)
        loop.close()
