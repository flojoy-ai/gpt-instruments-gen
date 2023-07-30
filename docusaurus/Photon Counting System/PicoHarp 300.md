
# PicoHarp 300

## Instrument Card

The PicoHarp 300 is a high-end, easy to use, plug and play Time-Correlated Single Photon Counting (TCSPC) system. It is connected to a PC through a USB 2.0 interface. The high quality and reliability of the PicoHarp 300 is expressed by a unique 5-year limited warranty.

<details open>
<summary><h2>Manufacturer Card</h2></summary>
The PicoQuant group was founded in 1996 to develop robust, compact, and easy to use time-resolved instrumentation and systems. Since April 2008 sales and support in North America is handled by PicoQuant Photonics North America Inc. In January 2010, the PicoQuant group was extended by PicoQuant Innovations, which was founded to support the increasing activities in the field of teaching, customer support, and event organization. <a href=https://www.picoquant.com/>Website</a>.

<ul>
  <li>Headquarters: Berlin, Germany</li>
  <li>Yearly Revenue (millions, USD): 14.7</li>
</ul>
</details>

## Connect to the PicoHarp 300 in Python

[Read our guide for turning Python scripts into Flojoy nodes.](https://docs.flojoy.ai/custom-nodes/creating-custom-node/)


### Pytango

```python
import time
import numpy as np
import PyTango as pt

# Measurement parameters, these are hardcoded since this is just a demo
binning = 0  # you can change this
offset = 0
tacq = 1000  # Measurement time in millisec, you can change this
syncDivider = 1  # you can change this
CFDZeroCross0 = 10  # you can change this (in mV)
CFDLevel0 = 100  # you can change this (in mV)
CFDZeroCross1 = 10  # you can change this (in mV)
CFDLevel1 = 50  # you can change this (in mV)

# Variables to store information read from device
counts = np.zeros(65536, dtype=np.uint32)
dev = None

# Connect to the PicoHarp device
dev_name = "pico/0"  # Replace with the actual device name
dev = pt.DeviceProxy(dev_name)

# Initialize the device
dev.Initialize(0)  # MODE_HIST = 0

# Set measurement parameters
dev.SetSyncDiv(syncDivider)
dev.SetInputCFD(0, CFDLevel0, CFDZeroCross0)
dev.SetInputCFD(1, CFDLevel1, CFDZeroCross1)
dev.SetBinning(binning)
dev.SetOffset(offset)

# Get device information
hw_model = dev.GetHardwareInfo().model
hw_partno = dev.GetHardwareInfo().partno
hw_version = dev.GetHardwareInfo().version
print(f"Found Model {hw_model} Part no {hw_partno} Version {hw_version}")

# Calibrate the device
dev.Calibrate()

# Set stop overflow
dev.SetStopOverflow(1, 65535)

# Start measurement loop
cmd = ""
while cmd != "q":
    # Clear histogram memory
    dev.ClearHistMem(0)

    input("Press RETURN to start measurement")

    # Start measurement
    dev.StartMeas(tacq)

    print(f"\nMeasuring for {tacq} milliseconds...")

    # Wait for measurement to complete
    while dev.CTCStatus() == 0:
        time.sleep(0.1)

    # Stop measurement
    dev.StopMeas()

    # Get histogram data
    counts = dev.GetHistogram(0)

    # Calculate total count
    total_count = np.sum(counts)

    print(f"\nTotalCount={total_count}")

    # Check for overflow
    if dev.GetFlags() & 0x0040 > 0:
        print("Overflow.")

    cmd = input("Enter c to continue or q to quit and save the count data.")

# Close the device
dev.CloseDevice()
```

