
# Lakeshore 370

## Instrument Card

The Model 370 AC resistance bridge is designed for precise, accurate, low noise, low excitation power AC resistance measurements. Its primary application is the measurement of resistive materials in cryogenic environments from 20 mK to 1 K. Fully integrated, the Model 370 includes features to reduce and control noise at every step of the resistance measurement process. A unique, patented, matched impedance current source and active common mode reduction circuitry minimize noise and self-heating errors. With up to 16 channels, IEEE-488 and serial interfaces, and closed loop temperature control, the Model 370 offers seamless integration with existing cryogenic systems and is the most complete package on the market today. Used with Lake Shore calibrated subkelvin resistance temperature sensors, it not only measures and displays, but also controls temperature for dilution refrigerators and other cryogenic systems.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.

<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the Lakeshore 370 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a Lakeshore 370 AC resistance bridge using Instrumentkit, you can use the following Python script:

```python
import instrumentkit as ik

# Connect to the Lakeshore 370 AC resistance bridge
bridge = ik.lakeshore.Lakeshore370.open_gpibusb('/dev/ttyUSB0', 1)

# Get the resistance of the first channel
resistance = bridge.channel[0].resistance

# Print the resistance
print(resistance)
```

This script imports the `instrumentkit` module as `ik` and uses the `open_gpibusb` method of the `Lakeshore370` class to connect to the Lakeshore 370 AC resistance bridge. The `open_gpibusb` method takes the device path (`'/dev/ttyUSB0'`) and the GPIB address (`1`) as arguments.

After connecting to the bridge, the script retrieves the resistance of the first channel using the `resistance` property of the `Channel` class. Finally, it prints the resistance value.

