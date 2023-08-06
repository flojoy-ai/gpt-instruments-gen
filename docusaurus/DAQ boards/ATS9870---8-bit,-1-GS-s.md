
# ATS9870 - 8 bit, 1 GS/s

## Instrument Card

ATS9870 is the world's first Giga-sample waveform digitizer based on the 8-lane PCI Express interface

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Alazar Technologies Inc. (AlazarTech) was founded in 2003 with the goal of serving the test and measurement market, in general, and the embedded waveform digitizer (OEM) market segment, in particular, by providing highly differentiated, high performance instrumentation products at affordable prices. <a href=https://www.alazartech.com/>Website</a>.
<br></br>
<ul>
  <li>Headquarters: CANADA - QC</li>
  <li>Yearly Revenue (millions, USD): 4.0</li>
</ul>
</details>

## Connect to the ATS9870 - 8 bit, 1 GS/s in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to an ATS9870 board using Qcodes, you can use the following Python script:

```python
from qcodes.instrument_drivers.AlazarTech.ATS9870 import AlazarTech_ATS9870

# Create an instance of the ATS9870 driver
ats9870 = AlazarTech_ATS9870('ats9870', dll_path='C:\\WINDOWS\\System32\\ATSApi.dll')

# Connect to the board
ats9870.connect()

# Now you can use the board for data acquisition and other operations
# For example, you can set the sample rate
ats9870.sample_rate(1_000_000_000)

# Disconnect from the board
ats9870.disconnect()
```

Note that you need to provide the correct path to the `ATSApi.dll` file in the `dll_path` argument of the `AlazarTech_ATS9870` constructor.

