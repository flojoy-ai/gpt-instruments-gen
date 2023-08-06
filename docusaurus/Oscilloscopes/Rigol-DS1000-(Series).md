
# Rigol DS1000 (Series)

## Instrument Card

The 1000 Series from RIGOL include the B, D, and E series oscilloscopes. The E Series are the value leader with 50-100 MHz models that include 2 channels and 1 Million points of memory. The D Series add low speed digital capture enabling basic mixed signal analysis in a economic package. The B Series provide more speed and power including our economic 4 channel, 200 MHz DS1204B model which provides 2 GSa/sec sampling. With features including FFTs, record and replay, roll mode, alternate trigger mode, and adjustable trigger sensitivity the 1000 Series is a great entry for value oscilloscope requirements.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
RIGOL Technologies, Inc. specializes in development and production of test and measuring equipment and is one of the fastest growing Chinese companies in this sphere.
RIGOL’s line of products includes [digital storage oscilloscopes](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=227), [function/arbitrary waveform generators](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=230), [digital multimeters](https://www.tmatlantic.com/e-store/index.php?SECTION_ID=233), PC-based devices compatible with LXI standard etc. <a href=https://www.rigol.com/>Website</a>.
<br></br>
<ul>
  <li>Headquarters: Beijing, China</li>
  <li>Yearly Revenue (millions, USD): 23.0</li>
</ul>
</details>

## Connect to the Rigol DS1000 (Series) in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Instrumentkit


```python
from instrumentkit import RigolDS1000Series

# Connect to the oscilloscope
oscilloscope = RigolDS1000Series("USB0::0x1AB1::0x0588::DS1ED141904883::INSTR")

# Print the available channels
print("Available channels:")
for channel in oscilloscope.channel:
    print(channel.name)

# Set the acquisition type to normal
oscilloscope.acquire_type = RigolDS1000Series.AcquisitionType.normal

# Set the number of averages to 8
oscilloscope.acquire_averages = 8

# Force a trigger
oscilloscope.force_trigger()

# Start running the oscilloscope trigger
oscilloscope.run()

# Stop the oscilloscope trigger
oscilloscope.stop()

# Release any lockout of the local control panel
oscilloscope.release_panel()

# Disconnect from the oscilloscope
oscilloscope.disconnect()
```

Note: Replace `"USB0::0x1AB1::0x0588::DS1ED141904883::INSTR"` with the actual VISA resource string of your oscilloscope.

