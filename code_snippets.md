## Show all data in output ##

```
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

```

## Disable need to scroll through output ##

```
from IPython.display import Javascript
display(Javascript('''google.colab.output.setIframeHeight(0, true, {maxHeight: 14821})'''))

```

## Mount and create subfolders, etc. ##

```
from google.colab import drive
drive.mount('/content/drive')

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

```

```
import os

if os.path.isdir('/content/drive/My Drive/Colab Notebooks/opensource_datasets/')==False:
  try:
    ! mkdir '/content/drive/My Drive/Colab Notebooks/opensource_datasets/'
  except e as Exception:
    pass  

os.chdir('/content/drive/My Drive/Colab Notebooks/opensource_datasets/' )

```

## ##
```
```
