
# KEYSIGHT M3201A

## Instrument Card

Keysight's M3201A PXIe arbitrary waveform generator offers 4 channels, on-board FPGA with optional FPGA software tools that enable real-time sequencing, inter-module synchronization, and graphical FPGA design environment.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT M3201A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT M3201A RF Signal Generator using Qcodes Community, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_M3201A import Keysight_M3201A

# Create an instance of the instrument
awg = Keysight_M3201A('awg', chassis=1, slot=7)

# Connect to the instrument
awg.connect()

# Now you can use the instrument for various operations
# For example, you can set the output voltage of a channel
awg.channels[1].amplitude(0.5)  # Set the amplitude of channel 1 to 0.5 V

# Disconnect from the instrument
awg.disconnect()
```

Note: Make sure you have the necessary dependencies installed, including Qcodes and the Keysight instrument driver.

