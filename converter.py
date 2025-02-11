import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/Rosendalsgatan/Upphandlingsdokument/6.4 Ritningar/6.4.4 Akustik ritningar.pdf"
pages = 1
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"Rosen14_{pages}.png")