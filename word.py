# from docx import Document

# # Open the document
# document = Document('document.docx')

# # Add a new paragraph to the document
# paragraph = document.add_paragraph()

# # Insert the image
# paragraph.add_run().add_picture('instagram.png')

# # Save the document
# document.save('new_document.docx')
# from docx import Document
# from docx.shared import Inches

# # Open the document
# document = Document('new_document.docx')

# # Find the image in the document
# for paragraph in document.paragraphs:
#     for run in paragraph.runs:
#         # print(run.style.name)
#         if 'Default Paragraph Font' in run.style.name:
#             # Get the image object
#             for x in range(20):
#                 image = run.add_picture('instagram.png')
            
#             # Set the width and height of the image
#             image.width = Inches(1)
#             image.height = Inches(0.5)

# # Save the document
# document.save('new_document.docx')

# from docx import Document

# # Open the document
# document = Document('document.docx')

# # Search for the paragraph with the specified text
# paragraph = document.find('Petar')

# # Print the paragraph's text
# print(paragraph.text)

# from docx import Document
# from docx.shared import Inches

# # Open the document
# document = Document('document.docx')

# # Add a new paragraph to the document
# document.add_heading("Petar", 0)
# paragraph = document.add_paragraph("samo test")

# # Insert the image and set its size
# # for x in range(50):
# #     run = paragraph.add_run()
# #     image = run.add_picture('instagram.png')
# #     image.width = Inches(0.7)
# #     image.height = Inches(0.4)

# # Save the document
# document.save('new_document.docx')

# from docx import Document
# from docx.shared import Inches

# # Create a new document
# document = Document()
# paragraph = document.add_paragraph()
# for x in range(50):
#     run = paragraph.add_run()
#     image = run.add_picture('instagram.png')
#     image.width = Inches(0.7)
#     image.height = Inches(0.4)

# document.save('testy.docx')