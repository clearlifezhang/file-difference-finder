import pytest
import os
from src.difference_finder import find_differences

def read_output_file(output_dir, filename):
    with open(os.path.join(output_dir, filename)) as f:
        return f.read().strip()

def cleanup_output_files(output_dir):
    files_to_remove = ['only_in_input1.txt', 'only_in_input2.txt']
    for file in files_to_remove:
        filepath = os.path.join(output_dir, file)
        if os.path.exists(filepath):
            os.remove(filepath)

def test_empty_files():
    output_dir = 'tests/'
    find_differences('tests/data/empty.txt', 'tests/data/empty.txt', output_dir)
    assert read_output_file(output_dir, 'only_in_input1.txt') == ''
    assert read_output_file(output_dir, 'only_in_input2.txt') == ''
    cleanup_output_files(output_dir)

def test_identical_files():
    output_dir = 'tests/'
    find_differences('tests/data/same1.txt', 'tests/data/same2.txt', output_dir)
    assert read_output_file(output_dir, 'only_in_input1.txt') == ''
    assert read_output_file(output_dir, 'only_in_input2.txt') == ''
    cleanup_output_files(output_dir)

def test_standard_case():
    output_dir = 'tests/'
    find_differences('tests/data/input1.txt', 'tests/data/input2.txt', output_dir)
    assert read_output_file(output_dir, 'only_in_input1.txt') == 'apple'
    assert read_output_file(output_dir, 'only_in_input2.txt') == 'date'
    cleanup_output_files(output_dir)

def test_varied_length():
    output_dir = 'tests/'
    find_differences('tests/data/varied1.txt', 'tests/data/varied2.txt', output_dir)
    assert read_output_file(output_dir, 'only_in_input1.txt') == 'apple'
    assert read_output_file(output_dir, 'only_in_input2.txt') == 'banana\npeach'
    cleanup_output_files(output_dir)

