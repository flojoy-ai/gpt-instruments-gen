
# KEYSIGHT N5767A

## Instrument Card

The single output, 1500 W N5767A, provides universal AC input, GPIB, LAN, USB, LXI compliance, and analog/resistance control of output voltage and current. It delivers reliable performance and enhanced capabilities in a compact 1U package.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N5767A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure

Here is a Python script that uses Pymeasure to connect to a KEYSIGHT N5767A Power Supply:

```python
import logging
from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import truncated_range
from pymeasure.adapters import VISAAdapter

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class KeysightN5767A(Instrument):
    """ Represents the Keysight N5767A Power supply
    interface for interacting with the instrument.
    """

    # Current (A)
    current_range = Instrument.control(
        ":CURR?", ":CURR %g",
        """ A floating point property that controls the DC current range in
        Amps, which can take values from 0 to 25 A.
        Auto-range is disabled when this property is set. """,
        validator=truncated_range,
        values=[0, 25],
    )

    current = Instrument.measurement(":MEAS:CURR?",
                                     """ Reads a setting current in Amps. """
                                     )

    # Voltage (V)
    voltage_range = Instrument.control(
        ":VOLT?", ":VOLT %g V",
        """ A floating point property that controls the DC voltage range in
        Volts, which can take values from 0 to 60 V.
        Auto-range is disabled when this property is set. """,
        validator=truncated_range,
        values=[0, 60]
    )

    voltage = Instrument.measurement("MEAS:VOLT?",
                                     """ Reads a DC voltage measurement in Volts. """
                                     )

    # _status (0/1)
    _status = Instrument.measurement(":OUTP?",
                                     """ Read power supply current output status. """
                                     )

    def enable(self):
        """ Enables the flow of current.
        """
        self.write(":OUTP 1")

    def disable(self):
        """ Disables the flow of current.
        """
        self.write(":OUTP 0")

    def is_enabled(self):
        """ Returns True if the current supply is enabled.
        """
        return bool(self._status)

    def __init__(self, adapter, name="Keysight N5767A power supply", **kwargs):
        super().__init__(
            adapter, name, **kwargs
        )
        # Set up data transfer format
        if isinstance(self.adapter, VISAAdapter):
            self.adapter.config(
                is_binary=False,
                datatype='float32',
                converter='f',
                separator=','
            )
```

This script defines a class `KeysightN5767A` that represents the KEYSIGHT N5767A Power Supply. It provides methods and properties to control and measure the current and voltage of the power supply.

To use this script, you need to have Pymeasure installed and import the necessary modules. Then, you can create an instance of the `KeysightN5767A` class and use its methods and properties to interact with the power supply.

