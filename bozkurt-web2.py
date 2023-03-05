import os
import random
import socket
import webbrowser
import urllib.request
import colorama
from colorama import Fore, Back, Style, init
import time
import sys

os.system("clear")

print("-------------------------------------------------------")
print("-                                                     -")
print("-                                                     -")
print("-                                                     -")
print("-                 F3rkan  WEB V2                      -")
print("-               İnstagram: @f3rrkan                   -")
print("-     Web Site: https://f3rkan.github.io/             -")
print("-                                                     -")
print("-                                                     -")
print("-                                                     -")
print("-------------------------------------------------------")
print()

print("1.Ddos ( Kali Linux & Win İçin ) ")
print("2.Port Tarama ( Kali Linux İçin )")
print("3.Sqlmap ( kali Linux İçin )")
print("4.MetaSploit ( Kali Linux İçin ) ")
print("5.Admin Panel Finder")
print("6.Youtube'u Aç")
print("7.Google'u Aç")
print("8.Gmail'i Aç")
print("9.İnstagram'ı Aç")
print("10.Twitter'ı Aç")
print("11.Github'ı Aç")
print("12.Facebook'u Aç")
print("13.Twitch'ı Aç")
print("14.Dlive'ı Aç")
print("15.Eba'ı Aç")
print("16.Spotify'ı Aç")

veri = input("İşlem Numarası Giriniz: ")

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

if veri =="1":
    print("1.Bozkurt Ddos")
    print("2.Hammer")
    print("3.TorsHammer")
    
    ddos = input("Seçin: ")
    
    if ddos =="1":
        os.system("git clone https://github.com/frkndncr/bozkurt-ddos")

    if ddos =="2":
        os.system("git clone https://github.com/cyweb/hammer")

    if ddos =="3":
        os.system("git clone https://github.com/Karlheinzniebuhr/torshammer")
    
elif veri =="2":
    ipadrs = input("İp Adres Giriniz: ")
    os.system("nmap -sV {ipadrs}")

elif veri =="3":
    sqlste = input("Siteyi Giriniz: ")
    os.system("sqlmap -u {sqlste} --dbs")

elif veri =="4":
    os.system("msfconsole")

if veri =="6":
    webbrowser.get(chrome_path).open("youtube.com")

elif veri =="7":
    webbrowser.get(chrome_path).open("google.com")

elif veri =="8":
    webbrowser.get(chrome_path).open("https://www.google.com/gmail/")

elif veri =="9":
    webbrowser.get(chrome_path).open("instagram.com")

elif veri =="10":
    webbrowser.get(chrome_path).open("twitter.com")

elif veri =="11":
    webbrowser.get(chrome_path).open("github.com")

elif veri =="12":
    webbrowser.get(chrome_path).open("facebook.com")

elif veri =="13":
    webbrowser.get(chrome_path).open("https://www.twitch.tv/")

elif veri =="14":
    webbrowser.get(chrome_path).open("https://dlive.tv/")

elif veri =="15":
    webbrowser.get(chrome_path).open("https://www.eba.gov.tr/")

elif veri =="16":
     webbrowser.open("https://spotify.com")
