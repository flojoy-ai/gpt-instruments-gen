
# KEYSIGHT N5173B EXG

## Instrument Card

The Keysight N5173B EXG microwave analog signal generator is the cost-effective choice when you need to balance budget and performance. It provides the essential signals that address parametric testing of broadband filters, amplifiers, receivers, and more. Perform basic LO upconversion or CW blocking with low-cost coverage to 13, 20, 31.8, or 40 GHz. Characterize broadband microwave components such as filters and amplifiers with the best combination of output power (+20 dBm at 20 GHz), low harmonics (≤ –55 dBc), and full step attenuation. Use as a high-stability system reference with standard high-performance OCXO at an aging rate of less than ± 5 parts per billion per day.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5173B EXG in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT N5173B EXG RF Signal Generator using Qcodes, you can use the following Python script:

```python
from qcodes import Station, Instrument
from qcodes.instrument_drivers.Keysight.Keysight_N51x1 import N51x1

# Create a station to hold the instrument
station = Station()

# Connect to the KEYSIGHT N5173B EXG RF Signal Generator
n5173b = N51x1('n5173b', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Add the instrument to the station
station.add_component(n5173b)

# Print the instrument's IDN information
print(n5173b.get_idn())

# Set the power to -10 dBm
n5173b.power(-10)

# Set the frequency to 1 GHz
n5173b.frequency(1e9)

# Enable the RF output
n5173b.rf_output('on')

# Disable the RF output
n5173b.rf_output('off')

# Close the connection to the instrument
n5173b.close()
```

This script creates a station to hold the instrument, connects to the KEYSIGHT N5173B EXG RF Signal Generator using the `N51x1` driver, adds the instrument to the station, and performs various operations such as getting the IDN information, setting the power and frequency, and enabling/disabling the RF output. Finally, it closes the connection to the instrument.

