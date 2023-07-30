
# USB SA 124 B

## Instrument Card

The Signal Hound USB-SA44B is a Software Defined Receiver (SDR) optimized as a narrow-band real-time RF spectrum analyzer. It is a compact, simple to use, effective troubleshooting tool for the general lab user, engineering students, and ham radio enthusiast.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Signal Hound is a manufacturer of RF spectrum analyzers and signal generators. <a href=https://signalhound.com/>Website</a>.

<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 3.6</li>
</ul>
</details>

## Connect to the USB SA 124 B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument_drivers.signal_hound.USB_SA124B import SignalHoundUSBSA124B

# Create an instance of the SignalHoundUSBSA124B instrument
sa = SignalHoundUSBSA124B("sa", dll_path="C:\\Program Files\\Signal Hound\\Spike\\sa_api.dll")

# Connect to the instrument
sa.connect()

# Print the instrument IDN
print(sa.get_idn())

# Configure the instrument parameters
sa.frequency(1e9)
sa.span(1e6)
sa.rbw(1e3)
sa.vbw(1e3)
sa.ref_lvl(0)
sa.external_reference(False)
sa.scale("log-scale")

# Perform a frequency sweep and get the data
data = sa.freq_sweep()

# Print the data
print(data)

# Disconnect from the instrument
sa.disconnect()
```
Note: Make sure to replace the `dll_path` argument with the correct path to the `sa_api.dll` file on your system.

