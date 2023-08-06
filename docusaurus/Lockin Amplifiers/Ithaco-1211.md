
# Ithaco 1211

## Instrument Card

The Ithaco 1211 Current Preamplifier measures current with full scale sensitivity ranging from 10-2 to 10-12 amperes

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Artisan Technology Group ® is a team of top-talent engineers and customer service specialists. We serve organizations that need to maintain and extend the life of their critical industrial, commercial, and military systems beyond obsolescence. <a href=https://www.artisantg.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 17.0</li>
</ul>
</details>

## Connect to the Ithaco 1211 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to an Ithaco 1211 Lockin Amplifier using Qcodes, you can use the following Python script:

```python
from qcodes.instrument.base import Instrument
from qcodes.instrument_drivers.ithaco.ithaco_1211 import Ithaco_1211

# Create an instance of the Ithaco_1211 instrument
ithaco = Ithaco_1211('ithaco', address='COM1')

# Connect to the instrument
ithaco.connect()

# Print the instrument's ID information
print(ithaco.get_idn())

# Set the sensitivity of the amplifier
ithaco.sens(1e-8)

# Set the output to be inverted
ithaco.invert(True)

# Set the sensitivity factor
ithaco.sens_factor(1)

# Set the suppression
ithaco.suppression(1e-7)

# Set the rise time
ithaco.risetime(0.3)

# Disconnect from the instrument
ithaco.disconnect()
```

This script creates an instance of the `Ithaco_1211` instrument, connects to it, and then performs various operations such as setting the sensitivity, inversion, sensitivity factor, suppression, and rise time. Finally, it disconnects from the instrument.

Note: Make sure to replace `'COM1'` with the appropriate address of your Ithaco 1211 Lockin Amplifier.

