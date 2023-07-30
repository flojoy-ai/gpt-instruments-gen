
# Lakeshore Model 372

## Instrument Card

The Model 372 AC resistance bridge and temperature controller builds on the solid foundation provided by the original Lake Shore AC resistance bridge. The Model 372 provides the best possible temperature measurement and control capabilities for dilution refrigerators (DRs) that are intended to be operated below 100 mK. The Model 372 makes it easy to perform multiple tasks that were once very difficult to perform reliably at ultra-low temperatures:

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Supporting advanced scientific research, Lake Shore is a leading global innovator in measurement and control solutions. <a href=https://www.lakeshore.com/home>Website</a>.

<ul>
  <li>Headquarters: Westerville, Ohio, USA</li>
  <li>Yearly Revenue (millions, USD): 21.4</li>
</ul>
</details>

## Connect to the Lakeshore Model 372 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a Lakeshore Model 372 Temperature Controller using Qcodes, you can use the following Python script:

```python
import qcodes as qc
from qcodes.instrument_drivers.Lakeshore.Model_372 import LakeshoreModel372

# Create an instance of the LakeshoreModel372 driver
lakeshore = LakeshoreModel372("lakeshore", "TCPIP::192.168.1.1::7777::SOCKET")

# Connect to the instrument
lakeshore.connect()

# Print the identification string of the instrument
print(lakeshore.IDN())

# Disconnect from the instrument
lakeshore.disconnect()
```

This script creates an instance of the `LakeshoreModel372` driver, specifying the name and address of the instrument. The `connect()` method is then called to establish a connection to the instrument. The `IDN()` method is used to retrieve the identification string of the instrument, which can be printed to verify the connection. Finally, the `disconnect()` method is called to close the connection to the instrument.

