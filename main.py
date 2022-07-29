import tkinter as tk


def toggle_eyes():
    current_color = c.itemcget(left_eye, 'fill')
    if current_color == 'white':
        new_color = '#1E96D5'
    else:
        new_color = 'white'
    c.itemconfigure(left_eye, fill = new_color)
    c.itemconfigure(right_eye, fill = new_color)

def blink():
    toggle_eyes()
    window.after(1000, blink)


# create a stand alone window
window = tk.Tk()
# create a canvas
c = tk.Canvas(master=window, bg='black', width=800, height=600)
face = c.create_oval(200, 115, 600, 490, fill='#1E96D5', outline='#1E96D5')
left_eye = c.create_oval(305, 150, 400, 270, fill='white', outline='black', width=2)
#left_eye_pupil = c.create_oval(365, 220, 390, 245, fill='black', outline='black')
right_eye = c.create_oval(400, 150, 495, 270, fill='white', outline='black', width=2)
#right_eye_pupil = c.create_oval(410, 220, 435, 245, fill='black', outline='black')
c.pack(fill=tk.BOTH, expand=True)
#schedule a call after said time passes
window.after(2000, blink)
#keep the window alive and destory on explict close
window.mainloop()