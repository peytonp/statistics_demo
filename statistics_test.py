import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
np.random.seed(100)
df = pd.DataFrame(np.random.randint(-10, 10, (10, 3)),
                  index=pd.date_range("1/1/2000", periods=10), columns=list("ABC"))
df = df.cumsum()
df.head()
df.plot()
plt.show()