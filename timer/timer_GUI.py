import tkinter as tk
import time
from threading import Thread

class TimerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Timer")

        self.time_left = 0
        self.running = False

        self.label = tk.Label(root, text="00:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack()

        tk.Button(root, text="Start", command=self.start_timer).pack(pady=5)
        tk.Button(root, text="Pause", command=self.pause_timer).pack(pady=5)
        tk.Button(root, text="Reset", command=self.reset_timer).pack(pady=5)

    def start_timer(self):
        try:
            if not self.running:
                if self.time_left == 0:
                    self.time_left = int(self.entry.get())
                self.running = True
                Thread(target=self.run).start()
        except ValueError:
            self.label.config(text="Invalid")

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00")

    def run(self):
        while self.running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.time_left -= 1

        if self.time_left == 0 and self.running:
            self.label.config(text="Time's up!")
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerGUI(root)
    root.mainloop()
