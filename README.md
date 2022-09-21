# Splitting

## Package that allows you to split documents into separate files for each page.

#### Requirements:

```
Python 3.8+
```
#### Instalation:
```
pip install -r requirements.txt
```

## Run instructions:

```python
from src.splitting.pdf import split as pdf_split
from src.splitting.excel import split as excel_split

# save destination is OPTIONAL (defaults to current location)

pdf_split('<PATH_TO_FILE>', dest='<SAVE_PATH>')
excel_split('<PATH_TO_FILE>', dest='<SAVE_PATH>')

```
NOTE: if the specified saving destination does not exist, the program will create the necessary directories.
