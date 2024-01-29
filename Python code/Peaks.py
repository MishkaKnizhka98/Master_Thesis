import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys, os
from matplotlib.widgets import Slider

os.listdir("Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023")

PATH = [None] * 13
PATH[0] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/12_Sample12_device3_It_150kV_VDrain1V_VGate1V.csv"
PATH[1] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/14_Sample12_device3_It_150kV_VDrain1V_VGate2V.csv"
PATH[2] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/16_Sample12_device3_It_150kV_VDrain1V_VGate3V.csv"
PATH[3] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/18_Sample12_device3_It_150kV_VDrain1V_VGate5V.csv"
PATH[4] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/20_Sample12_device3_It_150kV_VDrain1V_VGate10V.csv"
PATH[5] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/22_Sample12_device3_It_150kV_VDrain1V_VGate15V.csv"
PATH[6] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/24_Sample12_device3_It_150kV_VDrain1V_VGate20V.csv"
PATH[7] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/26_Sample12_device3_It_150kV_VDrain1V_VGate25V.csv"
PATH[8] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/28_Sample12_device3_It_150kV_VDrain1V_VGate30V.csv"
PATH[9] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/30_Sample12_device3_It_150kV_VDrain1V_VGate35V.csv"
PATH[10] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/32_Sample12_device3_It_150kV_VDrain1V_VGate40V.csv"
PATH[11] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/34_Sample12_device3_It_150kV_VDrain1V_VGate45V.csv"
PATH[12] = "Mikhail_Bandurist_Transistors/Strasbourg_Samples/Sample12_device3_15122023/36_Sample12_device3_It_150kV_VDrain1V_VGate50V.csv"

df = [None]*13
df[0] = pd.read_csv(PATH[0], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[1] = pd.read_csv(PATH[1], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[2] = pd.read_csv(PATH[2], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[3] = pd.read_csv(PATH[3], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[4] = pd.read_csv(PATH[4], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[5] = pd.read_csv(PATH[5], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[6] = pd.read_csv(PATH[6], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[7] = pd.read_csv(PATH[7], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[8] = pd.read_csv(PATH[8], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[9] = pd.read_csv(PATH[9], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[10] = pd.read_csv(PATH[10], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[11] = pd.read_csv(PATH[11], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])
df[12] = pd.read_csv(PATH[12], header=10, delimiter=";", usecols=["Time(ms)", "Idrain(A)"])

for i in range(len(df)):
    df[i] = df[i].rename(columns={"Time(ms)": "Time (s)", "Idrain(A)": "IDrain (A)"})
    df[i]["Time (s)"] /= 1000

peak_df = [None] * 13
for i in range(10):
    peak_df[i] = df[i].loc[(df[i]['Time (s)'] >= 704) & (df[i]['Time (s)'] <= 729)]
    peak_df[i]["IDrain (A)"] -= peak_df[i]["IDrain (A)"].iloc[0]

for i in range(10, 12):
    peak_df[i] = df[i].loc[(df[i]['Time (s)'] >= 804) & (df[i]['Time (s)'] <= 829)]
    peak_df[i]["Time (s)"] -= 100
    peak_df[i]["IDrain (A)"] -= peak_df[i]["IDrain (A)"].iloc[0]

peak_df[12] = df[12].loc[(df[12]['Time (s)'] >= 824) & (df[i]['Time (s)'] <= 844)]
peak_df[12]["Time (s)"] -= 100
peak_df[12]["IDrain (A)"] -= peak_df[12]["IDrain (A)"].iloc[0]

VGate_list = [1,2,3,5,10,15,20,25,30,35,40,45,50]
delta_h = 0.05

fig, ax = plt.subplots(figsize=(10, 20))
plt.subplots_adjust(bottom=0.1)
plt.title("Peak evolution through VGate", fontsize=30)
income_ticks = [float(i) / 1000000000 for i in range(0, 11, 1)]
plt.yticks(income_ticks, fontsize=15)
plt.xticks(fontsize=15)
plt.xlabel("Time (s)", fontsize=20)
plt.ylabel("IDrain (A)", fontsize=20)
ax.set_ylim([0, 5/1000000000])
ax.set_xlim([700, 800])

y_pos = 0.1
x_slider = [None]*13
y_slider = [None]*13
l = [None]*13
for i in range(13):
    l[i], = ax.plot(peak_df[i]["Time (s)"], peak_df[i]["IDrain (A)"], lw=2, label = "VGate = "+str(VGate_list[i])+"V")
    plt.legend(loc="upper right")

fig_1, ax_1 = plt.subplots(figsize=(5, 10))
for i in range(13):
    ax_slider = plt.axes(arg=[0.1, y_pos, 0.65, 0.01], facecolor="lightgoldenrodyellow")
    x_slider[i] = Slider(ax_slider, label="X-shift_" + str(VGate_list[i]) + "V", valmin=-100, valmax=100, valinit=0)

    ay_slider = plt.axes(arg=[0.1, y_pos+0.015, 0.65, 0.01], facecolor="lightgoldenrodyellow")
    y_slider[i] = Slider(ay_slider, label="Y-shift" + str(VGate_list[i]) + "V", valmin=-100 / 10000000000, valmax=100 / 10000000000, valinit=0)
    y_pos += delta_h

def update(value):
    x_shift = [None]*13
    y_shift = [None]*13
    for i in range(13):
        x_shift[i] = x_slider[i].val
        y_shift[i] = y_slider[i].val
        l[i].set_ydata(peak_df[i]["IDrain (A)"]+y_shift[i])
        l[i].set_xdata(peak_df[i]["Time (s)"]+x_shift[i])

    fig.canvas.draw_idle()

for i in range(13):
    x_slider[i].on_changed(update)
    y_slider[i].on_changed(update)


plt.show()