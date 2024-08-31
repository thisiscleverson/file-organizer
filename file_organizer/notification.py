import asyncio
from pathlib import Path
from desktop_notifier import DesktopNotifier, Button, DEFAULT_SOUND, Urgency



class Notification(DesktopNotifier):
    def __init__(self,title:str, message:str) -> None:
        super().__init__(
            app_name="File Organizer",
            notification_limit=10,
            app_icon="/home/cleverson/Desktop/file-organizer/assets/icons/icon.png"
        )

        self.__title = title
        self.__message = message

        self.__stop_event = asyncio.Event()

        
    async def __notification(self) -> None:
        await self.send(
            icon="assets/icons/move_file.png",
            title=self.__title,
            message=self.__message,
            urgency=Urgency.Critical,
            buttons=[
                Button(
                    title="Abrir no local do arquivo",
                    on_pressed=lambda: [print("Button!"), self.__stop_event.set()],
                )
            ],
            on_clicked=lambda: [print("Notification clicked"), self.__stop_event.set()],
            on_dismissed=lambda: [print("Notification dismissed"), self.__stop_event.set()],
            sound=DEFAULT_SOUND,
        )
        
        await self.__stop_event.wait()

        
    def show(self) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        task = loop.create_task(self.__notification())
        loop.run_until_complete(task)
        loop.close()
