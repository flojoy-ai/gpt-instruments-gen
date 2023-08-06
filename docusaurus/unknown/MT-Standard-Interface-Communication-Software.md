
# MT Standard Interface Communication Software

## Instrument Card

Instrument class to communicate with Mettler Toledo balances using the MT-SICS Standared Interface Command Set.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
. <a href=nan>Website</a>.
<br><br>
<ul>
  <li>Headquarters: nan</li>
  <li>Yearly Revenue (millions, USD): nan</li>
</ul>
</details>

## Connect to the MT Standard Interface Communication Software in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit

Here is an example Python script that uses Instrumentkit to connect to a Mettler Toledo balance using the MT Standard Interface Communication Software:

```python
import instrumentkit as ik

# Open a serial connection to the balance
inst = ik.mettler_toledo.MTSICS.open_serial('/dev/ttyUSB0', 9600)

# Perform operations on the balance
inst.clear_tare()
inst.reset()
inst.tare()
inst.zero()

# Get information from the balance
mt_sics_info = inst.mt_sics
mt_sics_commands = inst.mt_sics_commands
balance_name = inst.name
serial_number = inst.serial_number
tare_value = inst.tare_value
weight = inst.weight
weight_mode = inst.weight_mode

# Close the connection to the balance
inst.close()
```

Note: This script assumes that you have installed the `instrumentkit` package and imported it as `ik`.

