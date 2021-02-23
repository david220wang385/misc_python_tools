"""
References:
https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/
https://tutorial.eyehunts.com/python/python-string-index-function-index-substring/
https://www.w3schools.com/python/ref_string_endswith.asp
https://www.geeksforgeeks.org/python-string-ljust-rjust-center/
"""

import os, argparse

# Entrypoint
def main():

    # Provide decription of the program
    parser = argparse.ArgumentParser(
        description='Change file extension for all files in the current directory; Think of it as find and replace but for file endings'
    )

    # Positional arguments for specifying target directory/file and key to be used in the keystream
    parser.add_argument(
        'target_dir',
        help='The directory that you want apply file extension changes to'
    )
    parser.add_argument(
        'find_ending',
        help='File extension you want to find'
    )
    parser.add_argument(
        'replace_ending',
        help='File extension you want to replace the "found" extension with'
    )

    # Parse arguments and initialize variables
    args = parser.parse_args()
    target_dir = args.target_dir
    find_ending = args.find_ending
    replace_ending = args.replace_ending

    # Printing for debug
    print(" ARGUMENTS PARSED: ".center(80, '-'))
    print("Target directory:\t\t", target_dir)
    print("Extension to look for:\t\t", find_ending)
    print("Extension to replace with:\t", replace_ending)

    # Navigate to target directory
    os.chdir(target_dir)
    print("Changing to target directory:\t", os.getcwd())
    print("".rjust(80, '-'),"\n")

    # Prompt work
    print(" MATCHES FOUND: ".center(80, '-'))
    [print(file) for file in os.listdir() if file.endswith(find_ending)]
    print("".rjust(80, '-'),"\n")

    # Prompt user 
    user_input = input("> PROCEED WITH FILE RENAMING? (Y/N): ")
    print()

    # Proceed with file renaming
    if(user_input.lower() == 'y' or user_input.lower() == 'yes'):

        print(" RENAMING FILES: ".center(80, '-'))
        # Iterate through all files in the current directory (not recursive)
        for f in os.listdir():

            # If filename ends with target ending rename it
            if f.endswith(find_ending):
                new_name = '{}{}'.format(f[:f.index(find_ending)], replace_ending)
                os.rename(f, new_name)
                print("File renamed:\t", f.ljust(18), "\t-->\t", new_name.ljust(18))
                
        print("\n".rjust(80, '-'))

# Only execute if called directly
if __name__ == "__main__":
    main()