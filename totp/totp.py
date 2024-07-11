import pyotp
import pyperclip


def main():
    last_code = ''
    while True:
        try:
            code = input('\npast TOTP key end press <Enter>\n')
            code = ''.join(i for i in code.split())
            if code:
                last_code = code
            else:
                code = last_code
            totp = pyotp.TOTP(code)
            c = totp.now()
            print(f'\n{c}')
            pyperclip.copy(c)
        except Exception:
            print('wrong TOTP key')
            last_code = ''
