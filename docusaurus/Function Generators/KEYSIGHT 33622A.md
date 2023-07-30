
# KEYSIGHT 33622A

## Instrument Card

The Keysight 33622A function/arbitrary waveform generators offer the standard signals and features you expect, such as modulation, sweep, and burst. However, it also provides features that give you the capabilities and flexibility you need to get your job done quickly, no matter how complex. An intuitive front-panel user interface, for example, can be quickly and easily relearned when your attention has been focused elsewhere.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33622A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 33622A Function Generator using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_33600A import Keysight_33600A

# Create an instance of the instrument driver
instrument = Keysight_33600A('instrument_name', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
instrument.connect()

# Now you can use the instrument to control the function generator
# For example, you can set the frequency of channel 1 to 1 kHz
instrument.ch1.frequency(1e3)

# You can also read the current frequency setting
frequency = instrument.ch1.frequency()

# Disconnect from the instrument
instrument.disconnect()
```

Note: Replace `'instrument_name'` with a unique name for your instrument and `'TCPIP0::192.168.1.1::INSTR'` with the actual VISA resource name of your KEYSIGHT 33622A Function Generator.

