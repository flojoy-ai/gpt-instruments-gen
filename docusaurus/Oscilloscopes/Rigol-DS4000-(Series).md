
# Rigol DS4000 (Series)

## Instrument Card

The Rigol DS4000 series consists of 8 high level Oscilloscopes for professional operation, which come off very well compared to higher prices models of other brands.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
RIGOL Technologies, Inc. specializes in development and production of test and measuring equipment and is one of the fastest growing Chinese companies in this sphere.
RIGOL’s line of products includes [digital storage oscilloscopes](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=227), [function/arbitrary waveform generators](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=230), [digital multimeters](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=233), PC-based devices compatible with LXI standard etc. <a href=https://www.rigol.com/>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Beijing, China</li>
  <li>Yearly Revenue (millions, USD): 23.0</li>
</ul>
</details>

## Connect to the Rigol DS4000 (Series) in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a Rigol DS4000 Oscilloscope using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.rigol.rigol_ds4000 import RigolDS4000

# Create an instance of the RigolDS4000 instrument
scope = RigolDS4000("scope", "USB0::0x1AB1::0x04CE::DS4A203400948::INSTR")

# Connect to the instrument
scope.connect()

# Now you can use the instrument to perform various operations
# For example, you can start the acquisition
scope.run()

# You can also read the waveform data from a specific channel
channel1_data = scope.channels.ch1.curvedata()

# Print the first 10 points of the waveform
print(channel1_data[:10])

# Disconnect from the instrument
scope.disconnect()
```

This script creates an instance of the `RigolDS4000` instrument, specifying the name and the VISA address of the instrument. Then, it connects to the instrument using the `connect()` method. After that, you can use various methods and parameters of the instrument to control and read data from the oscilloscope. Finally, the script disconnects from the instrument using the `disconnect()` method.

