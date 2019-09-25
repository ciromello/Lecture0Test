exercise 13_2 

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:38:02 2019

@author: cmello
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:22:50 2019

@author: cmello
"""

import os

from PyPDF2 import PdfFileReader, PdfFileWriter

path = "C:/Users/cmello/Documents/" \
"Python Basics Book Dan Bader/" \
"exercises_chapter_13/"

input_file_path = os.path.join(path, "output/Walrus.pdf")
input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()


# Decrypt the PDF file
input_pdf.decrypt("IamtheWalrus")  # without this, I get an error message.

# 2
num_pages = input_pdf.getNumPages()
for n in range(0, num_pages):
	page = input_pdf.getPage(n)
	page.rotateClockwise(270)
	output_pdf.addPage(page)

output_file_path = os.path.join(path, "output/Walrus Rotated2.pdf")

with open(output_file_path, "wb") as output_file:
	output_pdf.write(output_file)



"""
CIRO START FROM STEP # 3
import copy

from PyPDF2 import PdfFileReader, PdfFileWriter

import os

path = "C:/Users/cmello/Documents/" \
"Python Basics Book Dan Bader/" \
"exercises_chapter_13/output/Walrus Rotated.pdf"

input_pdf = PdfFileReader(path)

input_pdf.decrypt("IamtheWalrus")

page.mediaBox

"""


# 3 

path2 = "C:/Users/cmello/Documents/" \
"Python Basics Book Dan Bader/" \
"exercises_chapter_13/Output/"

input_file_path2 = os.path.join(path2, "Walrus Rotated2.pdf")
input2_pdf = PdfFileReader(input_file_path2)
output2_pdf = PdfFileWriter()


#input_file_path2.decrypt("IamtheWalrus")
#input2_pdf.decrypt("IamtheWalrus")


for page_num in range(0, input2_pdf.getNumPages()):
	page_left = input2_pdf.getPage(page_num)
	page_right = copy.copy(page_left)
	# Calculate the new coordinates for the upper-right
	# corner of the page_left and the upper-left
	# corner of page_right
	upper_right = page_left.mediaBox.upperRight
	new_coords = (upper_right[0]/2, upper_right[1])
	# Crop and add left-side page to the ouput file
	page_left.mediaBox.upperRight = new_coords
	output2_pdf.addPage(page_left)
	# Crop and add right-side page to the output file
	page_right.mediaBox.upperLeft = new_coords
	output2_pdf.addPage(page_right)

# 4

output_file_path2 = os.path.join(path2, "Walrus_exercise13_.pdf")

with open(output_file_path2, "wb") as output_file:
	output2_pdf.write(output_file)
