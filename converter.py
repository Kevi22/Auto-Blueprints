import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/hbg/06 Projektering 6/Handlingar och textdokument/SK/Ritningar/SK-46-1-2001112.pdf"
pages = 0
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"H--SK-46-1-2001112{pages}.png")