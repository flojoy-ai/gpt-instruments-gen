
# KEYSIGHT 34980A Submodules

## Instrument Card

The Keysight 34980A Multifunction Switch/Measure unit is designed for R&D and
manufacturing test engineers who are working in design verification, automated
test or data acquisition and are either looking to upgrade their existing systems or
are in need of a new, cost-effective alternative

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT 34980A Submodules in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

To connect to a KEYSIGHT 34980A Submodule DAQ board using Qcodes, you can use the following Python script:

```python
from qcodes import VisaInstrument, InstrumentChannel
from typing import Union, List, Tuple, Optional


class KeysightSubModule(InstrumentChannel):
    # ... (code omitted for brevity)


class KeysightSwitchMatrixSubModule(KeysightSubModule):
    # ... (code omitted for brevity)


# Create an instance of the KEYSIGHT 34980A Submodule DAQ board
submodule = KeysightSwitchMatrixSubModule(parent=None, name='Submodule', slot=1)

# Connect to the instrument
submodule.connect()

# Check if a channel is open/disconnected
is_open = submodule.is_open(row=1, column=2)
print(f"Channel (1, 2) is open: {is_open}")

# Check if a channel is closed/connected
is_closed = submodule.is_closed(row=1, column=2)
print(f"Channel (1, 2) is closed: {is_closed}")

# Connect a specific channel
submodule.connect(row=1, column=2)

# Disconnect a specific channel
submodule.disconnect(row=1, column=2)

# Connect multiple channels
submodule.connect_paths([(1, 2), (3, 4), (5, 6)])

# Disconnect multiple channels
submodule.disconnect_paths([(1, 2), (3, 4), (5, 6)])

# Check if multiple channels are closed/connected
are_closed = submodule.are_closed([(1, 2), (3, 4), (5, 6)])
print(f"Channels [(1, 2), (3, 4), (5, 6)] are closed: {are_closed}")

# Check if multiple channels are open/disconnected
are_open = submodule.are_open([(1, 2), (3, 4), (5, 6)])
print(f"Channels [(1, 2), (3, 4), (5, 6)] are open: {are_open}")
```

This script creates an instance of the `KeysightSwitchMatrixSubModule` class, which is a subclass of `KeysightSubModule` and `InstrumentChannel`. It then connects to the KEYSIGHT 34980A Submodule DAQ board and performs various operations such as checking the status of channels, connecting and disconnecting channels, and checking the status of multiple channels.

Note: The `parent` argument in the `KeysightSubModule` constructor should be set to the appropriate parent instrument or channel object.

