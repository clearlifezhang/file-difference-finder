# File Difference Finder

## Description
File Difference Finder is a Python tool designed to compare two text files and identify unique strings in each file. It outputs two separate files, each containing the strings found exclusively in one of the original files.

## Features
- Compares two text files.
- Identifies unique strings in each file.
- Outputs the results into two separate files.

## Installation
Clone the repository to your local machine:
git clone https://github.com/clearlifezhang/file-difference-finder.git
cd file-difference-finder

Create and activate the Conda environment:
conda env create -f environment.yml
conda activate file-difference-finder-env


## Usage
To use the File Difference Finder, run the following command with the paths to your input files and the desired output directory:
python src/difference_finder.py <path_to_input_file_1> <path_to_input_file_2> <output_directory>

Example:
python src/difference_finder.py tests/data/input1.txt tests/data/input2.txt output/

The output will be generated in two files in the specified directory: `only_in_input1.txt` and `only_in_input2.txt`.

## Testing
To run the tests, ensure you have activated the Conda environment, and then execute:
pytest tests/test_difference_finder.py

in the root directory of the project. Output files generated during testing are automatically cleaned up.

## Contributing
Contributions to File Difference Finder are welcome! Please feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License -

Created by [Mingsheng Zhang](https://github.com/clearlifezhang)
