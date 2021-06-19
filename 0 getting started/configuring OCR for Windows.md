1 - download Tesseract for windows from https://github.com/UB-Mannheim/tesseract/wiki
either 
-   [tesseract-ocr-w32-setup-v5.0.0-alpha.20210506.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20210506.exe) (32 bit) and
-   [tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe) (64 bit) resp.

Install.

Add Tesseract to your system environmental variable 'path' (see for instance https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82) . This enables Windows to find the tessseract program whenever you'd enter the command 'tesseract' at the command prompt.

I've already added a user function to templater called 'ocr_win'. This is what is used to invoke tesseract from within Obsidian. the function is:

```
powershell tesseract "%ocr_input%" -
```

Inside the `_complex-templates` folder is the windows OCR template, called `ocr-win`. It differ from the Mac script (which is just called 'ocr')  where it creates the variable 'ocr-input' from the user's file selection. Because Macs create file paths with forward slashs `/` and Windows create file paths with back slashes `\`, there's a little find-and-replace done inside the variable to fix that. 

So - you don't have to do anything other than install Tesseract for Windows, and make sure it's in your system environmental variable `path`. You can double check once you've set that by opening a command prompt (type `cmd` in the address bar in your file explorer) and typing in `tesseract --version`. If there's a problem, Windows will tell you command not found.


