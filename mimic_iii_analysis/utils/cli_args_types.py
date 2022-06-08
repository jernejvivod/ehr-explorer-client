import argparse
import os


def dir_path(path: str) -> str:
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError('Path must specify a directory')
    return path
