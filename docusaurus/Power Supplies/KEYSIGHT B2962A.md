
# KEYSIGHT B2962A

## Instrument Card

The Keysight B2962A source / measure unit (SMU) is a 6.5-digit low noise power source that provides a power supply and source solution that meets the difficult measurement challenges researchers, designers, and developers face working on advanced components, circuits, and materials.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT B2962A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here's a Python script that uses Qcodes to connect to a KEYSIGHT B2962A Power Supply:

```python
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument_drivers.Keysight.KeysightB2962A import KeysightB2962A

# Create an instance of the KeysightB2962A instrument
power_supply = KeysightB2962A('power_supply', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
power_supply.connect()

# Get the identification information of the instrument
idn = power_supply.get_idn()
print(f"Vendor: {idn['vendor']}")
print(f"Model: {idn['model']}")
print(f"Serial: {idn['serial']}")
print(f"Firmware: {idn['firmware']}")

# Set the voltage and current limits for channel 1
power_supply.ch1.voltage_limit(5)  # Set voltage limit to 5V
power_supply.ch1.current_limit(0.1)  # Set current limit to 0.1A

# Enable channel 1
power_supply.ch1.enable('on')

# Set the voltage and current for channel 1
power_supply.ch1.source_voltage(3.3)  # Set voltage to 3.3V
power_supply.ch1.source_current(0.05)  # Set current to 0.05A

# Measure the voltage and current for channel 1
voltage = power_supply.ch1.voltage()
current = power_supply.ch1.current()
print(f"Voltage: {voltage}V")
print(f"Current: {current}A")

# Disable channel 1
power_supply.ch1.enable('off')

# Disconnect from the instrument
power_supply.disconnect()
```

This script creates an instance of the `KeysightB2962A` instrument, connects to the instrument using the specified address, retrieves the identification information of the instrument, sets the voltage and current limits for channel 1, enables channel 1, sets the desired voltage and current for channel 1, measures the voltage and current for channel 1, disables channel 1, and finally disconnects from the instrument.

