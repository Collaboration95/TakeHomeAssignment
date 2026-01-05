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
import uuid
from dataclasses import dataclass


@dataclass
class Config:
    source_path: str
    source_dir: str  # computed property
    build_num: str

    def __post_init__(self):
        self.source_dir = os.path.join(self.source_path, "develop", "global", "src")

def update_file_version(filename,pattern,replacement, source_dir):
    """Update the build number in the file"""
    print(f"Updating file: {filename}")

    filepath = os.path.join(source_dir,filename)
    # just following previous implementation
    temp_fp = os.path.join(source_dir, filename + str(uuid.uuid4())) 

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    os.chmod(filepath,0o755)
    try:
        with open( filepath, 'r') as fin:
            with open(temp_fp, 'w') as fout:
                for line in fin:
                    line = re.sub(pattern, replacement, line)
                    fout.write(line)
        
        os.remove(filepath)
        os.rename(temp_fp, filepath)
        print(f"Successfully updated file: {filename}")
    except Exception as e:
        if os.path.exists(temp_fp):
            os.remove(temp_fp)
        print(f"Error updating file: {filename}. {e}")
        sys.exit(1)

def updateSconstruct(config: Config):
    "Update the build number in the SConstruct file"
    update_file_version("SConstruct", "point\=[\d]+", "point="+config.build_num, config.source_dir)
    
# ADLMSDK_VERSION_POINT=6
def updateVersion(config: Config):
    "Update the build number in the VERSION file"
    update_file_version("VERSION", "ADLMSDK_VERSION_POINT=[\d]+", "ADLMSDK_VERSION_POINT="+config.build_num, config.source_dir)

def create_config() -> Config:
    """Create and validate configuration from environment variables."""
    build_num = os.environ.get("BuildNum")
    if not build_num:
        raise ValueError("BuildNum environment variable is not set")
    if not build_num.isdigit():
        raise ValueError(f"BuildNum must be a positive integer, got '{build_num}'")
    # Validate Source path 
    source_path = os.environ.get("SourcePath")
    if not source_path:
        raise ValueError("SourcePath environment variable is not set")
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source path {source_path} not found")
    if not os.path.isdir(source_path):
        raise ValueError(f"SourcePath {source_path} is not a directory")
    
    # Create version object (you can enhance this to parse from existing files)
    return Config(    
        source_path=source_path,
        build_num=build_num
    )


def main():
    print("----Starting version update process...------")
    try:
        config = create_config()
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}. Exiting...")
        sys.exit(1)
    updateSconstruct(config)
    updateVersion(config)
    print("----Version update process completed successfully----")


if __name__ == "__main__":
    main()