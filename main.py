import tkinter.messagebox as tm
import tkinter

from module import kalkulasi_persamaan

def show():
    tm.showinfo(title="Hasil", message=kalkulasi_persamaan.kalkukasi_turunan(persamaan.get(), berapa_kali.get()))
    
root = tkinter.Tk()

tkinter.Label(root, text="Persamaan: ").grid(row=0)
tkinter.Label(root, text="Berapa Turunan: ").grid(row=1)

persamaan = tkinter.Entry(root)
berapa_kali = tkinter.Entry(root)

persamaan.grid(row=0, column=1)
berapa_kali.grid(row=1, column=1)

tkinter.Button(root, text="Tampilkan", command=show).grid(row=3, column=1)
               
tkinter.mainloop()