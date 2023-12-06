import PyPDF2

pdfFileObj = open('../assets/pdfs/meetingminutes.pdf', "rb")
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.paper))
pageObj = pdfReader.pages[2]
page0Text = pageObj.extract_text()
print(page0Text)
pdfFileObj.close()