import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/Rosendalsgatan/6.4 Ritningar/6.4.1 Arkitekt ritningar.pdf"
pages = 0
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"Rosendals_0{pages}.png")