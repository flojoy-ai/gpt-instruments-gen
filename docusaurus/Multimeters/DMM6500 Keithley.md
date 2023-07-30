
# DMM6500 Keithley

## Instrument Card

6½ digit bench/system digital multimeter with large 5" (12.7cm) multi touch capacitive touchscreen and graphical display. It supports SCPI, TSP® scripting, Keithley 2000 SCPI emulation and Keysight 34401A SCPI emulation language modes.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keithley Instruments is a measurement and instrument company headquartered in Solon, Ohio, that develops, manufactures, markets, and sells data acquisition products, as well as complete systems for high-volume production and assembly testing. <a href=https://www.tek.com/en>Website</a>.

<ul>
  <li>Headquarters: Cleveland, Ohio, United States</li>
  <li>Yearly Revenue (millions, USD): 110.6</li>
</ul>
</details>

## Connect to the DMM6500 Keithley in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

Here is a Python script that uses Qcodes to connect to a Keithley DMM6500 Multimeter:

```python
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument.parameter import Parameter
from qcodes.utils.validators import Numbers


class KeithleyDMM6500(VisaInstrument):
    def __init__(self, name, address, **kwargs):
        super().__init__(name, address, terminator="\n", **kwargs)

        self.add_parameter(
            "voltage",
            get_cmd="MEAS:VOLT:DC?",
            get_parser=float,
            unit="V",
            vals=Numbers(),
        )

        self.add_parameter(
            "current",
            get_cmd="MEAS:CURR:DC?",
            get_parser=float,
            unit="A",
            vals=Numbers(),
        )

        self.add_parameter(
            "resistance",
            get_cmd="MEAS:RES?",
            get_parser=float,
            unit="Ohm",
            vals=Numbers(),
        )

        self.connect_message()

    def reset(self):
        self.write("*RST")


# Connect to the Keithley DMM6500
dmm = KeithleyDMM6500("dmm", "TCPIP0::192.168.1.1::INSTR")

# Reset the device
dmm.reset()

# Read voltage
voltage = dmm.voltage()
print("Voltage:", voltage)

# Read current
current = dmm.current()
print("Current:", current)

# Read resistance
resistance = dmm.resistance()
print("Resistance:", resistance)

# Close the connection
dmm.close()
```

This script creates a custom instrument class `KeithleyDMM6500` that inherits from `VisaInstrument`. It adds three parameters: `voltage`, `current`, and `resistance`, which are used to measure the corresponding quantities using the `MEAS` commands of the Keithley DMM6500.

The script then creates an instance of `KeithleyDMM6500` and connects to the instrument using the specified address. It resets the device, reads the voltage, current, and resistance values, and prints them. Finally, it closes the connection to the instrument.

