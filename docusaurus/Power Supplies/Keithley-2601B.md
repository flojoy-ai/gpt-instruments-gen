
# Keithley 2601B

## Instrument Card

The Model 2601B SourceMeter SMU instrument, is a new and improved one channel SMU instrument with a tightly integrated four-quadrant design that allows it to simultaneously source and measure both voltage and current to boost productivity in applications ranging from R&D to automated production test. In addition to retaining all the features of the Model 2601A, the Model 2601B has 6½-digit resolution, USB 2.0 connectivity, and software command emulation of the Model 2400 SourceMeter SMU Instrument that enables easy migration of legacy test code. The Model 2601B model is equipped with Keithley's high speed TSP technology (over 190% faster than traditional PC-to-instrument communication techniques,) which dramatically improves the system-level speed to lower the cost of test.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley 2601B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here's an example Python script that uses Qcodes to connect to a Keithley 2601B Power Supply:

```python
import qcodes as qc
from qcodes.instrument_drivers.tektronix.Keithley_2600_channels import Keithley2600

# Create a connection to the Keithley 2601B Power Supply
keithley = Keithley2600("keithley", "TCPIP::192.168.1.1::INSTR")

# Print the instrument ID
print(keithley.get_idn())

# Set the voltage and current limits
keithley.smua.limitv.set(10)  # Set voltage limit to 10V
keithley.smua.limiti.set(0.1)  # Set current limit to 0.1A

# Enable the output
keithley.smua.output.set(1)  # Turn on the output

# Set the voltage and current levels
keithley.smua.volt.set(5)  # Set the voltage to 5V
keithley.smua.curr.set(0.05)  # Set the current to 50mA

# Measure the voltage and current
voltage = keithley.smua.volt.get()
current = keithley.smua.curr.get()
print(f"Measured voltage: {voltage}V")
print(f"Measured current: {current}A")

# Disable the output
keithley.smua.output.set(0)  # Turn off the output

# Close the connection
keithley.close()
```

Note: Replace `"TCPIP::192.168.1.1::INSTR"` with the actual IP address or VISA resource address of your Keithley 2601B Power Supply.

