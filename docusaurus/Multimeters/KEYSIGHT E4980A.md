
# KEYSIGHT E4980A

## Instrument Card

The E4980A precision LCR meter provides the best combination of accuracy, speed, and versatility for a wide range of component measurements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Keysight Technologies, or Keysight, is an American company that manufactures electronics test and measurement equipment and software. <a href=https://www.keysight.com/us/en/home.html>Website</a>.
<br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5420.0</li>
</ul>
</details>

## Connect to the KEYSIGHT E4980A in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pymeasure


```python
from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import strict_discrete_set, strict_range
from pyvisa.errors import VisaIOError

class AgilentE4980(Instrument):
    """Represents LCR meter E4980A/AL"""

    ac_voltage = Instrument.control(":VOLT:LEV?", ":VOLT:LEV %g",
                                    "AC voltage level, in Volts",
                                    validator=strict_range,
                                    values=[0, 20])

    ac_current = Instrument.control(":CURR:LEV?", ":CURR:LEV %g",
                                    "AC current level, in Amps",
                                    validator=strict_range,
                                    values=[0, 0.1])

    frequency = Instrument.control(":FREQ:CW?", ":FREQ:CW %g",
                                   "AC frequency (range depending on model), in Hertz",
                                   validator=strict_range,
                                   values=[20, 2e6])

    impedance = Instrument.measurement(
        ":FETCH?",
        "Measured data A and B, according to :attr:`~.AgilentE4980.mode`",
        get_process=lambda x: x[:2])

    mode = Instrument.control("FUNCtion:IMPedance:TYPE?", "FUNCtion:IMPedance:TYPE %s",
                              """
Select quantities to be measured:
...
""",
                              validator=strict_discrete_set,
                              values=["CPD", "CPQ", "CPG", "CPRP",
                                      "CSD", "CSQ", "CSRS",
                                      "LPD", "LPQ", "LPG", "LPRP",
                                      "LSD", "LSQ", "LSRS",
                                      "RX", "ZTD", "ZTR", "GB", "YTD", "YTR", ])

    trigger_source = Instrument.control("TRIG:SOUR?", "TRIG:SOUR %s",
                                        """
Select trigger source; accept the values:
    * HOLD: manual
    * INT: internal
    * BUS: external bus (GPIB/LAN/USB)
    * EXT: external connector""",
                                        validator=strict_discrete_set,
                                        values=["HOLD", "INT", "BUS", "EXT"])

    def __init__(self, adapter, name="Agilent E4980A/AL LCR meter", **kwargs):
        super().__init__(
            adapter, name, **kwargs
        )
        self.timeout = 30000
        self.write("FORM ASC")

    def freq_sweep(self, freq_list, return_freq=False):
        """
        Run frequency list sweep using sequential trigger.
        ...
        """

    def aperture(self, time=None, averages=1):
        """
        Set and get aperture.
        ...
        """

# Connect to the instrument
from pymeasure.adapters import VISAAdapter

adapter = VISAAdapter("GPIB::1::INSTR")
meter = AgilentE4980(adapter)

# Set the AC voltage level
meter.ac_voltage = 10

# Set the AC current level
meter.ac_current = 0.05

# Set the frequency
meter.frequency = 1000

# Set the measurement mode
meter.mode = "CPD"

# Set the trigger source
meter.trigger_source = "INT"

# Perform a frequency sweep
freq_list = [100, 1000, 10000]
a_data, b_data = meter.freq_sweep(freq_list)

# Get the impedance measurement
impedance = meter.impedance

# Set the aperture
meter.aperture(time="SHORT", averages=10)

# Disconnect from the instrument
meter.disconnect()
```

This script connects to the KEYSIGHT E4980A LCR meter using the VISAAdapter from Pymeasure. It then sets various instrument parameters such as AC voltage level, AC current level, frequency, measurement mode, and trigger source. It also performs a frequency sweep and retrieves the impedance measurement. Finally, it sets the aperture and disconnects from the instrument.

### Qcodes

```python
from qcodes.instrument_drivers.Keysight.Keysight_E4980A import Keysight_E4980A

# Connect to the instrument
instrument = Keysight_E4980A("instrument_name", "TCPIP0::192.168.1.1::inst0::INSTR")

# Print the instrument ID
print(instrument.IDN())

# Set the frequency
instrument.frequency(1000)

# Set the voltage level
instrument.voltage_level(1)

# Set the current level
instrument.current_level(0.01)

# Perform a measurement
measurement = instrument.measure_impedance()
print(measurement.get())

# Enable DC bias
instrument.dc_bias_enabled(True)

# Set the DC bias voltage level
instrument.dc_bias_voltage_level(10)

# Perform another measurement
measurement = instrument.measure_impedance()
print(measurement.get())

# Disconnect from the instrument
instrument.close()
```
Note: Replace `"instrument_name"` and `"TCPIP0::192.168.1.1::inst0::INSTR"` with the appropriate values for your instrument.

