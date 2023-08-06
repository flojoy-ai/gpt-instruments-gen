
# KEYSIGHT - B1500A

## Instrument Card

It provides a wide range of measurement capabilities to cover the electrical characterization and evaluation of devices, materials, semiconductors, active/passive components, or virtually any other type of electronic device with uncompromised measurement reliability and efficiency. The B1500A modular architecture gives you the flexibility to upgrade when needed.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT - B1500A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure import Instrument

# Connect to the instrument
instrument = Instrument("GPIB::1::INSTR")

# Set the measurement mode to spectrum analyzer
instrument.write("MODE SA")

# Set the center frequency to 1 GHz
instrument.write("CF 1e9")

# Set the span to 1 MHz
instrument.write("SP 1e6")

# Set the resolution bandwidth to 1 kHz
instrument.write("RB 1e3")

# Set the video bandwidth to 1 kHz
instrument.write("VB 1e3")

# Start the measurement
instrument.write("TS")

# Read the measurement data
data = instrument.read()

# Print the measurement data
print(data)

# Disconnect from the instrument
instrument.close()
```

This script connects to the instrument using the GPIB interface and sets the measurement mode to spectrum analyzer. It then sets the center frequency, span, resolution bandwidth, and video bandwidth to the desired values. After starting the measurement, it reads the measurement data and prints it. Finally, it disconnects from the instrument.

Please note that you may need to modify the GPIB address and the specific commands based on your instrument and measurement requirements.

