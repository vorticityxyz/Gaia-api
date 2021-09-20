import segyio
import numpy as np

input_file = ""
output_file = ""

with segyio.open(input_file, "r") as f:
    data = segyio.tools.cube(f)

np.save(output_file, data)
