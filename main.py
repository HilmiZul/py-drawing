from Tkinter import *

form = Tk()
lebar = "800"
tinggi = "400"
form.geometry((lebar+"x"+tinggi))
form.title("Menggambar")

kanvas = Canvas(form, width=lebar, height=tinggi, bg="#fff")
kanvas.pack()


# input koordinat
x1 = input('X1: ')
y1 = input('Y1: ')
x2 = input('X2: ')
y2 = input('Y2: ')
warna = raw_input('Warna: ')

kanvas.create_rectangle((x1, y1, x2, y2), fill=warna)

form.mainloop()
