
# Aguc 2

## Instrument Card



<details open>
<summary><h2>Manufacturer Card</h2></summary>
Newport provides a wide range of photonics technology and products designed to enhance the capabilities and productivity of our customers' applications. <a href=https://www.newport.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: Irvine, California, United States</li>
  <li>Yearly Revenue (millions, USD): 3500.0</li>
</ul>
</details>

## Connect to the Aguc 2 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
from instrumentkit import Agilent

# Create an instance of the Agilent instrument
instrument = Agilent()

# Connect to the instrument
instrument.connect()

# Perform some operations with the instrument
instrument.write("SYST:REM")  # Set the instrument to remote mode
instrument.write("CONF:VOLT:DC")  # Configure the instrument for DC voltage measurement
instrument.write("INIT")  # Initiate the measurement
voltage = instrument.query("FETC?")  # Fetch the measurement result

# Print the measurement result
print("Voltage: ", voltage)

# Disconnect from the instrument
instrument.disconnect()
```

In this example, we first import the `Agilent` class from the `instrumentkit` module. We then create an instance of the `Agilent` instrument and connect to it using the `connect()` method.

After connecting, we can perform various operations with the instrument. In this example, we set the instrument to remote mode, configure it for DC voltage measurement, initiate the measurement, and fetch the measurement result using the `write()` and `query()` methods.

Finally, we print the measurement result and disconnect from the instrument using the `disconnect()` method.

Note: This code assumes that you have already installed the `instrumentkit` package. If not, you can install it using `pip install instrumentkit`.

