
# KEYSIGHT 33210A

## Instrument Card

The Keysight (formerly Agilent) 33210A is the latest function/arbitrary waveform generator from Keysight. It uses direct digital synthesis techniques to create a stable, accurate output signal having clean, low distortion sine waves. For user defined waveforms, option 002 provides 14-bit 8k point arbitrary waveform generation

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 33210A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 33210A Function Generator using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_33XXX import WaveformGenerator_33XXX

# Create an instance of the instrument
instrument = WaveformGenerator_33XXX('my_instrument', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
instrument.connect()

# Now you can use the instrument to control the function generator
# For example, you can set the frequency of channel 1 to 1 kHz
instrument.ch1.frequency(1e3)

# You can also read the current frequency setting
frequency = instrument.ch1.frequency()
print(f"The current frequency is: {frequency} Hz")

# Disconnect from the instrument
instrument.disconnect()
```

Note: Replace `'TCPIP0::192.168.1.1::INSTR'` with the actual VISA resource name of your KEYSIGHT 33210A Function Generator.

