from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os
app = Tk()

app.geometry('500x500+400+100')
app.resizable(False , False)
app.title('PDF Reader')
app.iconbitmap('pdf.ico')
app.config(background = 'white')

def view():
    file_name = filedialog.askopenfilename(initialdir = os.getcwd(),
                                           title = 'Select PDF',
                                           filetype = [('Select files','.pdf'),
                                                       ('Select files','.PDF'),
                                                       ('Select files','.txt')
                                                       ]
                                           )
    p = pdf.ShowPdf()
    show = p.pdf_view(app , pdf_location = open(file_name,"r"),width = 500 , height = 500)
    show.pack(pady=(0,0))

b1 = Button(app , text = 'Open PDF File' , fg = 'white' , bg = 'red' , command = view)
b1.pack(fill = X)



app.mainloop()