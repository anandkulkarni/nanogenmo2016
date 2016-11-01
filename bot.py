from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Command, NoEscape
import os

geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
doc = Document(geometry_options=geometry_options)

doc.preamble.append(Command('title', 'The Book of Meowmon'))
doc.preamble.append(Command('author', 'bot'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))



with doc.create(Section('Meow')):
	for i in range(1,50000):
   		doc.append('meow')

doc.generate_pdf('full', clean_tex=False)


