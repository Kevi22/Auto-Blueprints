import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/Jenningsskolan/bilagor/12_Ritningar/12.2 Arkitektriningar enligt förteckning/A-43-6-001.pdf"
pages = 0
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"A-43-6-001{pages}.png")