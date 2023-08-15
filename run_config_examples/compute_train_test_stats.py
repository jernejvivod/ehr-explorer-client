import argparse
import sys
from collections import Counter


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # parse arguments
    parser = argparse.ArgumentParser(prog='train-test-set-stats')
    parser.add_argument('--train-set-path', type=str, required=True, help='Path to training set')
    parser.add_argument('--test-set-path', type=str, required=True, help='Path to training set')

    parsed_args = vars(parser.parse_args(argv[1:]))
    write_stats_reports(parsed_args['train_set_path'], parsed_args['test_set_path'])


def write_stats_reports(train_set_path: str, test_set_path: str):
    """Compute stats and write to file.

    :param train_set_path: path to file containing the training examples in FastText format
    :param test_set_path: path to file containing the test examples in FastText format
    """

    # count all examples
    all_examples_count = count_examples(train_set_path) + count_examples(test_set_path)

    # count train set and test set examples
    train_examples_count = count_examples(train_set_path)
    test_examples_count = count_examples(test_set_path)

    # count classes
    classes_count_train = count_classes(train_set_path)
    classes_count_test = count_classes(test_set_path)

    num_positive_train = sum(classes_count_train[k] for k in classes_count_train.keys() if k > 0)
    num_negative_train = sum(classes_count_train[k] for k in classes_count_train.keys() if k == 0)
    num_positive_test = sum(classes_count_test[k] for k in classes_count_test.keys() if k > 0)
    num_negative_test = sum(classes_count_test[k] for k in classes_count_test.keys() if k == 0)

    # write computed stats to file
    with open('train-test-set-stats.txt', 'w') as f:
        f.write('number of examples: {}\n'.format(all_examples_count))
        f.write('number of examples in training set: {}\n'.format(train_examples_count))
        f.write('number of examples in test set: {}\n'.format(test_examples_count))
        f.write('number of positive examples in training set: {}\n'.format(num_positive_train))
        f.write('number of negative examples in training set: {}\n'.format(num_negative_train))
        f.write('number of positive examples in test set: {}\n'.format(num_positive_test))
        f.write('number of negative examples in test set: {}\n'.format(num_negative_test))

    # compute example lengths
    example_lengths_train = get_example_lengths(train_set_path)
    example_lengths_test = get_example_lengths(test_set_path)

    # write example lengths to a CSV file
    with open('example_lengths.csv', 'w') as f:
        f.write(' '.join(str(el) for el in example_lengths_train))
        f.write(' ')
        f.write(' '.join(str(el) for el in example_lengths_test))


def count_examples(file_path: str) -> int:
    """Count examples in FastText format in file.

    :param file_path: path to file containing the examples
    """
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)


def count_classes(file_path: str) -> Counter:
    """Count classes of examples in FastText format in file.

    :param file_path: path to file containing the examples
    """
    classes = []
    with open(file_path, 'r') as f:
        for line in f:
            classes.append(int(line.split(' ')[-1][len('__label__'):]))
    return Counter(classes)


def get_example_lengths(file_path: str) -> list:
    """Compute lengths of example in FastTExt format in file.

    :param file_path: path to file containing the examples
    """
    counts = []
    with open(file_path, 'r') as f:
        for line in f:
            counts.append(len(line.split(' ')) - 1)

    return counts


if __name__ == '__main__':
    main()
