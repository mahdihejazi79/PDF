from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *

splitwindow=Tk()
splitwindow.title('split pdf')
splitwindow.geometry('300x130')
	
e1=StringVar()
e2=IntVar()
e3=IntVar()
	
Label(splitwindow, text="path:").grid(row=0, column=0)
Label(splitwindow, text="start:").grid(row=1, column=0)
Label(splitwindow, text="end:").grid(row=2, column=0)
	
ent1=Entry(splitwindow, textvariable=e1).grid(row=0, column=1)	
ent2=Entry(splitwindow, textvariable=e2).grid(row=1, column=1)
ent3=Entry(splitwindow, textvariable=e3).grid(row=2, column=1)
	
def do_split():
	pdf = PdfFileReader(e1.get())
	pdf_writer = PdfFileWriter()
		
	for page in range(e2.get()-1,e3.get()):
		pdf_writer.addPage(pdf.getPage(page))

	output = f'{e2.get()}_{e3.get()}.pdf'
	with open(output, 'wb') as output_pdf:
		pdf_writer.write(output_pdf)
			
	splitwindow.destroy()
		
Button(splitwindow, text='split', command=do_split).grid(row=3, column=1)
			
splitwindow.mainloop()
