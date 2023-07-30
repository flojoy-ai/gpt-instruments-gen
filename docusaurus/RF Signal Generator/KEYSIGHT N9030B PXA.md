
# KEYSIGHT N9030B PXA

## Instrument Card

PXA signal analyzers are ideally suited for high-performance research and development (R&D) applications in aerospace/defense and commercial wireless communications. The PXA analyzes signals over wider bandwidths, reduces measurement uncertainty, and reveals previously hidden signals with noise floor extension (NFE). Unravel complex signals through the PXA’s broad set of measurement applications and demodulation capabilities or add real-time spectrum analysis capabilities with an upgradeable option.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT N9030B PXA in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here's an example Python script that uses Qcodes to connect to a KEYSIGHT N9030B PXA RF Signal Generator:

```python
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument.parameter import Parameter
from qcodes.utils.validators import Numbers


class KeysightN9030B(VisaInstrument):
    def __init__(self, name, address, **kwargs):
        super().__init__(name, address, terminator="\n", **kwargs)

        self.add_parameter(
            name="frequency",
            get_cmd=":FREQuency?",
            set_cmd=":FREQuency {}",
            get_parser=float,
            unit="Hz",
            vals=Numbers(1e6, 26.5e9),
            docstring="Sets and gets the frequency of the signal generator.",
        )

        self.add_parameter(
            name="power",
            get_cmd=":POWer?",
            set_cmd=":POWer {}",
            get_parser=float,
            unit="dBm",
            vals=Numbers(-140, 20),
            docstring="Sets and gets the power level of the signal generator.",
        )

        self.connect_message()

    def reset(self):
        self.write("*RST")

    def on(self):
        self.write(":OUTPut:STATe ON")

    def off(self):
        self.write(":OUTPut:STATe OFF")


# Connect to the KEYSIGHT N9030B PXA RF Signal Generator
signal_generator = KeysightN9030B("signal_generator", "TCPIP0::192.168.1.1::inst0::INSTR")

# Reset the signal generator
signal_generator.reset()

# Set the frequency to 1 GHz
signal_generator.frequency(1e9)

# Set the power level to -10 dBm
signal_generator.power(-10)

# Turn on the signal generator
signal_generator.on()

# Turn off the signal generator
signal_generator.off()
```

Note: Replace `"TCPIP0::192.168.1.1::inst0::INSTR"` with the actual VISA address of your KEYSIGHT N9030B PXA RF Signal Generator.

