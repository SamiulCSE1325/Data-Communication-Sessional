import numpy as np
import matplotlib.pyplot as plt
import base64



# Digital data
digitalDataSize = 20
digitalData = np.random.random_integers(0,1,digitalDataSize)
print(digitalData)

time_of_view        = 1.
analog_time         = np.linspace (0, time_of_view, int(10e5))

sampling_rate       = digitalDataSize
sampling_period     = 1. / sampling_rate
sample_number       = time_of_view / sampling_period
sampling_time       = np.linspace (0, time_of_view, int(sample_number))

carrier_frequency   = 9.
amplitude           = 1
phase               = 0

quantizing_bits     = 4
quantizing_levels   = 2 ** quantizing_bits / 2
quantizing_step     = 1. / quantizing_levels

def analog_signal (time_point):
    time_point_len = len(time_point)//digitalDataSize
    data = []
    if time_point_len <= 1:
        data = np.ones(digitalDataSize)
        for x in range(digitalDataSize):
            if digitalData[x] == 0:
                data[x] = -1
    else:
        data = np.array([1])
        for x in digitalData:
            if x == 1:
                data = np.concatenate((data, np.ones(time_point_len)),axis=0)
            else:
                data = np.concatenate((data, -1*np.ones(time_point_len)),axis=0)
        data = np.delete(data, 0)
    return data
sampling_signal     = analog_signal (sampling_time)
quantizing_signal   = np.round (sampling_signal / quantizing_step) * quantizing_step


fig = plt.figure ()
plt.plot (analog_time,   analog_signal (analog_time) )
plt.stem (sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
plt.title("digital data to digital signal conversion (MD.SAMIUL ALIM-180125)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()