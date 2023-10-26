#!/usr/bin/env python3

import os
import argparse

def find_differences(input_file1, input_file2, output_directory):
    output_file1 = os.path.join(output_directory, "only_in_input1.txt")
    output_file2 = os.path.join(output_directory, "only_in_input2.txt")

    with open(input_file1, 'r') as file1, open(input_file2, 'r') as file2:
        set1 = set(file1.read().splitlines())
        set2 = set(file2.read().splitlines())

    only_in_input1 = set1 - set2
    only_in_input2 = set2 - set1

    with open(output_file1, 'w') as out1:
        for line in sorted(only_in_input1):
            out1.write(line + '\n')

    with open(output_file2, 'w') as out2:
        for line in sorted(only_in_input2):
            out2.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description="Find differences between two files.")
    parser.add_argument('input_file1', help="Path to the first input file")
    parser.add_argument('input_file2', help="Path to the second input file")
    parser.add_argument('-o', '--output_directory', help="Directory where output files will be saved", default=os.getcwd())

    args = parser.parse_args()

    # Ensure the output directory exists
    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    find_differences(args.input_file1, args.input_file2, args.output_directory)

if __name__ == "__main__":
    main()

