from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *

mergewindow=Tk()
mergewindow.title('merge pdfs')
mergewindow.geometry('300x130')
                
e1=StringVar()
e2=StringVar()
e3=StringVar()
                
Label(mergewindow, text="pdf 1:").grid(row=0, column=0)
Label(mergewindow, text="pdf 2:").grid(row=1, column=0)
Label(mergewindow, text="output name:").grid(row=2, column=0)
                
ent1=Entry(mergewindow, textvariable=e1).grid(row=0, column=1)	
ent2=Entry(mergewindow, textvariable=e2).grid(row=1, column=1)
ent3=Entry(mergewindow, textvariable=e3).grid(row=2, column=1)
                
def do_merge():
        pdf_writer = PdfFileWriter()

        pdf_reader = PdfFileReader(e1.get())
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_reader = PdfFileReader(e2.get())
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(e3.get(), 'wb') as out:
            pdf_writer.write(out)

        mergewindow.destroy()
                        
Button(mergewindow, text='merge', command=do_merge).grid(row=3, column=1)
                                
mergewindow.mainloop()
