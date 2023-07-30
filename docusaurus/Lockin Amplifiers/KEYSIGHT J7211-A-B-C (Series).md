
# KEYSIGHT J7211/A/B/C (Series)

## Instrument Card



<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT J7211/A/B/C (Series) in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to a KEYSIGHT J7211/A/B/C Lockin Amplifier using Qcodes Community, you can use the following Python script:

```python
from qcodes.instrument.visa import VisaInstrument
from qcodes.utils.validators import Ints
from typing import Optional


class Keysight_J7211(VisaInstrument):
    r"""
    Qcodes driver for the Keysight J7211 Attenuation Control Unit.
    Tested with J7211B.

    Args:
        name: Instrument name
        address: Address or VISA alias of instrument
        attenuation: Optional attenuation level (in dB) to set on startup
        terminator: Termination character in VISA communication.
    """

    def __init__(self, name: str, address: str,
                 attenuation: Optional[int] = None,
                 terminator="\r", **kwargs):
        super().__init__(name=name, address=address,
                         terminator=terminator, **kwargs)

        model = self.IDN()['model']
        if model in ["J7211A", "J7211B"]:
            vals = Ints(0, 120)
        elif model in ["J7211C"]:
            vals = Ints(0, 100)
        else:
            raise RuntimeError(f"Model {model} is not supported.")

        self.add_parameter('attenuation', unit='dB',
                           set_cmd='ATT {:03.0f}',
                           get_cmd='ATT?',
                           get_parser=int,
                           vals=vals,
                           initial_value=attenuation)

        self.connect_message()
```

This script defines a class `Keysight_J7211` that inherits from `VisaInstrument` in the `qcodes.instrument.visa` module. The class represents the KEYSIGHT J7211 Attenuation Control Unit.

To use this class, you need to create an instance of it by providing the necessary arguments:

- `name`: The name of the instrument.
- `address`: The address or VISA alias of the instrument.
- `attenuation` (optional): The attenuation level (in dB) to set on startup.
- `terminator`: The termination character in VISA communication.

Once you have created an instance of `Keysight_J7211`, you can access and control the instrument using its parameters. In this case, the only parameter defined is `attenuation`, which represents the attenuation level of the control unit. It has the following properties:

- `unit`: The unit of the attenuation level (dB).
- `set_cmd`: The command to set the attenuation level, using the format `'ATT {:03.0f}'`.
- `get_cmd`: The command to get the current attenuation level.
- `get_parser`: The function to parse the response of the `get_cmd` into an integer.
- `vals`: The range of valid attenuation values based on the model of the control unit.
- `initial_value`: The initial attenuation level to set on startup.

You can connect to the instrument by calling the `connect_message()` method.

Note: This script only defines the class and its parameters. To use it, you need to create an instance of the class and interact with the instrument accordingly.

