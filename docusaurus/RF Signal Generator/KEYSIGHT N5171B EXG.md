
# KEYSIGHT N5171B EXG

## Instrument Card

N5171B EXG X-Series RF analog mid-performance signal generators offer 9 kHz to 6 GHz frequency coverage, optimized for manufacturing with faster throughput and greater uptime at the right price.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5171B EXG in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes import Station, Instrument
from qcodes.instrument_drivers.Keysight.N51x1 import N51x1

# Create a station to hold the instrument
station = Station()

# Connect to the KEYSIGHT N5171B EXG RF Signal Generator
n5171b = N51x1('n5171b', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Add the instrument to the station
station.add_component(n5171b)

# Print the IDN information of the instrument
print(n5171b.get_idn())

# Set the frequency to 1 GHz
n5171b.frequency(1e9)

# Set the power to -10 dBm
n5171b.power(-10)

# Enable the RF output
n5171b.rf_output(1)

# Disconnect from the instrument
n5171b.close()
```

This script connects to a KEYSIGHT N5171B EXG RF Signal Generator using the Qcodes driver `N51x1`. It creates a `Station` to hold the instrument, connects to the instrument using the instrument's IP address, adds the instrument to the station, and prints the IDN information of the instrument.

Then, it sets the frequency to 1 GHz, the power to -10 dBm, and enables the RF output. Finally, it closes the connection to the instrument.

