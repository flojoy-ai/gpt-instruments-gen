
# KEYSIGHT N5245A

## Instrument Card

The Keysight N5245A Network Analyzer provides a wide range of measurement applications for amplifiers, converters, antennas, or mixers with a single connection.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5245A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_N5245A import Keysight_N5245A

# Connect to the instrument
n5245a = Keysight_N5245A("n5245a", "TCPIP0::192.168.1.1::inst0::INSTR")

# Print the instrument ID
print(n5245a.IDN())

# Set the frequency range
n5245a.frequency_range(10e6, 50e9)

# Set the power range
n5245a.power_range(-30, 13)

# Set the number of ports
n5245a.number_of_ports(4)

# Enable FOM if option "080" is available
if "080" in n5245a.get_options():
    n5245a.enable_fom()

# Close the connection to the instrument
n5245a.close()
```

Note: Make sure to replace `"TCPIP0::192.168.1.1::inst0::INSTR"` with the actual IP address or VISA resource string of your instrument.

