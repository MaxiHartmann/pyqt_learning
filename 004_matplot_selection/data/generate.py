import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 1000)

f = 2
y = np.sin(f * x * 2 * np.pi)
y += 0.1 * np.sin(2 * f * x * 2 * np.pi)
y += 0.4 * np.sin(3 * f * x * 2 * np.pi)


if __name__ == "__main__":

    df = pd.DataFrame({"x": x, "y": y})
    df.to_csv("sinus.csv", float_format='%.5f', index=False)

    plt.plot(x, y)
    plt.show()
