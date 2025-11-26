from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.shared import Inches, Pt, Cm
from Util.header_wrap import add_header_image_and_wrap
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml.ns import qn

def generate_docx(filename):
    doc = Document()

    # create header (centered)
    section = doc.sections[0]
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(3.17)
    section.right_margin = Cm(3.17) 
    header = section.header

    if header:
        add_header_image_and_wrap(
            header,
            "./Resource/Header Logo Komdigi Dit IPD.png",
            pos_x_pt=10,
            pos_y_pt=10
        )

    doc.save(filename)


generate_docx("Test_Document.docx")