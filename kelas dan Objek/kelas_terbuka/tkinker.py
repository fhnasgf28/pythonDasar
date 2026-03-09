import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text='label1')
label2 = tkinter.Label(main_window, text='label2')

tombol1 = tkinter.Button(main_window, text='tombol1')
tombol2 = tkinter.Button(main_window, text='tombol2')

# mehtod positioning

label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

main_window.mainloop()
