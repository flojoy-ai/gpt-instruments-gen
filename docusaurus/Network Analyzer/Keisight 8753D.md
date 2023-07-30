
# Keisight 8753D

## Instrument Card

8753D Network Analyzer, 30 kHz to 3 GHz

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the Keisight 8753D in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a Keysight 8753D Network Analyzer using Qcodes, you can use the following Python script:

```python
import qcodes as qc
from qcodes.instrument_drivers.Keysight.Keysight_8753D import Keysight_8753D

# Create an instance of the instrument
instrument = Keysight_8753D("instrument_name", "TCPIP0::192.168.1.1::INSTR")

# Connect to the instrument
instrument.connect()

# Now you can use the instrument to perform measurements
# For example, you can set the start frequency
instrument.start_freq(1e6)

# You can also read the trace data
trace_data = instrument.trace()

# Disconnect from the instrument
instrument.disconnect()
```

Note that you need to replace `"instrument_name"` with the desired name for your instrument, and `"TCPIP0::192.168.1.1::INSTR"` with the actual address of your Keysight 8753D Network Analyzer.

