
# Rigol DP831

## Instrument Card

The Rigol DP831 features a relative large (8.9 cm / 3.5") and easy to read TFT monochrome display. In addition to the normal digital displays for voltage, current, and power, these values can also be displayed as signal curves.

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

## Connect to the Rigol DP831 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.rigol.DP831 import RigolDP831

# Create an instance of the RigolDP831 driver
dp831 = RigolDP831('dp831', 'TCPIP0::192.168.1.10::INSTR')

# Connect to the instrument
dp831.connect()

# Perform operations with the instrument

# Disconnect from the instrument
dp831.disconnect()
```

This code imports the necessary modules and creates an instance of the `RigolDP831` driver. It then connects to the instrument using the specified address. After connecting, you can perform various operations with the instrument. Finally, it disconnects from the instrument.

