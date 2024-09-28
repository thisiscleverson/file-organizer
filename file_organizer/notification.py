import asyncio
import sys
from pathlib import Path
from desktop_notifier import DesktopNotifier, Button, Urgency, Icon, Sound
from typing import Callable
from file_organizer.icons_path import IconsPath

def get_assets_path(path:str) -> str | None:
    if getattr(sys, 'frozen', False):
        asset_path  = Path.home() / '.file-organizer'
        assets_dir  = Path(asset_path)
        assets_file = assets_dir / path
    else:
        assets_file = Path('./' + path).absolute()

    if assets_file.exists():
        return assets_file
    return None



class Notification(DesktopNotifier):
    def __init__(self,title:str, message:str, icon:str) -> None:
        super().__init__(
            app_name="File Organizer",
            notification_limit=10,
            app_icon=Icon(path=get_assets_path(IconsPath.ICON.value))
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
            icon = Icon(path=get_assets_path(self.__icon)),
            title=self.__title,
            message=self.__message,
            urgency=Urgency.Critical,
            buttons=self.__button,
            on_clicked=lambda: self.__stop_event.set(),
            on_dismissed=lambda: self.__stop_event.set(),
            sound=Sound(name=get_assets_path("assets/sounds/sound.mp3")),
        )
        
        await self.__stop_event.wait()

        
    def show(self) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        task = loop.create_task(self.__notification())
        loop.run_until_complete(task)
        loop.close()
