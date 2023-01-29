import argparse
import os


def dir_path(path: str) -> str:
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError('Path must specify a directory.')
    return path


def test_size(value):
    value = float(value)
    if value < 0.0 or value > 1.0:
        raise argparse.ArgumentTypeError("Train set decimal fraction size should be between 0.0 and 1.0.")
    return value
