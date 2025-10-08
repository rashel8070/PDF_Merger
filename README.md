#PDF Merger Tool

A simple Python script that merges all PDF files in the current directory into a single output PDF using the PyPDF2 library.

Features
Automatically discovers and merges all .pdf files in the working directory.

Excludes the output file itself to prevent duplication.

Lightweight and easy to run.

Pure Python solution with no external dependencies beyond PyPDF2.

Prerequisites
Python 3.7 or higher

PyPDF2

Install PyPDF2 with pip:

bash
pip install PyPDF2
Usage
Clone the repository (or download the script):

bash
git clone https://github.com/yourusername/pdf-merger.git
cd pdf-merger
Place your PDF files in the repository directory.

Run the merger script:

bash
python main.py
This will produce a file named Merged.pdf in the same directory.
