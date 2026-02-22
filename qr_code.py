from pyqrcode import create
import tkinter as tk
from tkinter import colorchooser



root = tk.Tk()
root.title("QR Code Generator")
data = tk.Entry(root, font = ("Segoe UI", 12), width=30, relief="sunken", bd=2)
root.iconbitmap(r"d://kivy//qrcodegen//icon.ico")

my_color = (None,"White")


def color():
    global my_color
    my_color = colorchooser.askcolor()




color_button = tk.Button(root, text="Choose Color", font= ("Segoe UI", 12), command=color, bg="#3B8FC7", fg="white", relief="ridge", activebackground="#496BC7", cursor="hand2", activeforeground="white")





def gen_qr():
    global dta
    dta = data.get()
    if dta == "":
        statement.config(text="Please enter some text to generate QR Code")
        return
    
    dta = create(dta)
    test = dta.xbm(scale=5)
    global xbm_image
    if not my_color or not my_color[0]:
        bg_color = "white"
        fg_color = "black"
    else:
        bg_color = my_color[1]
        rgb = my_color[0]

        brightness = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])
        fg_color = "white" if brightness < 128 else "black"

    xbm_image = tk.BitmapImage(
        data=test,
        background=bg_color,
        foreground=fg_color
    )
    image_view.config(image=xbm_image)
    statement.config(text="QR Code Generated!")


heading = tk.Label(root, text="QR COde Generator", font = ("Segoe UI", 40, "bold"))
subtitle = tk.Label(root, text="Enter the text for your QR", font = ("Segoe UI", 14))

make_button = tk.Button(root, text="Generate QR" , font= ("Segoe UI", 12, "bold"), bg="#4CAF50",
    fg="white",relief= "raised", activebackground="#43A047", cursor="hand2",
    activeforeground="white",command=gen_qr)

image_view = tk.Label(root)
statement = tk.Label(root)



#grid

heading.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

subtitle.grid(row=1, column=0, sticky="e", padx=5, pady=8)
data.grid(row=1, column=1, sticky="w", padx=10, pady=8)

make_button.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10, pady=10)

color_button.grid(row=3, column=0, columnspan=2, pady=5)

image_view.grid(row=4, column=0, columnspan=2, pady=15)

statement.grid(row=5, column=0, columnspan=2, pady=(5,20))

root.mainloop()
