# This is a sample Python script.
from idlelib.run import exit_now


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("labas")

#1
print(15, 12, 89, 5.8)
#2
print(78*2)
print(5+3)
print(7/2)
print(85-32)
#3
print(5.2*3)
print(9.4*0.5)
print(4.2/2)
#4
print(7+2*3)
print((7+2)*3)
print(52+74+32)
print(87-65+14)
print(79/(5-2))
#5
result = 2 ** 4
print(result)

result = 8 ** 3
print(result)

result = 14 ** 0.5
print(result)

#6
remainder = 2 % 2
print(remainder)

remainder = 3 % 2
print(remainder)

remainder = 11 % 2
print(remainder)

remainder = 12 % 2
print(remainder)

remainder = 10 % 2
print(remainder)

#7


#8
print(5//2)
print(6//3)
print(6//4)
print(80//3)
print(45//4)
print(45//3)

#9
print(  type(6)  )
print(  type(2.5)  )
print(  type(157)  )
print(  type(-8.2)  )
print(  type(2%5)  )
print(  type(8*9)  )
print(  type(8.5*3)  )

#1

vardas = "Tomas"
pavarde = "Petrauskas"
amzius = 21
ugis = 1.80  # metrų
svoris = 75  # kilogramai
aukstoji_mokykla = "Vilniaus universitetas"
akademines_grupes_kodas = "IT-21"
kursas = 3
studiju_programos_pavadinimas = "Informacinių technologijų studijos"
atsiskaitytu_kreditu_skaicius = 60
print('vardas', vardas)
print('pavarde', pavarde)
print('amzius', amzius)
print('ugis', ugis)
print('svoris', svoris)
print('aukstoji mokykla', aukstoji_mokykla)
print('akademines grupes kodas', akademines_grupes_kodas)
print('kursas', kursas)
print('studiju programos pavadinimas', studiju_programos_pavadinimas)
print('atsiskaitytu kreditu skaicius', atsiskaitytu_kreditu_skaicius)

#2

pavadinimas = 'Vilnius'
valstybe = 'Lietuva'
apskritis = 'Vilniaus apskritis'
ikurimo_data = 1323  # m.
meras = 'Remigijus Šimašius'
plotas_kv_km = 401  # kvadratiniai kilometrai
gyventoju_skaicius = 580000  # gyventojų skaičius
print('pavadinimas', pavadinimas)
print('valstybe', valstybe)
print('apskritis', apskritis)
print('ikurimo_data', ikurimo_data)
print('meras', meras)
print('plotas_kv_km', plotas_kv_km)
print('gyventoju skaicius', gyventoju_skaicius)

#3
vardas = "Alina"
print("Mano vardas yra", vardas)

#4
akademine_grupe = "IFZM-6"
vidurkis = 8.0
print("Akademinė grupė:", akademine_grupe)
print("Vidurkis:", vidurkis)

#5
zodis = "Python"
print((zodis + " ") * 5)

#1
vardas = "Alina"
amzius = 41

print(f"{vardas}, {amzius} metų")
print("Pasiryžau išbandyti programavimą, nes tai leidžia kurti įdomias programas ir spręsti problemas.")

#2
eileraštis = """Nuo amžių vakare prie stalo dviese
Kaip angelas naminis lempa tvieskia
Apgaubki, angele, šviesa švaria
Ir saugoki du žmones vakare
Diena primargino, nesužiūrėsi"""

print(eileraštis)

#3
dydis = 3

print('*' * dydis)

for _ in range(dydis - 2):
    print('*' + ' ' * (dydis - 2) + '*')

print('*' * dydis)

#4
pavadinimas = "katė"
amzius = 3
kailio_spalva = "juoda"
svoris = 4.5

print(f"Gyvūnas - {pavadinimas} ({amzius} m.) turi {kailio_spalva} kailio spalvą ir sveria {svoris} kg.")

#5
skaičius = 25

print(str(skaičius) * 5)

#6
skaičius = 25

print((str(skaičius) + " ") * 5)

#7
for i in range(1, 4):
    print("*" * i)

#8
print("Pirmoji eilutė.\nAntroji eilutė.\nTrečioji eilutė.")

#9
print("+--------+--------+")
print("| Vardas | Amžius |")
print("+--------+--------+")
print("| Tomas  | 24     |")
print("| Jonas  | 26     |")
print("| Justė  | 25     |")
print("+--------+--------+")

#2 paskaita


#1 Išveskite atsakymus šių veiksmų:
#1. 8 * 4 + 2
#2. 8 * (4 + 2)
#3. 48 / 4
#.3 + 6 * 2

result1 = 8 * 4 + 2
result2 = 8 * (4 + 2)
result3 = 48 / 4
result4 = 3 + 6 * 2

print("1. 8 * 4 + 2 =", result1)
print("2. 8 * (4 + 2) =", result2)
print("3. 48 / 4 =", result3)
print("4. 3 + 6 * 2 =", result4)

#2 Susikurkite du kintamuosius skaičiams saugoti. Į juos įrašykite norimus
#skaičius. Susikurkite trečiąjį kintamąjį, kurio reikšmė būtų pirmų dviejų
#kintamųjų suma. Visus kintamuosius išveskite.

pirmas_sk = 5
antras_sk = 10

suma = pirmas_sk + antras_sk

print("Pirmas skaičius:", pirmas_sk)
print("Antras skaičius:", antras_sk)
print("Suma:", suma)

#3 Susikurkite tris kintamuosius skaičiams saugoti. Į juos įrašykite norimus
#skaičius. Raskite šių skaičių suma, skirtumą, sandaugą ir dalmenį.
#Atsakymus išveskite kartu su atliekamu veiksmu (pvz 8 + 2 + 4 = 14).

pirmas_sk = 8
antras_sk = 2
trecias_sk = 4

suma = pirmas_sk + antras_sk + trecias_sk
skirtumas = pirmas_sk - antras_sk - trecias_sk
sandauga = pirmas_sk * antras_sk * trecias_sk
dalmuo = pirmas_sk / antras_sk / trecias_sk

print(f"{pirmas_sk} + {antras_sk} + {trecias_sk} = {suma}")
print(f"{pirmas_sk} - {antras_sk} - {trecias_sk} = {skirtumas}")
print(f"{pirmas_sk} * {antras_sk} * {trecias_sk} = {sandauga}")
print(f"{pirmas_sk} / {antras_sk} / {trecias_sk} = {dalmuo:.2f}")

#
#4 Susikurkite du kintamuosius skaičiams saugoti. Į juos įrašykite norimus
#skaičius. Pirmąjį kintamąjį padidinkite 5-iais. Antrajį padidinkite 2 kartus.
#Išveskite visus atsakymus (pradines reikšmes ir pakeistas reikšmes).

pirmas_sk = 10
antras_sk = 4

pirmas_sk_padidintas = pirmas_sk + 5

antras_sk_padidintas = antras_sk * 2

print(f"Pradinis pirmas skaičius: {pirmas_sk}")
print(f"Pradinis antras skaičius: {antras_sk}")
print(f"Pirmas skaičius padidintas 5-iais: {pirmas_sk_padidintas}")
print(f"Antras skaičius padidintas 2 kartus: {antras_sk_padidintas}")

#
##1 Paprašykite vartotojo įvesti savo vardą, amžių ir kodėl pasirinko
# programavimą. Įvestą informaciją išveskite kaip nors tvarkingai, sakiniu ar
# atskirose eilutėse su prierašais.

#vardas = input("Įveskite savo vardą: ")
#amzius = input("Įveskite savo amžių: ")
#priezastis = input("Kodėl pasirinkote programavimą? ")
#
# print("\nĮvesta informacija:")
# print(f"Vardas: {vardas}")
# print(f"Amžius: {amzius} metų")
# print(f"Priežastis, kodėl pasirinkote programavimą: {priezastis}") #

#
# #
# ##2 Paprašykite vartotojo įvesti norimą simbolį. Iš šio simbolio išveskite
# #norimo dydžio kvadratą.
#
# #
# ##3 Paprašykite vartotojo įvesti norimą simbolį. Iš šio simbolio atspausdinkite
# #laiptus. Pvz.:
# #*
# #**
# #***
#
# #simbolis = input("*: ")
# #dydis = 3
#
# for i in range(1, dydis + 1):
#     print(simbolis * i) #


#4 Paprašykite vartotojo įvesti vardą, amžių, ūgį (metais) (nepamirškite ką
#reikia iškonvertuoti iš str į int ar float). Išveskite gautus duomenis ir jų
#tipus.




#uzduotis: Susikurkite tris kintamuosius skaičiams saugoti. Parašykite šias atskiras
# if sąlygas:
# Ar pirmas ir antras skaičiai yra lygūs?
#Ar antras ir trečias skaičiai yra lygūs?
#Ar pirmas skaičius yra didesnis už antrąjį?
#Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę (trečias skaičius padaugintas iš 2)?
#Ar pirmas skaičius yra lyginis (ar dalinasi iš 2)?
#Ar antras skaičius yra nelyginis (ar nesidalina iš 2)?
#Ar trečias skaičius yra teigiamas (didesnis už 0)?
#Ar pirmas skaičius yra neigiamas (mažesnis už 0)?
#Ar antras skaičius dalinasi iš 4?
#Ar trečias skaičius dalinasi iš 8?

pirmas_sk = 10
antras_sk = 20
trecias_sk = 3

# Ar pirmas ir antras skaičiai yra lygūs?
if pirmas_sk == antras_sk:
    print("Pirmas ir antras skaičiai yra lygūs.")
else:
    print("Pirmas ir antras skaičiai nėra lygūs.")

# Ar antras ir trečias skaičiai yra lygūs?
if antras_sk == trecias_sk:
    print("Antras ir trečias skaičiai yra lygūs.")
else:
    print("Antras ir trečias skaičiai nėra lygūs.")

# Ar pirmas skaičius yra didesnis už antrąjį?
if pirmas_sk > antras_sk:
    print("Pirmas skaičius yra didesnis už antrąjį.")
else:
    print("Pirmas skaičius nėra didesnis už antrąjį.")

# Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę?
if antras_sk > (trecias_sk * 2):
    print("Antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę.")
else:
    print("Antras skaičius nėra didesnis už dvigubą trečiojo skaičiaus reikšmę.")

# Ar pirmas skaičius yra lyginis?
if pirmas_sk % 2 == 0:
    print("Pirmas skaičius yra lyginis.")
else:
    print("Pirmas skaičius yra nelyginis.")

# Ar antras skaičius yra nelyginis?
if antras_sk % 2 != 0:
    print("Antras skaičius yra nelyginis.")
else:
    print("Antras skaičius yra lyginis.")

# Ar trečias skaičius yra teigiamas?
if trecias_sk > 0:
    print("Trečias skaičius yra teigiamas.")
else:
    print("Trečias skaičius nėra teigiamas.")

# Ar pirmas skaičius yra neigiamas?
if pirmas_sk < 0:
    print("Pirmas skaičius yra neigiamas.")
else:
    print("Pirmas skaičius nėra neigiamas.")

# Ar antras skaičius dalinasi iš 4?
if antras_sk % 4 == 0:
    print("Antras skaičius dalinasi iš 4.")
else:
    print("Antras skaičius nedalinasi iš 4.")

# Ar trečias skaičius dalinasi iš 8?
if trecias_sk % 8 == 0:
    print("Trečias skaičius dalinasi iš 8.")
else:
    print("Trečias skaičius nedalinasi iš 8.")

    git config --global user.name "Sulima83"
    git config --global user.email "ekvadora@gmail.com"










