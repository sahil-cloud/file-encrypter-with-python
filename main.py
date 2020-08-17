from tkinter import *
from tkinter import filedialog,messagebox

root = Tk()
root.geometry('300x300')
root.title('encrypt/decrypt')

def encdec():
    f1 = filedialog.askopenfile(mode='r', filetype=[ ('png file', '*.png'),('jpg file', '*.jpg'), ('mp3 file', '*.mp3'), ('video file', '*.mp4'), ('mkv file', '*.mkv'), ('gif file', '*.gif')])
    if f1 is not None:
        # print(f1)
        image = f1.name
        # print(image)
        key = e.get()
        e.delete(0,END)
        fl = open(image,'rb')
        img = fl.read()
        fl.close()
        img = bytearray(img)
        for index,values in enumerate(img):
            img[index] = values^int(key)
        f11= open(image,'wb')
        f11.write(img)
        f11.close()
        messagebox.showinfo('Congratulations',"Process completed successfully")

b = Button(root,text="encrypt/decrypt",font="luicida 10 bold",command=encdec)
b.place(x=90,y=30)

e = Entry(root)
e.place(x=60,y=80)
e.config(show="*")

l = Label(root,text='Integer Key only',font='luicida 15 bold')
l.place(x=50,y=120)

root.mainloop()
