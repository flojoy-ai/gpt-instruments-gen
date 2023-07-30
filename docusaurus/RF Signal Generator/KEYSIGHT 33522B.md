
# KEYSIGHT 33522B

## Instrument Card

Keysight 33500B Series waveform generators with exclusive Trueform signal generation technology offer more capability, fidelity, and flexibility than previous generation DDS generators. Easily generate the full range of signals you need to your devices with confidence the signal generator is outputting the signals you expect.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33522B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 33522B RF Signal Generator using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_33XXX import WaveformGenerator_33XXX

# Create an instance of the instrument
signal_generator = WaveformGenerator_33XXX('signal_generator', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
signal_generator.connect_message()
```

This script imports the `WaveformGenerator_33XXX` class from the `qcodes.instrument_drivers.Keysight.Keysight_33XXX` module. It then creates an instance of the instrument with the name `'signal_generator'` and the appropriate VISA resource address (`'TCPIP0::192.168.1.1::INSTR'` in this example). Finally, it calls the `connect_message()` method to establish a connection to the instrument and print a connection message.

