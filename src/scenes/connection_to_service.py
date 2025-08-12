"""The stage module with a connection to the service.

This is where the connection to the service takes place https://httpbin.org, which
specifically simulates a delay of 5 seconds.

"""
import asyncio
from asyncio import Task
from typing import TYPE_CHECKING, Optional

import aiohttp
from pygame import Vector2

from src.scene import Scene

from src.sprites import Text, TextAlign, Waiting, CompletionStatus

if TYPE_CHECKING:
    from src.app import App


class ConnectionToService(Scene):
    """A class with a connection to the service.
    """

    def __init__(self, app: 'App'):
        super().__init__(app)
        self.connection_tasks: dict[str, Optional[asyncio.Task]] = {}

    async def boot(self):
        self.add_sprite('delay_address',
                        Text(self.app, Vector2(10, 10),
                             '* Connecting to httpbin.org/delay/5',
                             align=TextAlign.LEFT))
        self.add_sprite('delay_waiting', Waiting(self.app, Vector2(45, 50), (400, 30),
                                                 CompletionStatus.WORKING))

    async def update(self):
        await self.update_tasks()

    async def enter(self):
        self.connection_tasks['delay'] = asyncio.create_task(self.fetch_get('https://httpbin.org/delay/0'))

    async def exit(self):
        pass

    async def update_tasks(self):
        completed_keys: list[str] = []
        for key, task in self.connection_tasks.items():
            if task and task.done():
                delay_waiting: Waiting = self.get_sprite('delay_waiting')
                result: bool = await task

                delay_waiting.completion_status = CompletionStatus.SUCCESS if result else CompletionStatus.ERROR
                completed_keys.append(key)

        for key in completed_keys:
            await self.connection_tasks.pop(key)

    @staticmethod
    async def fetch_get(url) -> bool:
        """Make a get request.

        Returns:
            True if the response is successful, otherwise False
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status == 200
