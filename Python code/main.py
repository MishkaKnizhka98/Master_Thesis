import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys, os

from matplotlib.widgets import Slider

os.listdir("C:/Users/Admin/Desktop/Master_Thesis/Mikhail_Bandurist_Transistors/Strasbourg_Samples")
os.listdir("Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023")
PATH = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/12_Sample12_device3_It_150kV_VDrain1V_VGate1V.csv"

df = pd.read_csv(PATH, header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df = df.rename(columns={"Time(ms)": "Time (s)", "Idrain(A)": "IDrain (A)"})
df["Time (s)"] /= 1000



selected_rows = df.loc[(df['Time (s)'] >= 704) & (df['Time (s)'] <= 729)]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
l, = ax.plot(selected_rows["Time (s)"], selected_rows["IDrain (A)"], lw=2)
income_ticks = [float(i) / 10000000000 for i in range(0, 20, 2)]
plt.yticks(income_ticks)

ax_slider = plt.axes(arg=[0.25, 0.2, 0.65, 0.03], facecolor = "lightgoldenrodyellow")
x_slider = Slider(ax_slider, label="X-shift", valmin=-100, valmax=100, valinit=0)

ay_slider = plt.axes(arg=[0.25, 0.1, 0.65, 0.03], facecolor = "lightgoldenrodyellow")
y_slider = Slider(ay_slider, label="Y-shift", valmin=-100/10000000000, valmax=100/10000000000, valinit=0)

def update(value):
    x_shift = x_slider.val
    y_shift = y_slider.val
    l.set_ydata(selected_rows["IDrain (A)"]+y_shift)
    l.set_xdata(selected_rows["Time (s)"]+x_shift)

    fig.canvas.draw_idle()

x_slider.on_changed(update)
y_slider.on_changed(update)

plt.show()



