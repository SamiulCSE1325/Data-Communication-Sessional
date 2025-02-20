import numpy as np
import matplotlib.pyplot as plt
import base64




Ac=2; 
fc=2; 
t=np.arange(0, 3.0, 0.0001)
phase = 0
ct=Ac*np.sin(2*np.pi*fc*t + phase)


k = 1.0
fm=3
Am = 2
mt=Am*np.sin(2 * np.pi*fm*t)



yt=Ac*np.sin((2*np.pi*fc*t) + (k * mt + phase))

fig, axis = plt.subplots(3, figsize=(10, 6))
fig.suptitle('Analog to Analog Conversion (MD.SAMIUL ALIM-180125)')
fig.tight_layout()
axis[0].set_title("Carrier Signal")
axis[0].plot(t,ct)
axis[1].set_title("Message Signal")
axis[1].plot(t,mt)
axis[2].set_title("Phase modulated Signal")
axis[2].plot(t,yt)
plt.show()
