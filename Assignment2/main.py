# Refactor code

# An intern has provided the code below to update the version number
# within two different files.
# The intern has left and you need to review and improve the code before
# submitting to source control.
#
# Please do not be constrained by the existing code (i.e. you don't have
# to keep the same function names, structure)
#
# Original Requirements
# ---------------------
# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)

import os
import re
# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

def update_file_version(filename,pattern,replacement):
    """Update the build number in the file"""

    filepath = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")
    # just following previous implementation
    temp_fp = os.path.join(os.environ["SourcePath"], "develop", "global", "src", filename + "1") 
    os.chmod(filepath,0755)
    
    with open( filepath, 'r') as fin:
        with open(temp_fp, 'w') as fout:
            for line in fin:
                line = re.sub(pattern, replacement, line)
                fout.write(line)
    
    os.remove(filepath)
    os.rename(temp_fp, filepath)
    os.chmod(filepath, 0755)


def updateSconstruct():
    "Update the build number in the SConstruct file"
    update_file_version(
        "SConstruct",
        "point\=[\d]+",
        "point="+os.environ["BuildNum"]
    )
    
# ADLMSDK_VERSION_POINT=6
def updateVersion():
    "Update the build number in the VERSION file"
    update_file_version(
        "VERSION",
        "ADLMSDK_VERSION_POINT=[\d]+",
        "ADLMSDK_VERSION_POINT="+os.environ["BuildNum"]
    )


def main():
    updateSconstruct()
    updateVersion()

main()