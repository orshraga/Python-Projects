import numpy as np
import matplotlib.pyplot as plt

# Parameters
amplitude = 1.0
frequency = 1000.0  # Frequency of the square wave
modulation_index = 5.0  # Modulation index for FM

# Time settings
sampling_rate = 10000  # Number of samples per second
duration = 1.0  # Duration of the signal in seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the carrier wave
carrier_wave = amplitude * np.cos(2 * np.pi * frequency * t)

# Generate the modulation signal (square wave)
modulation_signal = np.sign(np.sin(2 * np.pi * frequency * t))

# Generate the modulated signal
modulated_signal = amplitude * np.cos(2 * np.pi * (frequency + modulation_index * modulation_signal) * t)

# Plot the signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, carrier_wave)
plt.title('Carrier Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.plot(t, modulation_signal)
plt.title('Modulation Signal (Square Wave)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)
plt.title('Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Display the plot
plt.tight_layout()
plt.show()
