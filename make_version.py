#! -*- coding: UTF_8 -*-

import json
import os
import sys
from distutils.version import StrictVersion


def usage(exit_code):
    print("""usage:     script.py DIR OUT_FILE

DIR             The directory containing all version directories
OUT_FILE        The path to the json where versions discovered will be stored
""", file=sys.stderr)
    sys.exit(exit_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(1)

    directory = sys.argv[1]
    out_path = sys.argv[2]

    if os.path.exists(directory):
        # When the directory exists find all versions
        all_versions = []

        # Read all entries and find directories
        for entry in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, entry)):
                all_versions.append(entry)
        
        # Exclude non strict version name and append them to the final list of verions
        versions = []
        for version in ['latest', 'stable']:
            if version in all_versions:
                versions.append(version)
                all_versions.remove(version)
        
        # Generate the final list of versions by sorting in reverse mode
        #   This generate latest to oldest sorted version list
        versions += sorted(all_versions, key=StrictVersion, reverse=True)

        # Write the file to second parameter
        with open(out_path, 'w') as f:
            json.dump({"versions": versions}, f, separators=(',', ':'))
        
        # Exit OK
        sys.exit(0)
    else:
        print("No such file or directory", file=sys.stderr)
        sys.exit(2)
