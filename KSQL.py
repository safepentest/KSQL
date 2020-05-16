# python 3.7.1

print("apt update && upgrade")
print ("Y")
print ("pkg install figlet ")
print ("Y")
print ("pkg install git")
print ("Y")
print ("pkg install python")
print ("Y")
print ("pkg install python2")
print ("Y")
print("git clone https://github.com/sqlmapproject/sqlmap")
print ("Y")
while true:
  print("clear")
  print("figlet KSQL")
  print("Safe Pentest Devolper By KUZGUN ")
  print("Yapılabilecek hic bir yasadışı faliyetten biz sorumlu değiliz.(We are not responsible for any illegal activity that can be done.) \n \n")
  print(" 1=database \n 2=tables \n 3=colums \n 4=dump \n 5=çıkış(exit))")

  secim=int(input("seçiminizi giriniz:"))

  if secim==1:
    site=str(input("site:"))
    print("python2 sqlmap.py -u "site" --dbs")

  elif secim==2:
    site=str(input("site:"))
    db=str(input("database:"))
    print("python2 sqlmap.py -u "site" -D "db --tables)

  elif secim==3:
    site=str(input("site:"))
    db=str(input("database:"))
    table=str(input("tables:"))
    print("python2 sqlmap.py -u "site" -D "db " -T "table " --colums")

  elif secim==4:
    site=str(input("site:"))
    db=str(input("database:"))
    table=str(input("tables:"))
    colum=str(input("colums(exemples:user,passwd,root):"))
    print("python2 sqlmap.py -u "site" -D "db " -T "table " -C "colum" --dump")

  elif 5==secim:
    break

  else:
    print("Lütfen tekrar deneyiniz(try again)")