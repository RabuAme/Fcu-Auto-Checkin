# Fcu-Auto-Checkin
I'm a beginner of coding, and this is my first program.

If there are any bugs there, please tell me.

## Prerequisites  
  
 - Python3 ([Download](https://www.python.org/downloads/))
 - Chromedriver(Please download the correct version of your Chrome) ([Download](https://chromedriver.chromium.org/downloads))
 - Tesseract-OCR ([Download](https://github.com/UB-Mannheim/tesseract/wiki))

## Myconstants.py
 - **NID:**  
Your NID number
 - **Password:**  
Your FCU Password
 - **Tesseract:**  
Your Tesseract-ocr path

## Run the script
 1. Edit [Myconstants.py](Myconstants.py)
 2. First way: Install dependencies: `pip install -r requirements.txt` , Second way: Run [pip.bat](pip.bat)
 3. First way: Run [FCU.py](FCU.py): `python FCU.py` , Second way: Run [FCU.bat](FCU.bat)

## Export to exe
 1. Edit [Myconstants.py](Myconstants.py)
 2. First way: Install dependencies: `pip install -r requirements.txt` , Second way: Run [pip.bat](pip.bat)
 3. Run [toEXE.bat](toEXE.bat)
 4. Move FCU.exe from dist to main folder(with chromedriver)
 5. Run FCU.exe
 6. You can delete folder _pycache_ , build and file FCU.spec after all
