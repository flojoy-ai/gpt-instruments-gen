
# Mercuryips Visa

## Instrument Card



<details open>
<summary><h2>Manufacturer Card</h2></summary>
Oxford Instruments plc is a United Kingdom manufacturing and research company that designs and manufactures tools and systems for industry and research. The company is headquartered in Abingdon, Oxfordshire, England, with sites in the United Kingdom, United States, Europe, and Asia.[2] It is listed on the London Stock Exchange and is a constituent of the FTSE 250 Index.[3]. <a href=https://www.oxinst.com/>Website</a>.

<ul>
  <li>Headquarters: Abingdon, United Kingdom</li>
  <li>Yearly Revenue (millions, USD): 367.3</li>
</ul>
</details>

## Connect to the Mercuryips Visa in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Qcodes

```python
import qcodes as qc
from qcodes.instrument.visa import VisaInstrument

# Connect to the Mercuryips Visa instrument
mercuryips = VisaInstrument('mercuryips', 'TCPIP0::192.168.1.1::inst0::INSTR')

# Open communication with the instrument
mercuryips.open()

# Perform operations with the instrument

# Close communication with the instrument
mercuryips.close()
```

Explanation:
1. Import the necessary modules: `qcodes` and `VisaInstrument` from `qcodes.instrument.visa`.
2. Create an instance of the `VisaInstrument` class and assign it to the variable `mercuryips`. Provide a name for the instrument ('mercuryips') and the VISA address of the instrument ('TCPIP0::192.168.1.1::inst0::INSTR').
3. Open communication with the instrument using the `open()` method.
4. Perform any desired operations with the instrument.
5. Close communication with the instrument using the `close()` method.

