
# KEYSIGHT 33512B

## Instrument Card

The 33512B provides Keysight’s exclusive Trueform technology which offers unmatched capabilities for generating a full range of signals for your most demanding measurements. The 33512B can be easily upgraded to 30 MHz as your needs change.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33512B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 33512B RF Signal Generator using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_33XXX import WaveformGenerator_33XXX

# Create an instance of the instrument
signal_generator = WaveformGenerator_33XXX('signal_generator', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
signal_generator.connect_message()
```

This script imports the `WaveformGenerator_33XXX` class from the `qcodes.instrument_drivers.Keysight.Keysight_33XXX` module. It then creates an instance of the instrument with the name `'signal_generator'` and the appropriate VISA resource address (`'TCPIP0::192.168.1.1::INSTR'` in this example). Finally, it calls the `connect_message()` method to establish a connection to the instrument and print a connection message.

