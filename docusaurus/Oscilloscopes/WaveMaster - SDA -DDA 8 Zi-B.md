
# WaveMaster / SDA /DDA 8 Zi-B

## Instrument Card

The WaveMaster 8 Zi-B combines the performance, signal fidelity and feature set needed for today’s high-speed measurements with the ease of use of a standard benchtop oscilloscope. Featuring the highest-speed serial data triggers, the only complete multi-lane serial data analysis and eye diagram solution, and the most comprehensive set of compliance packages, the WaveMaster 8 Zi-B simplifies the most complex testing.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
Teledyne LeCroy is an American manufacturer of oscilloscopes, protocol analyzers and other test equipment. LeCroy is now a subsidiary of Teledyne Technologies. <a href=https://www.teledynelecroy.com/>Website</a>.
<br><br>
<ul>
  <li>Headquarters: USA</li>
  <li>Yearly Revenue (millions, USD): 5458.6</li>
</ul>
</details>

## Connect to the WaveMaster / SDA /DDA 8 Zi-B in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

To connect to a WaveMaster / SDA / DDA 8 Zi-B Oscilloscope using Instrumentkit, you can use the following code:

```python
import instrumentkit as ik

# Connect to the oscilloscope
address = "TCPIP0::192.168.0.10::INSTR"
oscilloscope = ik.teledyne.MAUI.open_visa(address)

# Perform operations on the oscilloscope
oscilloscope.run()
print(oscilloscope.trigger_state)

oscilloscope.time_div = 20 * ik.units.ns

channel = oscilloscope.channel[0]
channel.trace = True
channel.coupling = channel.Coupling.dc50
channel.scale = 1 * ik.units.V

xdat, ydat = channel.read_waveform()
```

This code connects to the oscilloscope at the specified address using the `open_visa` method from the `ik.teledyne.MAUI` module. It then performs various operations on the oscilloscope, such as starting the trigger in automatic mode, setting the timebase to 20 ns per division, and reading a waveform from the first channel.

Note: Make sure to replace `"TCPIP0::192.168.0.10::INSTR"` with the actual IP address or VISA resource string of your oscilloscope.

