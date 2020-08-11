
```
SEED=1234

import numpy as np; np.random.seed(SEED); np.random.RandomState(SEED)
import random as rn; rn.seed(SEED)
import tensorflow as tf

try:
    tf.set_random_seed(SEED)
except:
    tf.random.set_seed(SEED)

import os; os.environ['PYTHONHASHSEED']=str(SEED)

# ...

model.add(Dropout(0.25, seed=seed_value))



```

