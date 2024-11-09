import argparse
import sys


def main():
    """
    main function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', type=argparse.FileType('r'),
                        help=('provide the file that contains the '
                            'hexadecimal key of at least 64 characters'))
    parser.add_argument('-k', type=argparse.FileType('r'), choices=['otp.key'],
                        help=('provide the file which contains the key that '
                            'will be used to generate the password.'))
    args = parser.parse_args()
    if args.g:
        print(args.g.name)
    if args.k:
        print(args.k)

if __name__ == '__main__':
    main()
