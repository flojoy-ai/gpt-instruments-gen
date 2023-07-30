
# Keithley 485

## Instrument Card

The Keithley 485 Autoranging Picoammeter provides 100fA sensitivity with 4 1/2-digit resolution in a low-cost, highly sensitive, easy-to-use instrument. The 485 measures DC current on seven ranges covering 10 decades from 100fA to 2mA. The input can withstand overloads as high as 1000V (with 100kΩ limiting resistor) for flexibility in a wide range of applications in test, research, and student labs. An analog output linearly converts the incoming current to voltage for hard copy output or control loop applications.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.

<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the Keithley 485 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
import instrumentkit as ik

# Connect to the Keithley 485 picoammeter
inst = ik.keithley.Keithley485.open_gpibusb("/dev/ttyUSB0", 22)

# Set the input range to 2e-9 A
inst.input_range = "2e-9"

# Enable zero check mode
inst.zero_check = True

# Enable log mode
inst.log = True

# Enable relative mode
inst.relative = True

# Set the trigger mode to continuous on talk
inst.trigger_mode = "continuous_ontalk"

# Perform a current measurement
measurement = inst.measure()

# Print the measurement result
print(measurement)
```

This script connects to the Keithley 485 picoammeter using the `open_gpibusb` method from the `ik.keithley.Keithley485` class. It then sets various properties of the picoammeter, such as the input range, zero check mode, log mode, relative mode, and trigger mode. Finally, it performs a current measurement using the `measure` method and prints the result.

Note: This script assumes that you have already installed the Instrumentkit library and have the necessary permissions to access the GPIB device at `/dev/ttyUSB0`.

