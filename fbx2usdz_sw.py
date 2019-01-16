# Fbx to USDZ converter
# Version 0.0
# Scotty Wilson
# scottyw@apple.com
#######################

import os
import glob
from os import walk

# Variables #
#############

input_fbx = ""
object_name = ""

# Function to determine what assets are available
def get_fbx_asset(files_in_directory):

	has_fbx = False

	threedee_asset = ""

	for asset in files_in_directory:
		if ".fbx" in asset and not has_fbx:
			has_fbx = True
			threedee_asset = asset
			break

	print("Checking for available 3D assets:")
	print("----------")
	print("FBX: " + str(has_fbx))
	print("----------")

	return threedee_asset

# Get directory this script is located in.
cwd = os.getcwd()

# Get filename for assets to convert
files_in_directory = []
for (dirpath, dirnames, filenames) in walk(cwd):
    files_in_directory.extend(filenames)
    break

# Get fbx asset
input_fbx = get_fbx_asset(files_in_directory)

output_command_string = './FBX2glTF ' + threedee_asset

print('------------')
print('Final output string:')
print(output_command_string)

import os
os.system(output_command_string)