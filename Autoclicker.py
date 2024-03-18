import tkinter as tk
import time
from pynput.mouse import Button, Controller

class AutoClicker:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Auto Clicker")

    self.click_rate_label = tk.Label(self.root, text="Click Rate (CPS):")
    self.click_rate_entry = tk.Entry(self.root)

    self.click_delay_label = tk.Label(self.root, text="Click Delay (ms):")
    self.click_delay_entry = tk.Entry(self.root)

    self.start_button = tk.Button(self.root, text="Start", command=self.start_autoclicker)
    self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_autoclicker)

    self.click_rate_label.grid(row=0, column=0)
    self.click_rate_entry.grid(row=0, column=1)

    self.click_delay_label.grid(row=1, column=0)
    self.click_delay_entry.grid(row=1, column=1)

    self.start_button.grid(row=2, column=0)
    self.stop_button.grid(row=2, column=1)

    self.mouse = Controller()

    self.root.mainloop()

  def start_autoclicker(self):
    click_rate = int(self.click_rate_entry.get())
    click_delay = int(self.click_delay_entry.get())

    while True:
      self.mouse.click(Button.left)
      time.sleep(1 / click_rate)

  def stop_autoclicker(self):
    pass

if __name__ == "__main__":
  autoclicker = AutoClicker()