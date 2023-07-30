
# Keithley 2602A

## Instrument Card

The Keithley 2602A SourceMeter is used as either a bench-top I-V characterization tool or as a building block component of multi-channel I-V test systems. For bench-top use, the Keithley 2602A SourceMeter features an embedded TSP® Express Software Tool that allows users to quickly and easily perform common I-V tests without programming or installing software. For system level applications, the Keithley 2602A SourceMeter's Test Script Processor (TSP®) architecture along with new capabilities such as parallel test execution and precision timing provide the highest throughput in the industry to lower the cost of test.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.
<br>
<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley 2602A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes


```python
import qcodes as qc
from qcodes.instrument_drivers.tektronix.Keithley_2600_channels import Keithley2600

# Create an instance of the Keithley 2602A instrument
keithley = Keithley2600('keithley', 'TCPIP::192.168.1.1::INSTR')

# Connect to the instrument
keithley.connect()

# Print the instrument ID
print(keithley.get_idn())

# Set the voltage and current limits
keithley.smua.limitv(10)  # Set voltage limit to 10V
keithley.smua.limiti(0.1)  # Set current limit to 0.1A

# Enable the output
keithley.smua.output(1)  # Turn on the output

# Set the voltage and current levels
keithley.smua.volt(5)  # Set voltage to 5V
keithley.smua.curr(0.05)  # Set current to 50mA

# Measure the voltage and current
voltage = keithley.smua.volt()
current = keithley.smua.curr()
print(f"Voltage: {voltage}V, Current: {current}A")

# Disable the output
keithley.smua.output(0)  # Turn off the output

# Disconnect from the instrument
keithley.disconnect()
```

Note: Replace `'TCPIP::192.168.1.1::INSTR'` with the actual IP address or VISA resource address of your Keithley 2602A Power Supply.

This script creates an instance of the `Keithley2600` instrument, connects to it, sets the voltage and current limits, enables the output, sets the voltage and current levels, measures the voltage and current, disables the output, and finally disconnects from the instrument.

Make sure to install the necessary dependencies (`qcodes` and `pyvisa`) before running the script.

