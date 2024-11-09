import argparse
import os
import string
import sys
from totp import TOTP


def parse_args() -> argparse.Namespace:
    """
    parse the argument and return a argparse.Namespace object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', help=('provide the file that contains the '
                                'hexadecimal key of at least 64 characters'))
    parser.add_argument('-k', type=argparse.FileType(), choices=['otp.key'],
                        help=('provide the file which contains the key that '
                            'will be used to generate the password.'))
    return parser.parse_args()


def key_not_hex(key: str) -> bool:
    """
    check if the key contains only hexadecimal characters.
    """
    return all(c in string.hexdigits for c in key)


def get_key_from_file(filename: str) -> str:
    """
    read the key from the file and return it.
    """
    try:
        with open(filename) as f:
            key = f.read()
            if len(key) < 64 or key_not_hex(key):
                print(f'{sys.argv[0]}: error: key must be 64 hexadecimal '
                    'characters.', file=sys.stderr)
                sys.exit(1)
            return key
    except FileNotFoundError:
        print(f'usage: python3 {sys.argv[0]} [-h] [-g G] [-k {{otp.key}}]',
            file=sys.stderr)
        print((f"{sys.argv[0]}: error: argument -g: can't open '{filename}'"
            f" No such file or directory: '{filename}'"),
            file=sys.stderr)
        sys.exit(1)


def store_key(key: str) -> None:
    """
    read the key from the file and generate a TOTP password.
    """
    with open('otp.key', 'w') as file:
        file.write(key)


def main() -> None:
    """
    main function.
    """
    args = parse_args()
    if args.g:
        key = get_key_from_file(args.g)
        store_key(key)
    if args.k:
        print(args.k)

if __name__ == '__main__':
    main()
