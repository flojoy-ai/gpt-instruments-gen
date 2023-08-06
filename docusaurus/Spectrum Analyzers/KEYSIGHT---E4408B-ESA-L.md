
# KEYSIGHT - E4408B ESA-L

## Instrument Card

E4408B ESA-L Basic Spectrum Analyzer, 9 kHz to 26.5 GHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT - E4408B ESA-L in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.agilent import AgilentE4408B

# Create a VISA adapter for the instrument
adapter = VISAAdapter("TCPIP::192.168.1.1::INSTR")  # Replace with the actual IP address of the instrument

# Connect to the instrument
instrument = AgilentE4408B(adapter)

# Set the start and stop frequencies
instrument.start_frequency = 1e9  # 1 GHz
instrument.stop_frequency = 2e9  # 2 GHz

# Set the number of frequency points
instrument.frequency_points = 101

# Set the frequency step
instrument.frequency_step = 1e6  # 1 MHz

# Set the center frequency
instrument.center_frequency = 1.5e9  # 1.5 GHz

# Set the sweep time
instrument.sweep_time = 0.1  # 100 ms

# Get the frequencies and trace data
frequencies = instrument.frequencies
trace_data = instrument.trace(1)

# Print the frequencies and trace data
for frequency, data in zip(frequencies, trace_data):
    print(f"Frequency: {frequency} Hz, Data: {data}")

# Disconnect from the instrument
instrument.disconnect()
```

This script connects to the KEYSIGHT - E4408B ESA-L Spectrum Analyzer using a VISA adapter with the instrument's IP address. It then sets various properties of the instrument such as start and stop frequencies, number of frequency points, frequency step, center frequency, and sweep time. It then retrieves the frequencies and trace data using the `frequencies` and `trace` methods respectively. Finally, it prints the frequencies and trace data and disconnects from the instrument.

