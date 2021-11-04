import PyPDF2
import pyttsx3

# path to your pdf file
pdf_file = "files/the_pdf.pdf"

def making_text(pdf_path):
    with open("files/the_pdf.pdf", "rb") as f:
        pdf=PyPDF2.PdfFileReader(f)
        pages=pdf.numPages
        pageobj=pdf.getPage(pages-1)
        text=pageobj.extractText()
    extract = []
    for i in text:
        if i == "\n":
            pass
        else:
            extract.append(i)
    result = "".join(extract)
    return result

# it's additional code for make the text to txt file but i'm not do it becuase it's not necessary :)
# with open("files/text.txt", "w") as txt:
#     txt.writelines(result)

# with open("files/text.txt", "r") as txt:
#     text = txt.read()

# convert to audiobook
text = making_text(pdf_file)
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()