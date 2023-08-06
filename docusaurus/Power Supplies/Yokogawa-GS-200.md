
# Yokogawa GS 200

## Instrument Card

The GS200 is a low voltage/current DC source with high accuracy, high stability, and high resolution. With its excellent traceability, stability, and 5 1/2-digit resolution, the GS200 generates extremely low-noise DC voltage and current signals that are required for many applications. Additionally, the optional monitoring feature turns the GS200 into a voltage and current measuring instrument.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Yokogawa is a leading provider of Industrial Automation and Test and Measurement solutions. Combining superior technology with engineering services, project management, and maintenance, Yokogawa delivers field proven operational efficiency, safety, quality, and reliability. <a href=https://www.yokogawa.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: Japan</li>
  <li>Yearly Revenue (millions, USD): 318.0</li>
</ul>
</details>

## Connect to the Yokogawa GS 200 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
from qcodes.instrument_drivers.yokogawa.GS200 import YokogawaGS200

# Connect to the Yokogawa GS200 power supply
gs200 = YokogawaGS200("gs200", "GPIB0::1::INSTR")

# Print the output state
print(gs200.output())

# Turn on the output
gs200.output(True)

# Set the voltage to 1V
gs200.voltage(1)

# Set the current to 100mA
gs200.current(0.1)

# Ramp the voltage from 0V to 5V with a step of 1V and a delay of 1 second
gs200.ramp_voltage(5, 1, 1)

# Ramp the current from 0A to 1A with a step of 0.1A and a delay of 0.1 seconds
gs200.ramp_current(1, 0.1, 0.1)

# Turn off the output
gs200.output(False)

# Disconnect from the power supply
gs200.close()
```
Note: Make sure to replace `"GPIB0::1::INSTR"` with the actual address of your Yokogawa GS200 power supply.

