
# KEYSIGHT DSOX1102G

## Instrument Card

The DSOX1102G oscilloscope provides 70, 100 MHz of bandwidth on 2 analog channels, and waveform generator

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT DSOX1102G in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.keysight import KeysightDSOX1102G

# Connect to the oscilloscope
adapter = VISAAdapter("USB0::0x0957::0x179B::MY44012345::INSTR")
oscilloscope = KeysightDSOX1102G(adapter)

# Perform some operations on the oscilloscope
oscilloscope.clear_status()
oscilloscope.autoscale()
ch1_data_array, ch1_preamble = oscilloscope.download_data(source="channel1", points=2000)

# Disconnect from the oscilloscope
oscilloscope.shutdown()
```

In this script, we first import the necessary modules from Pymeasure. We then create a `VISAAdapter` object to connect to the oscilloscope using its VISA address. Next, we create a `KeysightDSOX1102G` object using the adapter.

We can then perform various operations on the oscilloscope, such as clearing the status, autoscaling the display, and downloading data from channel 1. Finally, we call the `shutdown()` method to disconnect from the oscilloscope.

Note: Replace `"USB0::0x0957::0x179B::MY44012345::INSTR"` with the actual VISA address of your oscilloscope.

