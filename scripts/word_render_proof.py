"""Render a DOCX to PDF in a private Word instance for visual QA."""
from pathlib import Path
import sys

import pythoncom
import win32com.client

pythoncom.CoInitialize()
word = None
document = None
try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    document = word.Documents.Open(str(Path(sys.argv[1]).resolve()), ReadOnly=True, AddToRecentFiles=False)
    document.ExportAsFixedFormat(str(Path(sys.argv[2]).resolve()), 17)
    print("Word proof PDF created.")
finally:
    if document is not None:
        document.Close(SaveChanges=False)
    if word is not None:
        word.Quit(SaveChanges=False)
    pythoncom.CoUninitialize()
