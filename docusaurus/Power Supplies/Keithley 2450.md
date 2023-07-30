
# Keithley 2450

## Instrument Card

The 2450 is Keithley's next-generation SourceMeter source measure unit (SMU) instrument that truly brings Ohm's law (current, voltage, and resistance) testing right to your fingertips. Its innovative graphical user interface (GUI) and advanced, capacitive touchscreen technology allow intuitive usage and minimize the learning curve to enable engineers and scientists to learn faster, work smarter, and invent easier. The 2450 is the SMU for everyone: a versatile instrument, particularly well-suited for characterizing modern scaled semiconductors, nano-scale devices and materials, organic semiconductors, printed electronics, and other small-geometry and low-power devices.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.
<br>
<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley 2450 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.adapters import VISAAdapter
from pymeasure.instruments.keithley import Keithley2450

# Create a VISA adapter for the instrument
adapter = VISAAdapter("GPIB::1")

# Connect to the Keithley 2450 Power Supply
keithley = Keithley2450(adapter)

# Configure the instrument
keithley.apply_current()
keithley.source_current_range = 10e-3
keithley.compliance_voltage = 10
keithley.source_current = 0
keithley.enable_source()

# Measure voltage
keithley.measure_voltage()

# Ramp the current to 5 mA
keithley.ramp_to_current(5e-3)

# Print the voltage
print(keithley.voltage)

# Shutdown the instrument
keithley.shutdown()
```

This script first creates a VISA adapter using the `VISAAdapter` class from Pymeasure. The adapter is then used to connect to the Keithley 2450 Power Supply by creating an instance of the `Keithley2450` class.

The script then configures the instrument by setting the source mode to current, the current range to 10 mA, the compliance voltage to 10 V, and the source current to 0 mA. It then enables the source output.

Next, it configures the instrument to measure voltage.

After that, it ramps the current to 5 mA using the `ramp_to_current` method.

Finally, it prints the measured voltage and shuts down the instrument.

Note: Make sure to replace `"GPIB::1"` with the appropriate address of your Keithley 2450 Power Supply.

### Qcodes

To connect to a Keithley 2450 Power Supply using Qcodes, you can use the following Python script:

```python
import qcodes as qc
from qcodes.instrument_drivers.tektronix.Keithley_2450 import Keithley_2450

# Connect to the Keithley 2450 Power Supply
keithley = Keithley_2450("keithley", "TCPIP0::192.168.1.1::INSTR")

# Print the instrument ID
print(keithley.IDN())

# Set the source function to voltage
keithley.source_function("voltage")

# Set the voltage to 1V
keithley.source_voltage(1)

# Enable the output
keithley.output_enabled(True)

# Measure the current
current = keithley.sense_current()
print(f"Current: {current} A")

# Disable the output
keithley.output_enabled(False)

# Close the connection
keithley.close()
```

Make sure to replace `"TCPIP0::192.168.1.1::INSTR"` with the actual IP address or VISA resource string of your Keithley 2450 Power Supply.

