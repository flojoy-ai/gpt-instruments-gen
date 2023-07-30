
# KEYSIGHT N5230C

## Instrument Card

The Keysight N5230C PNA-L is a microwave network analyzer made to test amplifiers, passive parts, and frequency converters using S-parameters and basic nonlinearity. The Keysight N5230C has a 110 dB system / 122 dB receiver dynamic range. The N5230C has a 300 kHz to 20 GHz frequency range and has 2 or 4 ports with built-in sources.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5230C in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes.instrument_drivers.Keysight.Keysight_N5230C import Keysight_N5230C

# Connect to the N5230C Network Analyzer
n5230c = Keysight_N5230C('n5230c', 'TCPIP0::192.168.1.1::INSTR')

# Perform operations using the instrument
n5230c.connect()
n5230c.get_idn()
n5230c.set_frequency(1e9)
n5230c.set_power(-10)
n5230c.measure('S21')
n5230c.get_data('S21')
n5230c.disconnect()
```

Note: Replace `'TCPIP0::192.168.1.1::INSTR'` with the actual IP address or VISA resource string of your N5230C Network Analyzer.

