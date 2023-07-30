
# M5180 2-Port 18 GHz Analyzer

## Instrument Card

The M5180 is a 2-port, 18 GHz Vector Network Analyzer that delivers metrology-grade performance in a more economical package that excludes a number of advanced features

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Copper Mountain Technologies** develops innovative RF test and measurement solutions for engineers worldwide that enable engineers to extend their reach. <a href=https://coppermountaintech.com/>Website</a>.
<br>
<ul>
  <li>Headquarters: US</li>
  <li>Yearly Revenue (millions, USD): 301.0</li>
</ul>
</details>

## Connect to the M5180 2-Port 18 GHz Analyzer in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

```python
from qcodes import Station
from qcodes.instrument_drivers.CopperMountain.M5180 import M5180

# Create a station to hold the instruments
station = Station()

# Connect to the M5180 instrument
m5180 = M5180('m5180', 'TCPIP0::192.168.1.1::inst0::INSTR')
station.add_component(m5180)

# Print the available parameters of the M5180 instrument
print(m5180.parameters)

# Set the start frequency to 1 GHz
m5180.start(1e9)

# Set the stop frequency to 10 GHz
m5180.stop(10e9)

# Set the number of points to 1001
m5180.npts(1001)

# Perform a frequency sweep and get the S-parameters
freq, s11_mag, s11_phase, s12_mag, s12_phase, s21_mag, s21_phase, s22_mag, s22_phase = m5180.get_s()

# Print the S11 magnitude and phase at the first frequency point
print(f"S11 magnitude: {s11_mag[0]} dB")
print(f"S11 phase: {s11_phase[0]} rad")

# Perform a single point measurement and get the S-parameters
point_s11_mag, point_s11_phase = m5180.point_s11()

# Print the S11 magnitude and phase at the single point
print(f"Point S11 magnitude: {point_s11_mag} dB")
print(f"Point S11 phase: {point_s11_phase} rad")
```
Note: Replace `'TCPIP0::192.168.1.1::inst0::INSTR'` with the actual IP address or VISA resource string of your M5180 instrument.

