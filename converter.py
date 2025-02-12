import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/Kofferdalsvägen /6.4 Ritningar/6.4 Ritningar/6.4.4 Rör/V-52-11.pdf"
pages = 0
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"kofferdals_1.1{pages}.png")