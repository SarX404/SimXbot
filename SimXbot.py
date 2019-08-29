import requests,os,json
os.system('clear')

#WARNA
blue='\033[1;34m'
green='\033[1;32m'
purple='\033[1;35m'
cyan='\033[1;36m'
red='\033[1;31m'
white='\033[1;37m'
yellow='\033[1;33m'


print ('''


\033[1;35m
       ____  _          __  ___           _
      / ___|(_)_ __ ___ \ \/ / |__   ___ | |_
      \___ \| | '_ ` _ \ \  /| '_ \ / _ \| __|
       ___) | | | | | | |/  \| |_) | (_) | |_
      |____/|_|_| |_| |_/_/\_\_.__/ \___/ \__|


\033[1;32m ===============================================\033[1;m
\033[1;37m|                     SimXbot                   |
\033[1;32m ===============================================\033[1;m

\033[1;36m  [ + ]  \033[1;32mAuthor     : Samber_Galeng\033[1;m
\033[1;36m  [ + ]  \033[1;32mContact Me : Deathxx404@gmail.com\033[1;m
\033[1;36m  [ + ]  \033[1;32mFacebook   : Samber Galeng\033[1;m
''')


nama = raw_input(green+"    [+]"+white+" Nama : ")
bhs  = raw_input(green+"    [+]"+white+" Bahasa : ")
print
print
print

while(True):
     try:
          msg = raw_input(cyan+"	[+] "+white+nama+" : ")
          url = "https://wsapi.simsimi.com/190410/talk/"

          payload = "{\n\t\"utext\": \"%s\", \n\t\"lang\": \"%s\" \n}"%(msg,bhs)
          headers = {
          'Content-Type': "application/json",
          'x-api-key': "BFlPYu4a696ci1HIJI8BmYJv57rd4i8GTjvwSvpQ"
          }

          response = requests.request("POST", url, data=payload, headers=headers)

	  print ""

          y = json.loads(response.text)
          print yellow+"	[+] "+white+"Simi : "+y["atext"]
	  print ""
     except KeyboardInterrupt:
          exit()
