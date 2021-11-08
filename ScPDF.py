from PyPDF2 import PdfFileWriter , PdfFileReader


print(" _______                                _               ")
print("|__   __|                              | |              ")
print("   | | ___  __ _ _ __ ___     ___ _   _| |__   ___ _ __ ")
print("   | |/ _ \/ _` | '_ ` _ \   / __| | | | '_ \ / _ \ '__|")
print("   |_|\___|\__,_|_| |_| |_|  \___|\__, |_.__/ \___|_|   ")
print("                                   __/ |                ")
print("                                  |___/                 ")
print("          _                       _ _             ")
print("    /\   | |                     | (_)            ")
print("   /  \  | |  _ __ ___   __ _  __| |_ _ __   __ _ ")
print("  / /\ \ | | | '_ ` _ \ / _` |/ _` | | '_ \ / _` |")
print(" / ____ \| | | | | | | | (_| | (_| | | | | | (_| |")
print("/_/    \_\_| |_| |_| |_|\__,_|\__,_|_|_| |_|\__,_|")
print("                                                 ")
print("                                                 ")
print("                                                 ")
print("         create password on pdf file              ")
print("             enter file_name.PDF                  ")
print("        PDF file must be in same directory        ")
print("                                                 ")
print("                                                 ")


pdfname = input("Enter PDF name:")
try:
    out = PdfFileWriter()
    file = PdfFileReader(pdfname)
    num = file.numPages

    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)
except:
  print("The file name is incorrect or the file type is not a PDF")
  quit()
password = input("Enter password:")

out.encrypt(password)
with open("my PDF_sec.pdf" , "wb") as f :

    out.write(f)

print("done ! for create secure file : my PDF_sec.pdf")
