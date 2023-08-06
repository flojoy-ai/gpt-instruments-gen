
# KEYSIGHT 5222B

## Instrument Card

The Keysight N5222B PNA Microwave Network Analyzer 10 MHz to 26.5 GHz is an integrated and flexible test engine that can measure active devices such as amplifiers, mixers, and frequency converters. This analyzer operates at a frequency range of 900 Hz to 26.5 GHz. The Keysight N5222B provides a combination of excellent hardware and powerful measurement applications to measure a broad range of devices quickly and accurately.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 5222B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 5222B Network Analyzer using Qcodes, you can use the following Python script:

```python
from qcodes import Station
from qcodes.instrument_drivers.Keysight.Keysight_PNA import Keysight_PNA

# Create a station to hold the instruments
station = Station()

# Connect to the KEYSIGHT 5222B Network Analyzer
pna = Keysight_PNA('pna', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Add the KEYSIGHT 5222B Network Analyzer to the station
station.add_component(pna)

# Print the available options on the KEYSIGHT 5222B Network Analyzer
print(pna.get_options())

# Print the trace catalog on the KEYSIGHT 5222B Network Analyzer
print(pna.get_trace_catalog())

# Select a trace on the KEYSIGHT 5222B Network Analyzer by name
pna.select_trace_by_name('S11')

# Set the start and stop frequencies on the KEYSIGHT 5222B Network Analyzer
pna.start(1e6)
pna.stop(1e9)

# Set the power on the KEYSIGHT 5222B Network Analyzer
pna.power(-10)

# Set the number of points in a sweep on the KEYSIGHT 5222B Network Analyzer
pna.points(1001)

# Set the IF bandwidth on the KEYSIGHT 5222B Network Analyzer
pna.if_bandwidth(1e3)

# Set the electrical delay on the KEYSIGHT 5222B Network Analyzer
pna.electrical_delay(0)

# Set the sweep mode on the KEYSIGHT 5222B Network Analyzer
pna.sweep_mode('CONT')

# Run a sweep on the KEYSIGHT 5222B Network Analyzer
pna.run_sweep()

# Get the data from the selected trace on the KEYSIGHT 5222B Network Analyzer
data = pna.traces[0].get()

# Print the data
print(data)

# Disconnect from the KEYSIGHT 5222B Network Analyzer
pna.close()
```

This script creates a station to hold the instruments and connects to the KEYSIGHT 5222B Network Analyzer using the `Keysight_PNA` driver from Qcodes. It then performs various operations on the network analyzer, such as getting the available options, selecting a trace, setting frequency and power parameters, running a sweep, and getting the data from the selected trace. Finally, it disconnects from the network analyzer.

