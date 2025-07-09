import tkinter as tk
from tkinter import ttk
import time
import keyboard 
import winsound

class OverlayStopwatch:
    def __init__(self, root):
        self.root = root
        # Основные настройки окна
        self.root.title("⏱️ Таймер")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.geometry("220x150+1150+20") 
        self.root.configure(bg='#121212')
        
        main_frame = tk.Frame(root, bg='#121212')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.label = tk.Label(
            main_frame,
            text="00:00:00",
            font=("Segoe UI", 28, "bold"),
            fg="#00FFAA",
            bg='#121212',
            pady=10
        )
        self.label.pack(fill='x')
        
        button_frame = tk.Frame(main_frame, bg='#121212')
        button_frame.pack(fill='x', pady=(10, 0))
        
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('TButton',
                      font=('Segoe UI', 9, 'bold'),
                      borderwidth=1,
                      padding=5)
        
        style.map('Reset.TButton',
                foreground=[('pressed', 'white'), ('active', 'white')],
                background=[('pressed', '#3A3A3A'), ('active', '#3A3A3A')])
        
        style.map('Close.TButton',
                foreground=[('pressed', 'white'), ('active', 'white')],
                background=[('pressed', '#d32f2f'), ('active', '#f44336')])
        
        # Кнопка сброса
        self.reset_btn = ttk.Button(
            button_frame,
            text="⟳ Сброс (E)",
            style='Reset.TButton',
            command=self.reset_and_start
        )
        self.reset_btn.pack(side='left', expand=True)
        
        # Кнопка закрытия
        self.close_btn = ttk.Button(
            button_frame,
            text="× Закрыть",
            style='Close.TButton',
            command=self.safe_close
        )
        self.close_btn.pack(side='right', expand=True)
        
        # Инициализация таймера
        self.is_running = False
        self.start_time = 0
        self.alarm_triggered = False
        
        # Горячая клавиша для сброса
        keyboard.on_press_key("e", lambda _: self.reset_and_start())
        
        # Запуск таймера
        self.reset_and_start()
    
    def reset_and_start(self):
        self.start_time = time.time()
        self.alarm_triggered = False
        if not self.is_running:
            self.is_running = True
            self.update_time()
    
    def update_time(self):
        if not self.is_running:
            return
            
        elapsed = time.time() - self.start_time
        h = int(elapsed // 3600)
        m = int((elapsed % 3600) // 60)
        s = int(elapsed % 60)
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        self.label.config(text=time_str)
        
        # Проверка на 00:01:00 и воспроизведение звука
        if m == 1 and s == 00 and not self.alarm_triggered:
            self.play_alarm()
            self.alarm_triggered = True  
        
        if self.is_running:
            self.root.after(50, self.update_time)
    
    def play_alarm(self):
        winsound.Beep(700, 500)  
    
    def safe_close(self):
        self.is_running = False
        self.root.destroy()
