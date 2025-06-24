from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path

# Load the source PDF
reader = PdfReader("ROS1860.pdf")

# Page numbers are 0-indexed (e.g., page 5 is index 4)
page_number = int(input('Please enter page number: '))  
page_number -= 1  # Convert to 0-indexed for internal processing
# Create a writer and add the desired page
writer = PdfWriter()
writer.add_page(reader.pages[page_number])

# Save to a new PDF
file_name = f"page{page_number+1}.pdf"
with open(file_name, "wb") as f:
    writer.write(f)

# Convert PDF to list of PIL images (one per page)
image = convert_from_path(file_name, dpi=300)

image[0].save(f"page_{page_number+1}.png", "PNG")

