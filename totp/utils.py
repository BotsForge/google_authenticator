import ctypes


LOGO = """
╔══╗─╔══╗╔════╗╔══╗────╔══╗╔══╗╔═══╗╔═══╗╔═══╗
║╔╗║─║╔╗║╚═╗╔═╝║╔═╝────║╔═╝║╔╗║║╔═╗║║╔══╝║╔══╝
║╚╝╚╗║║║║──║║──║╚═╗╔══╗║╚═╗║║║║║╚═╝║║║╔═╗║╚══╗
║╔═╗║║║║║──║║──╚═╗║╚══╝║╔═╝║║║║║╔╗╔╝║║╚╗║║╔══╝
║╚═╝║║╚╝║──║║──╔═╝║────║║──║╚╝║║║║║─║╚═╝║║╚══╗
╚═══╝╚══╝──╚╝──╚══╝────╚╝──╚══╝╚╝╚╝─╚═══╝╚═══╝
https://t.me/bots_forge
"""


def set_console_size_and_name(width: int, height: int, name: str = None) -> None:
    if hwnd := ctypes.windll.kernel32.GetConsoleWindow():
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        left = (screen_width - width) // 2
        top = (screen_height - height) // 2

        ctypes.windll.user32.MoveWindow(hwnd, left, top, width, height, True)
        if name:
            ctypes.windll.kernel32.SetConsoleTitleW(name)
