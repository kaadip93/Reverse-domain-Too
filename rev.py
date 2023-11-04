# KaSper_BaGhDaD
# Cyb3r Drag0nz Team

# -*- coding: utf-8 -*-
#usr/bin/env python3

import requests, os
from bs4 import BeautifulSoup
from colorama import Fore

os.system("clear")
print(Fore.RED + """
      ,-.
     / \  `.  __..-,O
    :   \ --''_..-'.'
    |    . .-' `. '.
    :     .     .`.'
     \     `.  /  ..
      \      `.   ' .
       `,       `.   \ 
      ,|,`.        `-.\ 
     '.||  ``-...__..-`
      |  |
      |__|       --------------------------------------------
      /||\\       Coded By KaSper_BaGhDaD | @Cyb3r_Drag0nz
     //||\\\\                Mass Reverse Domin 1.0
    // || \\\\   ---------------------------------------------
 __//__||__\\\\ __
'--------------' 

 """)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
file = open('domainlist.txt', 'r').read().split('\n')
for link in file:
        if link == "":
                continue
        url = "https://viewdns.info/reverseip/?host="+link+"&t=1"
        text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(text, 'html.parser')
        narrow = soup.find('table', attrs={'border':'1'})
        domain = narrow.findAll('td', attrs={'align':None})[2:]
        for line in domain:
                print(Fore.GREEN+ '[+] ' + Fore.WHITE + line.text)
                file = open('Result.txt', 'a')
                content = (line.text + '\n')
                file.writelines(content)
        
    


    
