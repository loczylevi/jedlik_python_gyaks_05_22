print("1.feladat: Kisebb-nagyobb meghatározása")
bekeres = int(input("Kérem az első számot: "))
bekeres2 = int(input("Kérem a második számot: "))

if bekeres > bekeres2:
  print(f"A nagyobb szám {bekeres}, a kisebb {bekeres2}\n")
elif bekeres2 > bekeres:
  print(f"A nagyobb szám {bekeres2}, a kisebb {bekeres}\n")  
else:
  print("A két szám egyenlő\n")
  
print("2.feladat: Szökőév listázó")
szam1 = int(input("Kérem az egyik évszámot: "))
szam2 = int(input("Kérem a másik évszámot: "))
tol = 0
ig = 0

if szam1 > szam2:
  ig = szam1
  tol = szam2
else:
  ig = szam2
  tol = szam1
lista = []

for szam in range(tol,ig+1):
  lista.append(szam)
  
def szokoev(lista):
  szokoev = []
  for ev in lista:
    if ev % 400 == 0:
      szokoev.append(str(ev))      
    if ev % 4 == 0 and ev % 100 != 0:
      szokoev.append(str(ev))
  return szokoev
  
szokoev = szokoev(lista)
if len(szokoev):
  print(f"Szökőévek: {'; '.join(szokoev)}\n")
else:
  print("Nincs szökőév a megadott tartományban!\n")
  
#név;város;ország;magasság;emelet;épült
#10 Upper Bank Street;London;Anglia;151;32;2003
  
class Épület:
  def __init__(self,sor):
    nev,varos,orszag,magassag,emelet,epult = sor.strip().split(";")
    self.nev = nev
    self.varos = varos
    self.orszag = orszag
    self.magassag = float(magassag.replace(",","."))
    self.emelet = int(emelet)
    self.epult = int(epult)

with open("legmagasabb.txt","r",encoding="utf-8") as f:
  fejlec = f.readline()
  lista = [Épület(sor) for sor in f]

print(f"3.2 feladat: Épületek száma: {len(lista)} db.")

em_ossz = sum([sor.emelet for sor in lista])

print(f"3.3 feladat: Emeletek összege: {em_ossz} db.")

legmagasabb = [(sor.magassag, sor) for sor in lista]
nagy,adat = max(legmagasabb)

print(f"""3.4 feladat: A legmagasabb épület adatai
        Név: {adat.nev}
        Város: {adat.varos}
        Ország: {adat.orszag}
        Magasság: {adat.magassag} m
        Emeletek száma: {adat.emelet}
        Épités éve: {adat.epult}""")


kereso = [sor for sor in lista if sor.orszag == "Olaszország"]

if len(kereso) > 0:
  print("3.5 feladat: Van olasz épület az adatok között!")
else:
   print("3.5 feladat: Nincs olasz épület az adatok között!") 