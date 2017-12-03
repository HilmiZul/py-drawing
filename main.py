from Tkinter import *

form = Tk()
lebar = "800"
tinggi = "400"
form.geometry((lebar+"x"+tinggi))
form.title("Menggambar")

kanvas = Canvas(form, width=lebar, height=tinggi, bg="#fff")
kanvas.pack()

# func. untuk membuat shape
def buat_lingkaran(koord, warna):
  kanvas.create_oval(koord, fill=warna)

def buat_persegi(koord, warna):
  kanvas.create_rectangle(koord, fill=warna)

# input koordinat dengan looping
# buat shape sebanyak sesuka hati :)
gambar = True
while gambar:
  print "[1] Lingkaran"
  print "[2] Persegi"
  pilih = input("Pilih nomor: ")

  if pilih == 1:
    koord = x1, y1, x2, y2 = input('X1: '), input('Y1: '), input('X2: '), input('Y2: ')
    warna = raw_input('Warna: ')
    buat_lingkaran(koord, warna)
  elif pilih == 2:
    koord = x1, y1, x2, y2 = input('X1: '), input('Y1: '), input('X2: '), input('Y2: ')
    warna = raw_input('Warna: ')
    buat_persegi(koord, warna)

  tanya = raw_input('Gambar lagi? [y/t] ')
  if tanya == 'y':
    gambar = True
  else:
    gambar = False
    print "Close kanvas untuk mengakhiri program"

form.mainloop()
