import tkinter as tk
from tkinter import Canvas
import time
import math

# إعداد النافذة
window = tk.Tk()
window.title("Analog Clock")
window.geometry("400x400")
window.configure(bg="#FFC196")

# إعداد اللوحة
canvas = Canvas(window, width=400, height=400, bg="#DFCFBE", highlightthickness=0)
canvas.pack()

# رسم الإطار الخارجي للساعة
canvas.create_oval(50, 50, 350, 350, width=2, outline="#939597", fill="#FFFAF0")

# رسم الأرقام
for i in range(1, 13):
    angle = math.radians(i * 30 - 90)
    x = 200 + 130 * math.cos(angle)
    y = 200 + 130 * math.sin(angle)
    canvas.create_text(x, y, text=str(i), font=("Arial", 16, "bold"), fill="black")

# تحديث عقارب الساعة
def update_clock():
    canvas.delete("hands")
    now = time.localtime()
    hours = now.tm_hour % 12
    minutes = now.tm_min
    seconds = now.tm_sec

    # عقرب الساعات
    hour_angle = math.radians(hours * 30 - 90 + minutes * 0.5)
    hour_x = 200 + 80 * math.cos(hour_angle)
    hour_y = 200 + 80 * math.sin(hour_angle)
    canvas.create_line(200, 200, hour_x, hour_y, width=6, fill="black", tag="hands")

    # عقرب الدقائق
    minute_angle = math.radians(minutes * 6 - 90)
    minute_x = 200 + 110 * math.cos(minute_angle)
    minute_y = 200 + 110 * math.sin(minute_angle)
    canvas.create_line(200, 200, minute_x, minute_y, width=4, fill="gray", tag="hands")

    # عقرب الثواني
    second_angle = math.radians(seconds * 6 - 90)
    second_x = 200 + 120 * math.cos(second_angle)
    second_y = 200 + 120 * math.sin(second_angle)
    canvas.create_line(200, 200, second_x, second_y, width=2, fill="black", tag="hands")

    window.after(1000, update_clock)

# تشغيل الساعة
update_clock()
window.mainloop()