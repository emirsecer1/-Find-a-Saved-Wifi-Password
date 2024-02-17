import subprocess

print("Kayıtlı olan sifreler: ")

veri = subprocess.check_output(['netsh', 'wlan',
'show', 'profiles']).decode('utf-8').split('\n')
sistemler = [i.split(":")[1][1:-1]
for i in veri if "All User Profile" in i]
for i in sistemler:
    sonuç = subprocess.check_output(['netsh', 'wlan', 'show',
     'profile', i, 'key=clear']).decode('utf-8').split(
        '\n')
    sonuç = [b.split(":")[1][1:-1]
     for b in sonuç if "Key Content" in b]
    try:
        print(" \\{:<30}| Şifre:  {:<}".format(i, sonuç[0]))
    except IndexError:
        print(" \\{:<30}| Şifre:  {:<}".format(i, ""))