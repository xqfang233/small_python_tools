# Importing necessary libraries
# Note: These libraries need to be installed in the user's environment
# They are not installed in this environment, so the code is for demonstration purposes only

import ebooklib
from ebooklib import epub
from PIL import Image
from io import BytesIO
import os
from fpdf import FPDF
import re


class PDF(FPDF):
    def header(self):
        # You can add a header here if needed
        pass

    def footer(self):
        # And a footer here
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')



def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def epub_to_pdf(epub_path, pdf_path):
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=1, margin=15)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)

    image_tracker = set()

    # Process each item in the EPUB
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Add a new page for each chapter/document
            pdf.add_page()
            # Clean and add text to the PDF
            text = clean_html(item.get_body_content().decode('utf-8')).strip()
            pdf.multi_cell(0, 10, text)

        elif item.get_type() == ebooklib.ITEM_IMAGE:
            image_content = item.get_content()
            if image_content not in image_tracker:
                image_tracker.add(image_content)
                # Handle images - extract and add to PDF
                image = Image.open(BytesIO(image_content))
                image_path = "temp.jpg"
                image.save(image_path)
                pdf.image(image_path, x=None, y=None, w=0, h=0, type='', link='')
                os.remove(image_path)

    # Save the PDF file
    pdf.output(pdf_path)

# Example usage:
if __name__=='__main__':
    bookname ="the uncertainty solution how to invest with confid"
    epub_path = "C:/Users/xq/Downloads/the uncertainty solution how to invest with confid.epub"
    pdf_path = bookname + ".pdf"
    epub_to_pdf(epub_path, pdf_path)
