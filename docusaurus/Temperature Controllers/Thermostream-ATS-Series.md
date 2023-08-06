
# Thermostream ATS Series

## Instrument Card

Temptronic ThermoStreams are portable systems that deliver clean dry air for precision temperature testing or conditioning of electronics (ICs, MEMS, transceivers, or circuits) and materials. No other systems can bring your test subjects to temperature faster with precise control

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Temptronic** temperature forcing systems, are designed for testing and characterization of semiconductors, ICs, chips, electronics, and materials. <a href=https://www.intestthermal.com/temptronic>Website</a>.
<br></br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 19.0</li>
</ul>
</details>

## Connect to the Thermostream ATS Series in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure

Here is an example Python script that uses Pymeasure to connect to a Thermostream ATS Series Temperature Controller:

```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.thermostream import ATSBase

# Connect to the instrument
adapter = VISAAdapter("TCPIP::192.168.1.1::INSTR")  # Replace with the actual IP address of the instrument
instrument = ATSBase(adapter)

# Configure the instrument
instrument.configure(
    temp_window=1,
    dut_type='T',
    soak_time=30,
    dut_constant=100,
    temp_limit_air_low=-60,
    temp_limit_air_high=220,
    temp_limit_air_dut=50,
    maximum_test_time=1000
)

# Start the instrument
instrument.start()

# Set the temperature to 25 degrees Celsius
instrument.set_temperature(25)

# Wait for the instrument to settle
instrument.wait_for_settling()

# Check if the instrument is at temperature
if instrument.at_temperature():
    print("The instrument is at temperature")
else:
    print("The instrument is not at temperature")

# Stop the instrument
instrument.shutdown()
```

Note: Replace `"TCPIP::192.168.1.1::INSTR"` with the actual VISA address of the instrument, which can be found using the instrument's software or by consulting the instrument's documentation.

