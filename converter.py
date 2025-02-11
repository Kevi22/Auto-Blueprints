import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "data_lake/blueprints/Rosendalsgatan_ny_förskola_totalentreprenad/Upphandlingsdokument/6.3 Beskrivningar/6.3.5 Rambeskrivning El- och telesystem.pdf"
pages = 76
doc = fitz.open(file_path)  # open document
page = doc[pages]
pix = page.get_pixmap()  # render page to an image
pix.save(f"Blåsväder10_{pages}.png")