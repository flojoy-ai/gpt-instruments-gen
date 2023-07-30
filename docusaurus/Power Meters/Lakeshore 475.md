
# Lakeshore 475

## Instrument Card

Lake Shore combined the technical advantages of digital signal processing with over a decade of experience in precision magnetic field measurements to produce the first commercial digital signal processor (DSP) based Hall effect gaussmeter, the Model 475. DSP technology creates a solid foundation for accurate, stable, and repeatable field measurement while simultaneously enabling the gaussmeter to offer an unequaled set of useful measurement features. The Model 475 is intended for the most demanding DC and AC applications. In many cases, it provides the functionality of two or more instruments in a field measurement system.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.

<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the Lakeshore 475 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
import instrumentkit as ik
import instrumentkit.devices as ik_dev
import instrumentkit.io as ik_io
import instrumentkit.io.serial as ik_serial

# Create a serial connection to the Lakeshore 475 Gaussmeter
serial_conn = ik_serial.SerialConnection(port='/dev/ttyUSB0', baudrate=9600)
lakeshore = ik_dev.Lakeshore475(connection=serial_conn)

# Open the connection to the Gaussmeter
lakeshore.open()

# Read the field value from the connected probe
field = lakeshore.field
print(f"Field: {field}")

# Set the field units to Tesla
lakeshore.field_units = ik.units.tesla

# Set the field setpoint to 0.05 Tesla
lakeshore.field_setpoint = 0.05 * ik.units.tesla

# Close the connection to the Gaussmeter
lakeshore.close()
```

Note: This code assumes that you have already installed the Instrumentkit library.

