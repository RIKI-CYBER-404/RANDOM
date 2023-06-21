import os, platform

print(50*"-")

print("[>>] JOIN MY GROUP")

print(50*"-")

os.system('xdg-open https://facebook.com/groups/3292482557465277/ ')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from XD64 import riki

    riki()

elif bit == '32bit':

    from XD32 import riki

    riki()
