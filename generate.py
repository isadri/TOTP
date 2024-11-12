import argparse
import qrcode
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import string
import sys
from totp.totp import TOTP


def parse_args() -> argparse.Namespace:
    """
    parse the argument and return a argparse.Namespace object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', help=('provide the file that contains the '
                                'hexadecimal key of at least 64 characters'))
    parser.add_argument('-k', type=str, choices=['otp.key'],
                        help=('provide the file which contains the key that '
                            'will be used to generate the password.'))
    return parser.parse_args()


def is_hex(key: str) -> bool:
    """
    check if the key contains only hexadecimal characters.
    """
    chars = string.ascii_uppercase + '234567='
    return all(c for c in key if c in chars)


def get_key_from_file(filename: str) -> str:
    """
    read the key from the file and return it.
    """
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            key = f.read()
            if len(key) < 64 or not is_hex(key):
                print(f'{sys.argv[0]}: error: key must be 64 hexadecimal '
                    'characters.', file=sys.stderr)
                sys.exit(1)
            return key
    except (FileNotFoundError, PermissionError):
        print(f'usage: python3 {sys.argv[0]} [-h] [-g G] [-k {{otp.key}}]',
            file=sys.stderr)
        print(f"{sys.argv[0]}: error: argument -g: can't open '{filename}'",
            file=sys.stderr)
        sys.exit(1)


def store_key(key: str) -> None:
    """
    read the key from the file and generate a TOTP password.
    """
    try:
        with open('otp.key', 'w', encoding='UTF-8') as f:
            f.write(key)
            print("Key was successfully saved in otp.key.")
    except (FileNotFoundError, PermissionError):
        print(f'usage: python3 {sys.argv[0]} [-h] [-g G] [-k {{otp.key}}]',
            file=sys.stderr)
        print(f"{sys.argv[0]}: error: argument -g: can't open 'otp.key'",
            file=sys.stderr)
        sys.exit(1)


def generate_password(otp: TOTP) -> int:
    """
    read the key from the otp.key file and generate a TOTP value.

    Returns:
        The TOTP value.
    """
    try:
        with open('otp.key', 'r', encoding='UTF-8') as f:
            key = f.read()
            return otp.generate(key)
    except (FileNotFoundError, PermissionError):
        print(f'usage: python3 {sys.argv[0]} [-h] [-g G] [-k {{otp.key}}]',
            file=sys.stderr)
        print(f"{sys.argv[0]}: error: argument -g: can't open 'otp.key'",
            file=sys.stderr)
        sys.exit(1)


def create_uri(key: str) -> str:
    """
    create a uri to add to qrcode
    """
    uri = f'otpauth://totp/TOTP:isadri?secret={key}&issuer=TOTP&digits=6&period=30'
    return uri


def make_qrcode_image(uri: str) -> PngImageFile:
    """
    create an image for the qrcode and display it.
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(uri)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='black', black_color='white')
    qr_img.save('otp.png')
    img = Image.open('otp.png')
    img.show()
    return img


def create_qrcode() -> tuple[str, PngImageFile]:
    """
    Create a qrcode.
    """
    try:
        with open('otp.key', 'r', encoding='UTF-8') as f:
            secret = f.read()
            uri = create_uri(secret)
            img = make_qrcode_image(uri)
            return secret, img
    except (FileNotFoundError, PermissionError):
        print(f'usage: python3 {sys.argv[0]} [-h] [-g G] [-k {{otp.key}}]',
            file=sys.stderr)
        print(f"{sys.argv[0]}: error: argument -g: can't open 'otp.key'",
            file=sys.stderr)
        sys.exit(1)


def verfiy_otp(secret, otp) -> None:
    """
    verify if the given otp of the given secret is valid.
    """
    user_otp = input('Enter the otp: ')
    if otp.verify(secret, user_otp):
        print('Valid')
    else:
        print('Not Valid, try after some seconds.')


def main() -> None:
    """
    main function.
    """
    otp = TOTP()

    args = parse_args()
    if args.g:
        secret = get_key_from_file(args.g)
        store_key(secret)
    if args.k:
        secret, img = create_qrcode()
        verfiy_otp(secret, otp)
        img.close()


if __name__ == '__main__':
    main()
