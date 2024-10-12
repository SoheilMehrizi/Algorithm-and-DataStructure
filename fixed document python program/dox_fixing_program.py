#fix reversed date 
damaged_file_address = input("please Enter the adress of Damaged file:\n")
from docx import Document 

numbersdone = 0 
doc = Document(damaged_file_address)

for para in doc.paragraphs:
    newtxt = ''
    for char in para.text:
        if char in "1234567890":
            if numbersdone == 0:
                numbersdone += 1
            
            newtxt = newtxt[:-1*numbersdone] + char + newtxt[-1*numbersdone:]
            numbersdone += 1
        else:
            newtxt += char
            numbersdone = 0         
    para.text = newtxt
doc.save(
    input("give me the address to save fixed doc")+"fixeddoc.docx"
)
