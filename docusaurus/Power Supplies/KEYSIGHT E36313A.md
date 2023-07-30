
# KEYSIGHT E36313A

## Instrument Card

The triple output, 160 W, E36313A provides small, compact size for bench use; low output ripple and noise; built-in measurements and basic programmable features with USB and LAN, and optional GPIB interfaces.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT E36313A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT E36313A Power Supply using Qcodes Community, you can use the following Python script:

```python
from qcodes.instrument_drivers.Keysight.E36313A import E36313A

# Create an instance of the E36313A instrument
power_supply = E36313A('power_supply', 'TCPIP0::192.168.1.1::INSTR')

# Connect to the instrument
power_supply.connect()

# Get the identification information of the instrument
idn = power_supply.get_idn()
print("Instrument IDN:", idn)

# Set the voltage and current for channel 1
power_supply.ch1.source_voltage(5)  # Set voltage to 5V
power_supply.ch1.source_current(0.5)  # Set current to 0.5A

# Enable channel 1
power_supply.ch1.enable('on')

# Read the voltage and current from channel 1
voltage = power_supply.ch1.voltage()
current = power_supply.ch1.current()
print("Channel 1 - Voltage:", voltage, "V")
print("Channel 1 - Current:", current, "A")

# Disable channel 1
power_supply.ch1.enable('off')

# Disconnect from the instrument
power_supply.disconnect()
```

Note: Replace `'TCPIP0::192.168.1.1::INSTR'` with the actual IP address or VISA resource string of your KEYSIGHT E36313A Power Supply.

