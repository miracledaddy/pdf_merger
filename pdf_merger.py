#importing modules\libraries
import PyPDF2
import sys
import os

#initializing empty list for collecting names of .pdf files
pdf_files_list = []
#createing object of PyPDF2 class with property to merge pdf files
merger = PyPDF2.PdfMerger()

#iterating over all files in the specified dir (current dir)
for file in os.listdir(os.curdir):
    #checking is the file .pdf or not
    if file.endswith(".pdf"):
        #adding a name of the .pdf file to list
        pdf_files_list.append(file)
        #adding .pdf file to the PyPDF2 object to be merged in one
        merger.append(file)

#creating new .pdf file with specified name consisting of all found pdf files in the current dir
merger.write("combined_docs.pdf")

print("\nWe have found such .pdf files in a current directory as:")

for file in pdf_files_list:
    print(file)

print("\nAnd merged them into the next file: combined_docs.pdf")
