# General #
```
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))
```

# Percent of missing values
```
train.isnull().sum(axis=0)/len(train.index) * 100
```


# Dataframe #

```
names = pd.read_excel( 'names.xlsx' )

names.loc[lambda df: df['Last name'].str.replace(' ', '').str.upper()  == ln.upper() ]                

```

# Plotting #

```
fig,axes=plt.subplots(1,1, figsize=(  W,H ));
```

# JupyterHub #
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



# Specific to  Google Colab ##

## Mount and create subfolders, etc. ##

```
from google.colab import drive
drive.mount('/content/drive', force_remount=False )

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
