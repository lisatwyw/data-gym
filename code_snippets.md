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
