from PyPDF2 import PdfFileReader, PdfFileWriter

def split():
	print('enter path')
	path=input()
	print('enter start')
	from_page=int(input())
	print('enter end')
	to_page=int(input())
	
	pdf = PdfFileReader(path)
	pdf_writer = PdfFileWriter()
	
	for page in range(from_page-1,to_page):
		pdf_writer.addPage(pdf.getPage(page))

	output = f'{from_page}_{to_page}.pdf'
	with open(output, 'wb') as output_pdf:
		pdf_writer.write(output_pdf)
		
def merge_pdfs():
	pdf_writer = PdfFileWriter()
	
	print('enter paths')
	paths=[str(path) for path in input().split()]
	print('enter name of merge_file if you want else push enter')
	output=input()
	if output=='':
		first=1
		for path in paths:
			if first:
				output+=path[:-4]
				first=0
			else:
				output+='+'+path[:-4]
		output+='.pdf'
	for path in paths:
		pdf_reader = PdfFileReader(path)
		for page in range(pdf_reader.getNumPages()):
			pdf_writer.addPage(pdf_reader.getPage(page))

	with open(output, 'wb') as out:
		pdf_writer.write(out)
	
while True:
	print('enter your choice')
	print('1.split pdf')
	print('2.merge pdfs')
	print('3.exit\n')
	
	choice=input()
	if choice=='1':
		split()
	elif choice=='2':
		merge_pdfs()
	elif choice=='3':
		break
	else:
		print('enter correct number\n')
