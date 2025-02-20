import numpy as np
import matplotlib.pyplot as plt
import base64


fig, axis = plt.subplots(4, figsize=(10, 6))
fig.suptitle('Digital to Analog Conversion (MD.SAMIUL ALIM-180125)')
fig.tight_layout()

def compute_Unipolar_NRZ_Encoding(bits, N, bit_rate, T, Time):

  x = np.array([])
  for i in range(N):
    temp = bits[i]* np.ones((T))
    x = np.append(x, temp)
  t = np.linspace(0,N*Time,len(x))
  return [t, x]



bitsSize = 20
bits = np.random.random_integers(0,1,bitsSize)
Time = 10e-6   
bit_rate = 1/Time 
N = len(bits)   
T = 100
t,x = compute_Unipolar_NRZ_Encoding(bits, N, bit_rate, T, Time)
# x - Unipolar-NRZ encoded signal

axis[0].set_title("Unipolar-NRZ encoded signal")
axis[0].plot(t,x)


A = 8                       
fc1 =round(10*bit_rate)
fc2 =round(20*bit_rate)
tc = np.arange(0, Time, Time/T)
fsk_modulated_signal = np.array([])
for i in range(N):
  if bits[i] == 1:
    sig = A * np.sin(2.0 * np.pi * fc1 * tc)
    fsk_modulated_signal = np.append(fsk_modulated_signal, sig)
  else:
    sig = A * np.sin(2.0 * np.pi * fc2 * tc)
    fsk_modulated_signal = np.append(fsk_modulated_signal, sig)
  
# fsk_modulated_signal - FSK Modulated signal


axis[1].set_title("FSK Modulated signal")
axis[1].plot(t,fsk_modulated_signal)


# bits = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]) 
Time = 10e-6   
bit_rate = 1/Time 
N = len(bits)   
T = 100
t,x = compute_Unipolar_NRZ_Encoding(bits, N, bit_rate, T, Time)
# x - Unipolar-NRZ encoded signal

axis[2].set_title("Unipolar-NRZ encoded signal")
axis[2].plot(t,x)

A = 8                       
fc =round(10*bit_rate)
ph1 = 0
ph2 = np.pi
tc = np.arange(0, Time, Time/T)
psk_modulated_signal = np.array([])
for i in range(N):
  if bits[i] == 1:
    sig = A * np.sin((2.0 * np.pi * fc * tc) + ph1)
    psk_modulated_signal = np.append(psk_modulated_signal, sig)
  else:
    sig = A * np.sin((2.0 * np.pi * fc * tc) + ph2)
    psk_modulated_signal = np.append(psk_modulated_signal, sig)
  
# psk_modulated_signal - PSK Modulated signal


axis[3].set_title("PSK Modulated signal")
axis[3].plot(t,psk_modulated_signal)

plt.show()
