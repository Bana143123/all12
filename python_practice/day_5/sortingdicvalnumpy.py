import numpy as np
import pandas as pd
d={"abc":["Narendra","reddy","kumar"],"age":[20,24,25],"city":["Bng","hyd","chennai"]
}
df=pd.DataFrame(d)
a=np.array(df["city"])
sorte=np.argsort(a)
sortedval=df.iloc[sorte]
print(sortedval)

