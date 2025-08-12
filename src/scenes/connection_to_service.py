"""The stage module with a connection to the service.

This is where the connection to the service takes place https://httpbin.org, which
specifically simulates a delay of 5 seconds.

"""
from typing import TYPE_CHECKING

from src.scene import Scene

if TYPE_CHECKING:
    from src.app import App


class ConnectionToService(Scene):
    """A class with a connection to the service.
    """

    def __init__(self, app: 'App'):
        super().__init__(app)

    async def boot(self):
        pass

    async def update(self):
        pass

    async def enter(self):
        pass

    async def exit(self):
        pass
