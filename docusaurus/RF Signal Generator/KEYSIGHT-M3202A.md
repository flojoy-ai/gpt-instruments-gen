
# KEYSIGHT M3202A

## Instrument Card

Keysight's M3202A PXIe arbitrary waveform generator offers 4 channels, on-board FPGA with optional software tools that enable real-time sequencing, inter-module synchronization, and graphical FPGA design environment.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT M3202A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT M3202A RF Signal Generator using Qcodes Community, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.Keysight_M3202A import M3202A

# Create an instance of the M3202A driver
awg1 = M3202A('awg1', chassis=0, slot=2)

# Connect to the instrument
awg1.connect()

# Now you can use the instrument for various operations
# For example, you can upload a waveform
waveform_data = [0, 1, 0, -1, 0, 1, 0, -1]  # Example waveform data
ref_1 = awg1.upload_waveform(waveform_data)

# Set the trigger mode and queue the waveform
trigger_mode = awg1.SD_TriggerModes.EXTTRIG
awg1.awg_queue_waveform(1, ref_1, trigger_mode, 0, 1, 0)

# Disconnect from the instrument
awg1.disconnect()
```

In this script, we import the `M3202A` driver from `qcodes.instrument_drivers.Keysight.Keysight_M3202A`. We then create an instance of the driver with the name 'awg1' and specify the chassis number and slot number where the device is located.

Next, we connect to the instrument using the `connect()` method. After connecting, we can perform various operations on the instrument. In this example, we upload a waveform using the `upload_waveform()` method and obtain a waveform reference `ref_1`.

We then set the trigger mode to `EXTTRIG` and queue the waveform using the `awg_queue_waveform()` method.

Finally, we disconnect from the instrument using the `disconnect()` method.

Note: Make sure you have the necessary dependencies installed, including the Qcodes Community package and the Keysight instrument drivers.

