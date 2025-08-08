"""The main program file.
"""
from src.app import App


def main():
    """The function starts when the program is started.
    """
    app = App()
    app.change_scene('Intro')
    app.loop()


if __name__ == '__main__':
    main()
