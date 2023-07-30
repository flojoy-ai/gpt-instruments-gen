
# KEYSIGHT N9000A

## Instrument Card

N9000A CXA Signal Analyzer, 9 kHz to 26.5 GHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N9000A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT N9000A Spectrum Analyzer using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station, Instrument
from qcodes.instrument_drivers.Keysight.Keysight_N9000A import Keysight_N9000A

# Create a station to hold the instrument
station = Station()

# Connect to the KEYSIGHT N9000A Spectrum Analyzer
n9000a = Keysight_N9000A('n9000a', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Add the instrument to the station
station.add_component(n9000a)

# Print the instrument ID
print(n9000a.IDN())

# Close the connection
n9000a.close()
```

This script creates a station to hold the instrument, connects to the KEYSIGHT N9000A Spectrum Analyzer using the `Keysight_N9000A` driver, adds the instrument to the station, prints the instrument ID, and then closes the connection.

Note: Make sure to replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual address of your KEYSIGHT N9000A Spectrum Analyzer.

