
# ATS9440 - 14 bit, 125 MS/s, 4 ch

## Instrument Card

ATS9440 is a 4-channel, 14-bit, 125 MS/s waveform digitizer based on the 8-lane PCI Express interface

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Alazar Technologies Inc. (AlazarTech) was founded in 2003 with the goal of serving the test and measurement market, in general, and the embedded waveform digitizer (OEM) market segment, in particular, by providing highly differentiated, high performance instrumentation products at affordable prices. <a href=https://www.alazartech.com/>Website</a>.

<ul>
  <li>Headquarters: CANADA - QC</li>
  <li>Yearly Revenue (millions, USD): 4.0</li>
</ul>
</details>

## Connect to the ATS9440 - 14 bit, 125 MS/s, 4 ch in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here is a Python script that uses Qcodes to connect to an ATS9440 - 14 bit, 125 MS/s, 4 ch DAQ board:

```python
from qcodes import Station
from qcodes.instrument_drivers.AlazarTech.ATS9440 import AlazarTech_ATS9440

# Create a station to hold the instruments
station = Station()

# Create an instance of the ATS9440 instrument
ats9440 = AlazarTech_ATS9440('ats9440', dll_path='C:\\WINDOWS\\System32\\ATSApi.dll')

# Add the instrument to the station
station.add_component(ats9440)

# Connect to the instrument
ats9440.connect()

# Now you can use the instrument to perform measurements
# For example, you can set the clock source:
ats9440.clock_source('INTERNAL_CLOCK')

# You can also read the current clock source:
clock_source = ats9440.clock_source()

# Disconnect from the instrument
ats9440.disconnect()
```

Note: Make sure to replace `'C:\\WINDOWS\\System32\\ATSApi.dll'` with the correct path to the ATSApi.dll file on your system.

