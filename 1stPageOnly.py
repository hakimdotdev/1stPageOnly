import os
import PyPDF2 as pdf

def entferne_seiten(pdfdatei):
    pdf_reader = pdf.PdfFileReader(pdfdatei, strict=False)
    pdf_writer = pdf.PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(0))
    with open(pdfdatei, 'wb') as out_file:
        pdf_writer.write(out_file)

def durchsuche_verzeichnis(verzeichnis):
    for datei in os.listdir(verzeichnis):
        if datei.endswith('.pdf'):
            entferne_seiten(os.path.join(verzeichnis, datei))
        elif os.path.isdir(os.path.join(verzeichnis, datei)):
            durchsuche_verzeichnis(os.path.join(verzeichnis, datei))

def hauptfunktion():
    aktuelles_verzeichnis = os.getcwd()
    for datei in os.listdir(aktuelles_verzeichnis):
        if datei.endswith('.pdf'):
            entferne_seiten(os.path.join(aktuelles_verzeichnis, datei))
        elif os.path.isdir(os.path.join(aktuelles_verzeichnis, datei)):
            durchsuche_verzeichnis(os.path.join(aktuelles_verzeichnis, datei))

hauptfunktion()
