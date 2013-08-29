"""
A rudimentary way to train additional ham into our pickle file.

Example usage:

$ python train_spam.py /path/to/spam.pkl
blah blah blah^D
"""
import sys
from spambayes.storage import PickledClassifier


def main():
    pickle_filename = sys.argv[-1]
    bayes = PickledClassifier(pickle_filename)
    message = sys.stdin.readlines()
    bayes.learn(message, False)
    bayes.store()


if __name__ == '__main__':
    main()
