import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0, 1, 30)
noise = np.random.normal(1, 0.1, 30)

### Probe 1
y = np.sin(2 * np.pi * x) 
df = pd.DataFrame({"x": x, "y": y})
df_noise = pd.DataFrame({"x": x, "y": y * noise})

df.to_csv("./data_1/probe1.csv", index=False)
df_noise.to_csv("./data_2/probe1.csv", index=False)

### Probe 2
y = np.sin(2 * np.pi * x) + 2
df = pd.DataFrame({"x": x, "y": y})
df_noise = pd.DataFrame({"x": x, "y": y * noise})

df.to_csv("./data_1/probe2.csv", index=False)
df_noise.to_csv("./data_2/probe2.csv", index=False)

### Probe 3
y = 3 * np.sin(2 * np.pi * x) + 2
df = pd.DataFrame({"x": x, "y": y})
df_noise = pd.DataFrame({"x": x, "y": y * noise})

df.to_csv("./data_1/probe3.csv", index=False)
df_noise.to_csv("./data_2/probe3.csv", index=False)
