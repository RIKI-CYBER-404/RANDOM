import os
import platform, time
os.system('clear')
#os.system('xdg-open https://chat.whatsapp.com/ETph2TkuyGaGgVqXdnwuNz')
print("join WhatsApp gc for upcoming updates");time.sleep(5)


os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import XD64
    
elif b == '32bit':
    import XD32
