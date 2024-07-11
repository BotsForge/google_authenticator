# pyinstaller -n "TOTP" -F -i "authcode.ico" --add-data "authcode.ico;." main.py

from totp.totp import main
from totp.utils import LOGO, set_console_size_and_name

if __name__ == '__main__':
    set_console_size_and_name(420, 500, 'TOTP')
    print(LOGO)
    main()
