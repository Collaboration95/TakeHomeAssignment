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
import sys
# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

def update_file_version(filename,pattern,replacement, source_path):
    """Update the build number in the file"""
    print(f"Updating file: {filename}")

    filepath = os.path.join(source_path,"develop","global","src",filename)
    # just following previous implementation
    temp_fp = os.path.join(source_path, "develop", "global", "src", filename + "1") 

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    os.chmod(filepath,0o755)

    with open( filepath, 'r') as fin:
        with open(temp_fp, 'w') as fout:
            for line in fin:
                line = re.sub(pattern, replacement, line)
                fout.write(line)
    
    os.remove(filepath)
    os.rename(temp_fp, filepath)
    print(f"Successfully updated file: {filename}")
    
def _check_build_number():
    """Helper function to validate BuildNum variable"""
    build_num = os.environ.get("BuildNum")
    if not build_num:
        raise ValueError("BuildNum environment variable is not set")
    if not build_num.isdigit():
        raise ValueError("BuildNum environment variable is not a number")
    print(f"Build number: {build_num}")
    return build_num

def _check_source_path():
    """Helper function to validate SourcePath variable"""
    source_path = os.environ.get("SourcePath")
    if not source_path:
        raise ValueError("SourcePath environment variable is not set")
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source path {source_path} not found")
    if not os.path.isdir(source_path):
        raise ValueError("SourcePath environment variable is not a directory")
    print(f"Source path is validated : {source_path}")
    return source_path

def updateSconstruct(build_num, source_path):
    "Update the build number in the SConstruct file"
    update_file_version("SConstruct", "point\=[\d]+", "point="+build_num, source_path)
    
# ADLMSDK_VERSION_POINT=6
def updateVersion(build_num, source_path):
    "Update the build number in the VERSION file"
    update_file_version("VERSION", "ADLMSDK_VERSION_POINT=[\d]+", "ADLMSDK_VERSION_POINT="+build_num, source_path)


def main():
    print("----Starting version update process...------")
    try:
        build_num = _check_build_number()
        source_path = _check_source_path()
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}. Exiting...")
        sys.exit(1)
    updateSconstruct(build_num, source_path)
    updateVersion(build_num, source_path)
    print("----Version update process completed successfully----")


if __name__ == "__main__":
    main()