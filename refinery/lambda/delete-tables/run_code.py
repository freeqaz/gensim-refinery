
# Start of Refinery Generated Code
import traceback
import json
import sys
# End of Refinery Generated Code

import yaml

from block_code import main

# Begin Refinery Generated Code
with open('input_config.yaml') as block_config_raw:
  block_config = yaml.safe_load(block_config_raw)
  input_data = block_config["input_data"]
  backpack_data = block_config["backpack_data"]

output_data = main(input_data, backpack_data)

print(json.dumps(output_data, indent=2))
# End Refinery Generated Code
