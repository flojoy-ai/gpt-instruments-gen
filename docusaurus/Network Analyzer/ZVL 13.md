
# ZVL 13

## Instrument Card

The ZVL is a compact, cost-efficient, powerful and portable network analyzer. It is ideal for use in development, production, and service. It is the only instrument to combine the functions of a network analyzer, spectrum analyzer, and power meter in a single box, making you much more efficient.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Rohde & Schwarz GmbH & Co KG is an international electronics group specializing in the fields of electronic test equipment, broadcast & media, cybersecurity, radiomonitoring and radiolocation, and radiocommunication. <a href=https://www.rohde-schwarz.com/ca/home_48230.html>Website</a>.
<br>
<ul>
  <li>Headquarters: Munich, Germany</li>
  <li>Yearly Revenue (millions, USD): 2500.0</li>
</ul>
</details>

## Connect to the ZVL 13 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a ZVL 13 Network Analyzer using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station
from qcodes.instrument_drivers.rohde_schwarz.ZVL13 import ZVL13

# Create a station to hold the instruments
station = Station()

# Connect to the ZVL 13 Network Analyzer
zvl13 = ZVL13('zvl13', 'TCPIP0::192.168.1.1::inst0::INSTR')
station.add_component(zvl13)

# Print the available parameters and functions of the ZVL 13
print(zvl13.parameters)
print(zvl13.functions)

# Set the start frequency, stop frequency, and number of points
zvl13.start(1e6)
zvl13.stop(1e9)
zvl13.npts(101)

# Perform a frequency sweep and get the magnitude and phase data
mag, phase = zvl13.trace_mag_phase()

# Print the magnitude and phase data
print(mag)
print(phase)

# Disconnect from the instruments
zvl13.close()
```

Note: Replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual address of your ZVL 13 Network Analyzer.

