"""Update fields with a private, hidden Microsoft Word instance when available."""
from pathlib import Path
import sys

try:
    import pythoncom
    import win32com.client
except ImportError:
    print("Microsoft Word automation requires the optional pywin32 package.", file=sys.stderr)
    raise SystemExit(1)

pythoncom.CoInitialize()
word = None
document = None
try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    document = word.Documents.Open(str(Path(sys.argv[1]).resolve()), ReadOnly=False, AddToRecentFiles=False)
    document.Fields.Update()
    for toc in document.TablesOfContents:
        toc.Update()
    document.Repaginate()
    document.Save()
    print("Microsoft Word updated fields and repaginated the document.")
except Exception as exc:
    print(f"Microsoft Word update failed: {exc}", file=sys.stderr)
    raise SystemExit(1)
finally:
    if document is not None:
        document.Close(SaveChanges=False)
    if word is not None:
        word.Quit(SaveChanges=False)
    pythoncom.CoUninitialize()
