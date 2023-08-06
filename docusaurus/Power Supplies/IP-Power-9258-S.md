
# IP Power 9258 S

## Instrument Card

IP9258 is a web controller which can be easily used in the industry field

<details open>
<summary><h2>Manufacturer Card</h2></summary>
**Aviosys** IP POWER is a remote power management device that allows you to control power on/off and monitor power status of connected devices. <a href=https://www.aviosys.com/>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Taiwan</li>
  <li>Yearly Revenue (millions, USD): 5.0</li>
</ul>
</details>

## Connect to the IP Power 9258 S in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes Community

To connect to an Aviosys IP Power 9258S power supply using Qcodes Community, you can use the following Python script:

```python
from qcodes import Station
from qcodes.instrument_drivers.Aviosys_IP_Power_9258S import Aviosys_IP_Power_9258S

# Create a station to hold the instrument
station = Station()

# Define the instrument settings
instrument_name = 'power_supply'
address = 'http://<ip_address>'
login_name = '<login_name>'
login_password = '<login_password>'

# Create the instrument instance
power_supply = Aviosys_IP_Power_9258S(instrument_name, address, login_name, login_password)

# Add the instrument to the station
station.add_component(power_supply)

# Connect to the instrument
power_supply.connect()

# Access the power channels
channel_A = power_supply.channels.ChanA
channel_B = power_supply.channels.ChanB

# Turn on channel A
channel_A.power_enabled.set(1)

# Turn off channel B
channel_B.power_enabled.set(0)

# Disconnect from the instrument
power_supply.disconnect()
```

Make sure to replace `<ip_address>`, `<login_name>`, and `<login_password>` with the actual IP address, login name, and login password of your Aviosys IP Power 9258S power supply.

