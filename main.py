import sys
import keyboard
import tkinter as tk
import cv2
from threading import Thread
from timer import OverlayStopwatch
from loc_point import find_point_loc

### Для копиляции в .exe pyinstaller --onefile --hidden-import cv2 --add-data "sources/probka.png;sources" --icon sources/icon.ico main.py

class App():
    def __init__(self, root):
        self.root = root
        self.stopwatch = OverlayStopwatch(root)

        keyboard.add_hotkey('k', self._main_logic)
        keyboard.add_hotkey('f12', self.break_main)

    def run_main(self):
        """Запускает main() в отдельном потоке (чтобы не блокировать Tkinter)."""
        Thread(target=self._main_logic, daemon=True).start()

    def break_main(self):
        print("Аварийная остановка активирована!")
        self.root.destroy()
        sys.exit(0)

    def _main_logic(self):
        print('Запуск main_logic...')
        find_point_loc()
        return 
    
def print_banner():
    banner = """
    ███╗   ███╗██╗  ██╗██╗   ██╗██╗  ██╗
    ████╗ ████║██║ ██╔╝██║   ██║██║ ██╔╝
    ██╔████╔██║█████╔╝ ██║   ██║█████╔╝ 
    ██║╚██╔╝██║██╔═██╗  ██╗ ██╔╝██╔═██╗ 
    ██║ ╚═╝ ██║██║  ██╗  ████╔╝ ██║  ██╗
    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝
    
    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗███████╗
    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝
    ███████╗██║     ██████╔╝██║██████╔╝   ██║   ███████╗
    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ╚════██║
    ███████║╚██████╗██║  ██║██║██║        ██║   ███████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚══════╝
    """
    print(banner)
    print("=" * 60)
    print(">>> Готов к работе. <<<")
    print(">>> Установлено звуковое сопровождение на 00:01:00 <<<")
    print(">>> Для отображения таймера запустите игру в оконном режмие <<<")
    print(">>> Нажмите [K] для запуска <<<")
    print(">>> Timer reset: [E] <<<")
    print(">>> Emergency Stop: [F12] <<<")
    print("=" * 60)

if __name__ == '__main__':
    print_banner()
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.stopwatch.safe_close)
    root.mainloop()