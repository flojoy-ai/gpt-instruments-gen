
# ATS9373 - 12 bit, 4 GS/s

## Instrument Card

ATS9373 is a 12-bit waveform digitizer board that can sample one analog input at rates up to 4 GS/s or two inputs at 2 GS/s.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Alazar Technologies Inc. (AlazarTech) was founded in 2003 with the goal of serving the test and measurement market, in general, and the embedded waveform digitizer (OEM) market segment, in particular, by providing highly differentiated, high performance instrumentation products at affordable prices. <a href=https://www.alazartech.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: CANADA - QC</li>
  <li>Yearly Revenue (millions, USD): 4.0</li>
</ul>
</details>

## Connect to the ATS9373 - 12 bit, 4 GS/s in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here is a Python script that uses Qcodes to connect to an ATS9373 - 12 bit, 4 GS/s DAQ board:

```python
from qcodes.instrument_drivers.AlazarTech.ATS import AlazarTech_ATS
from qcodes.instrument_drivers.AlazarTech.ATS9373 import AlazarTechATS9373

# Connect to the ATS9373 board
ats = AlazarTechATS9373('ats', dll_path='C:\\WINDOWS\\System32\\ATSApi.dll')

# Print the board ID
print(ats.get_idn())

# Set the clock source to INTERNAL_CLOCK
ats.clock_source('INTERNAL_CLOCK')

# Set the sample rate to 4 GS/s
ats.sample_rate(4_000_000_000)

# Set other parameters as needed

# Close the connection to the board
ats.close()
```

This script connects to the ATS9373 board using the `AlazarTechATS9373` driver. It sets the clock source to `INTERNAL_CLOCK` and the sample rate to 4 GS/s. You can set other parameters as needed for your application. Finally, it closes the connection to the board.

