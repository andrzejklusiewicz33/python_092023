#test
#  JAVA (fuuuu)
# class Main{
#
#     public static void main(String arg[]){
#     System.out.println("hello");
# }
#
# }
#
# def funkcja():
#     print('hello')
#
# print('hello')
# print("hello")
# print("Mc'Donalds")
# #imie='Andrzej'
# #PEP8
# first_name='Andrzej'
# print(first_name,type(first_name))
# #String firstName='Andrzej'
# first_name=123
# print(first_name,type(first_name))
# first_name=1.23
# print(first_name,type(first_name))
# first_name=input('podaj imię:\n')
# print(first_name)
#x=input('podaj wartość x:\n')
#print(x,type(x))
#print(x/2)
# fruit='Banana'
# color='blue'
# print("Twój ulubiony owoc to : ",fruit)
# print("Twój ulubiony owoc to: "+fruit)
# print("Twój ulubiony owoc to {}, a kolor {}".format(fruit,color,'UWAGA'))
#
# x=123
# y=345
# print('x='+str(x) )
# print('x={}'.format(x))
# print(f'x={x} y={y}')
#
# a=input('')
# b=input('')
# a,b=input(''),input('')
#1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
#   wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
#
# first_name=input('Podaj imię:\n')
# last_name=input('Podaj nazwisko:\n')
# print(f'Witaj {first_name} {last_name}!')
# print('Witaj {} {}!'.format(first_name,last_name))
# print('Witaj '+first_name+' '+last_name+'!')
# print('Witaj',first_name,last_name,'!')
#print('Hello World!')

# x=input('dej liczbe:\n')
# x=int(x)
# print(x,type(x))
# print(x/2)
#
# x=int(  input('dej liczbe:\n') )
# print(x,type(x))
# print(x/2)
#float
#print(round(1/3,2))
#print(pow(10,3))
#x=1.23
#2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika
# jego masę w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.
#
# height=float(input('podaj wzrost:\n'))
# bmi=72/pow(height,2)

# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'Twoje BMI={bmi}')
#
# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=weight/pow(height,2)
# print(f'Twoje BMI={round(bmi,2)}')

# x=1
# if x==1:
#     print('x wynosi jeden')
#     print('siema!')
# print('koniec')

# x=2
# if x==1:
#     print('x jest równe jeden')
# else:
#     print('x NIE jest równe jeden')
#
# x=4
# if x==1:
#     print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# else:
#     print('x mniejsze od jeden lub większe od 3 (albo liczba zmiennoprzecinkowa)')

#3. Niech użytkownik poda jakąś liczbę.
# Jeśli poda dodatnią to chcemy wyświetlić tę wartość
# z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".
# x=1
# if x>0:
#     pass
#
# def bmi(w,m):
#     pass
#
# bmi(1.76,72)
#
# number=int(input('dej liczbę:\n'))
# if number>0:
#     print(number,'jest dodatnia')
# elif number<0:
#     print(number,'jest ujemna')

#
# number=int(input('dej liczbę:\n'))
# if number>0:
#     print(number,'jest dodatnia')
# elif number<0:
#     print(number,'jest ujemna')
# else:
#     print(number,'jest zerem')


# number=int(input('dej liczbę:\n'))
# if number>0:
#     print(number,'jest dodatnia')
# elif number<0:
#     print(number,'jest ujemna')
# elif number==0:
#     print(number,'jest zerem')

# number=int(input('dej liczbę:\n'))
# if number>0:
#     print(number,'jest dodatnia')
# elif number<0:
#     print(number,'jest ujemna')
# else:
#     print(number,'jest zerem')


# 4. Rozbuduj swój program do bmi w taki sposob by
# poza wyswietleniem obliczonego bmi
#   wyświetlił nam również odpowiedni opis wg skali z Wikipedii.

#
# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'Twoje BMI={bmi}')
# if bmi<16:
#     print('wyglodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('waga ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('1 stopień przypakowania')
# elif bmi<40:
#     print('2 stopień przypakowania')
# else:
#     print('3 stopień przypakowania')

#
# for x in range(3):
#     print('siema!')


#
# for _ in range(3):
#     print('siema!')


# for x in range(1,11):
#     print(f'siema! {x}')
#
# for x in range(1,11,2):
#     print(f'siema! {x}')
#
# while True:
#     pass

#
# while 1==1:
#     pass
#
# x=1
# while x<1000:
#     x=x*2
#     print(x)
#
# lista=['koza','nietoperz','toperz']
# for e in lista:
#     print(e)

# for x in (1,11,2):
#     print(f'siema! {x}')

#5. Wyświetl 20 kolejnych potęg liczby 2

# for p in range(1,21):
#     print(f"{p} potęga liczby 2 to",pow(2,p))

# for x in range(-10,11):
#     print(x)

# for x in range(-10,11):
#     print(x)
#     if x<0:
#         print('ujemna')
#     elif x==0:
#         print('zero')
#     else:
#         print('dodatnia')

#
# for x in range(-10,11):
#     if x<0:
#         print(f'{x} ujemna')
#     elif x==0:
#         print(f'{x} zero')
#     else:
#         print(f'{x} dodatnia')

# imie2=input('podaj imie:\n')
# nazwisko2=input('podaj nazwisko:\n')
# print(f"Witaj,{imie2}",imie2,nazwisko2)

#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
  #parzysta czy nieparzysta

# x=12
# print(x%2)
# if x%2==0:
#     print(f'{x} jest parzysty')
# else:
#     print(f'{x} jest nieparzysty')

# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzysty')
#     else:
#         print(f'{x} jest nieparzysty')
#
# x=1
# print(x)
# x=x+1
# x++
# x+=2
# x=x+2
# x*=2
# x=x*2

#7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
  # - kwotę lokaty
  # - oprocentowanie w skali roku
  # - ilość miesięcy na jaką zakladamy lokatę
  # Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
  # oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
  # Kapitalizacja comiesięczna
#
# money=10000
# p=0.05
# tl=24

# for m in range(1,tl+1):
#     money=round(money+(money*p/12),2)
#     print(f"miesiąc={m} hajs={money}")

#
# money=100000
# p=-0.1
# tl=60
#
# for m in range(1,tl+1):
#     money=round(money+(money*p/12),2)
#     print(f"miesiąc={m} hajs={money}")


#8. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby
# 2 aż wartość  potęgi nie przekroczy wartości podanej przez użytkownika


# max=int(input('ile max:\n'))
# result=0
# np=0
# while result<max:
#     np+=1
#     result=pow(2,np)
#     print(result)


# max=int(input('ile max:\n'))
# result=0
# np=0
# while result<max:
#     print(result)
#     np += 1
#     result=pow(2,np)


# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(tekst.replace('a','X'))
# print(tekst.lower().replace('a','X'))
# print(tekst)
# tekst=tekst.upper().replace('A','X').replace('E','Y')
# print(tekst)

#9.  Napisz program który przyjmie od użyszkodnika ciąg tekstowy
# a następnie usunie z niego znaki ,.!? i wyświetli
# powiększony do dużych liter na konsoli

# text=input('dej tekst:\n')
# print(text
#       .replace('.','')
#       .replace(',','')
#       .replace('!','')
#       .replace('?','')
#       .upper()
#       )
#
# Niebo,
# Niebo!
# Niebo.

# text='hello ! ? , . koniec'
# not_wanted=['!','?',',','.','e','l']
# for e in not_wanted:
#     text=text.replace(e,'')
# print(text)

# print(len('siema'))
# print(len([1,2,3,4]))
#print('siema'.len()) #nie ma

# t="        helllooooo         "
# print(t)
# print(t.strip())
#
# t='aaaaa bbbb aaaaa'
# print(t.strip('a'))


# t="        helllooooo         "
# print(len(t))
# print(len(t.strip()))


# for line in open('files/data.csv', encoding='utf-8'):
#     if len(line.strip())>0:
#         print(line.strip(), len(line.strip()))

#10. Napisz program który wyświetli na konsoli niepuste linie
# z pliku tekstowego którego nazwę poda użytkownik
#
# t="siała BABA mak, znowu BABA, a teraz duża BABA"
# if "baba" in t.lower():
#     print('jest baba')
# else:
#     print('nie ma baby')
#
# print(t.lower().count('baba'))
# print(t.upper().count('BABA'))

# text=open('tadzio.txt',encoding='utf-8').read()
# print(text.upper())

#11. Napisz program który zliczy ilość wystąpień małej
# lub dużej wersji ciagu tekstowego podanego przez
# użytkownika w pliku którego nazwę również poda użytkownik.

# file_name=input('podaj nazwę pliku:\n')
# phrase=input('czego szukasz:\n')
# text=open(file_name,encoding='utf-8').read()
# x=text.lower().count(phrase.lower())
# print(x)

#to jest źle - to przykład
# file_name=input('podaj nazwę pliku:\n')
# phrase=input('czego szukasz:\n')
# text=open(file_name,encoding='utf-8').read()
# x=text.count(phrase)
# print(x)

# #to jest dobrze
# file_name=input('podaj nazwę pliku:\n')
# phrase=input('czego szukasz:\n')
# print(open(file_name,encoding='utf-8').read().lower().count(phrase.lower()))

#12. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
#  poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#   linie w których znalazła poszukiwaną frazę wraz z numerem linii.
#   Wyszukiwarka powinna być nieczula na wielkosc liter.

# file_name='tadzio.txt'
# phrase='tadeusz'
# x=0
# for line in open('tadzio.txt',encoding='utf-8'):
#     x+=1
#     if phrase.lower() in line.lower():
#         print(x,line.strip())

# file_name=input('podaj nazwę pliku:\n')
# phrase=input('podaj szukaną frazę:\n')
# x=0
# for line in open(file_name,encoding='utf-8'):
#     x+=1
#     if phrase.lower() in line.lower():
#         print(x,line.strip())

#print('hello')  #komentarz
# tekst='siała baba mak'
# print(tekst[0])
# print(tekst[0:5])
#.13 Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
# Program ma wyświetlić wszystkie linie które nie są w całości komentarzami
# wraz z numerami tych linii w pliku

# file_name='main.py'
# for line in open(file_name,encoding='utf-8'):
#     if len(line.strip())>0 and line.strip()[0]!='#':
#         print(line)



# file_name='main.py'
# for line in open(file_name,encoding='utf-8'):
#     if  line.strip()[0]!='#' and len(line.strip())>0:
#         print(line)
#
# file_name=input('podaj nazwę pliku:\n')
# x=0
# for line in open(file_name,encoding='utf-8').readlines():
#     x+=1
#     if  len(line.strip())>0 and line.strip()[0]!='#':
#         print(x,line.strip())
#
# lista=[]
# lista=list()
# lista=[1,2,'tekst',[3,4] ]
# print(lista,type(lista))
# lista.append(88888)
# zmienna=123
# lista.append(zmienna)
# for e in lista:
#     print(e)
# print(f'pozycja 2={lista[2]}')
# print(lista[0:2])

#14. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
#  Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
#
# result=[]
# for x in range(1,11):
#     result.append(pow(2,x))
# for r in result:
#     print(r)


#
# result=[]
# for x in range(1,11):
#     result.append(pow(2,x))
#     print(result[x-1]) #fuuuuuu

# result=[]
# for x in range(1,11):
#     p=pow(2,x)
#     result.append(p)
#     print(p)
#
# result=[]
# for x in range(1,11):
#     result.append(pow(2,x))
# for i in range(0,len(result)):
#     print(result[i])

#import pandas
# import random
# for x in range(10):
#     print(random.randint(1,1000))
#     print(random.random()*10)
#
# x=1
# y=x
#
# l1=[1,2,3]
# l2=l1
# l1.clear()
# print(l1)
# print(l2)

#
# l1=[1,2,3]
# l2=l1.copy()
# l1.clear()
# print(l1)
# print(l2)

# l1=[1,2,3]
# l2=[4,5,6]
# # print(l1,type(l1))
# # print(l1)
# # print(*l1)
# l3=[  l1,l2  ]
# print(l3)
# for e in l3:
#     print(e)
# def fun(*args):
#     for a in args:
#         print(a)
#
# fun(1,'nietoperz','lubie','pierogi')

#
# l1=[1,2,3]
# l2=[4,5,6]
# l3=[  l1,l2  ]
# print(l3)
# for e in l3:
#     print(e)


# l1=[1,2,3]
# l2=[4,5,6]
# l3=[  *l1,*l2  ]
# print(l3)
# for e in l3:
#     print(e)

# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)


#15. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)

# import random
#
# print(random.randint(1,3))
# print(random.randint(1,3))

# import random
# l1=[]
# l2=[]
# for _ in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
# print(l1)
# print(l2)
# l3=[*l1,*l2]
# print(l3)
# l1.extend(l2)
# print(l1)

# #lista=[1,2,3]
# lista=[ [1,'A'] , [2,'B'] ]
# print(lista)
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,10):
#     element=[x,x*1000]
#     lista.append(element)
# print(lista)
# for e in lista:
#     print(e)
#     print(e[1])

#
# lista=[]
# for x in range(1,10):
#     lista.append([x,x*1000])
# print(lista)
# for e in lista:
#     print(e)

#16. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# [1,2]
# [2,4]
# [3,8]
#
# lista=[]
# for x in range(1,11):
#     element=[x,pow(2,x)]
#     lista.append(element)
#
# for l in lista:
#     print(l)



# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
#
# for l in lista:
#     print(l)

#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
#
# print([x for x in range(1,11)])
#
# print([x*1000 for x in range(1,11)])
#
# import random
# lista=[random.randint(1,10) for _ in range(10)]
# print(lista)
#
#
# print([x for x in range(1,11) if x%2==0])
#
# print([x*1000 for x in range(1,11) if x%2==0])
#
# lista=[x for x in range(1,11)]
# print(lista)
# inna=[e for e in lista if e%2==0]
# print(inna)
#
# inna=[e*1000 for e in lista if e%2==0]
# print(inna)
# import random
# lista=[]
# for _ in range(10):
#     x=random.randint(1,10)
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[random.randint(1,10) for _ in range(10)]
# lista2=[e for e in lista if e%2==0]
# print( lista2 )
#
# print([e for e in  [random.randint(1,10) for _ in range(10)] if e%2==0 ])

#17. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     element=pow(2,x)
#     lista.append(element)
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     lista.append(pow(2,x))
# print(lista)
#
# lista=[pow(2,x) for x in range(1,11)]
# print(lista)
# print([pow(2,x) for x in range(1,11)])

#18. Umieść w liście wartości kolejnych tysięcy od 1000 do 100000.
#. 1000,2000,3000,4000
#
# lista=[]
# for x in range(1,101):
#     lista.append(x*1000)
#
# print(lista)
#
# lista=[x*1000 for x in range(1,101)]
# print(lista)
#
# lista=[x for x in range(1000,100001,1000)]
# print(lista)

# lista=[]
# for x in range(1,11):
#     element=[x,x*1000]
#     lista.append(element)
# print(lista)
#
#
# lista=[]
# for x in range(1,11):
#     lista.append([x,x*1000])
# print(lista)
#
# lista=[[x,x*1000] for x in range(1,11)]
# print(lista)

#19. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla liczby 2

# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
# print(lista)
#
# print([ [x,pow(2,x)] for x in range(1,11)])
#
# for d in open('files/data.csv',encoding='utf-8'):
#     print(d.strip())

#
# string='2;Ferdynand;Kiepski;1.68;90'
# lista=string.split(';')
# print(lista)
# print(lista[1].replace('e','X'))
# print(lista[3],type(lista[3]))
# print(float(lista[3])/2)
#
# hajs='hajs '
# print(hajs*1000)

string='2;Ferdynand;Kiepski;1.68;90'

#20. Napisz program który z pliku data.csv wyświetli powiekszone imiona i nazwiska
#
# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().split(';')
#     print(lista[1])
#     print(lista[1].replace('a','X'))


#
# for d in open('files/data.csv',encoding='utf-8'):
#     print(d.strip().split(';'))
#     print(d.strip().split(';')[1].upper())

#
# for d in open('files/data.csv',encoding='utf-8'):
#     print(d.strip().split(';'))
#     imie=d.strip().split(';')[1]
#     nazwisko=d.strip().split(';')[2]
#     print(imie.upper(),nazwisko.upper())
#
# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().split(';')
#     print(lista[1].upper(),lista[2].upper())


#
# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().upper().split(';') #powiekszamy caly wiersz
#     print(lista[1],lista[2])



# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().upper().split(';') #powiekszamy caly wiersz
#     print(lista[1],lista[2])
#
#
# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().split(';').upper() #to nie ma prawa zadzialac - lancuchowanie funkcji i typy danych
#     print(lista[1],lista[2])
#
# #tak najlepiej
# for d in open('files/data.csv',encoding='utf-8'):
#     lista=d.strip().split(';')
#     print(lista[1].upper(),lista[2].upper())

#
# import time
#
# poczatek=time.time()
# print('start')
# time.sleep(3)
# print('koniec')
# koniec=time.time()
# print(f'czas trwania {koniec-poczatek}s')

#21. Zaladuj do postaci listy list zawartosc pliku data.csv

# result=[]
# for d in open('files/data.csv',encoding='utf-8'):
#     result.append(  d.strip().split(';') )
# print(result)
# for r in result:
#     print(r,r[1])
#
# result=[]
# for x in range(1,11):
#     result.append(x*1000)
#
# result=[x*1000 for x in range(1,11)]
# print(result)

#22. ⦁	Korzystajac z list skladanych zaladuj do listy zawartosc pliku data.csv w taki sposób
# by linie oczyścic z bialych znaków i rozbić na listy. Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy  element po elemencie.


# result=[]
# for d in open('files/data.csv',encoding='utf-8'):
#     result.append(  d.strip().split(';') )

# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     print(r)

#
# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     print(r[3],type(r[3]),r[4],type(r[4]))
#     print(pow(float(r[3]),2))
#     print(r[3]*10)
#     print(   float(r[3])*10  )

#23. Dla każdego wpisu w pliku data.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika

#
# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     print(r)
#     w=float(r[3])


#
# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     h=float(r[3])
#     w=float(r[4])
#     bmi=round(w/pow(h,2),2)
#     print(r,bmi)



# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     h=float(r[3])
#     w=float(r[4])
#     bmi=round(w/pow(h,2),2)
#     r.append(bmi)
#     print(r)


# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     bmi=round(float(r[4])/pow(float(r[3]),2),2)
#     r.append(bmi)
#     print(r)


# result=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# for r in result:
#     r.append(round(float(r[4])/pow(float(r[3]),2),2))
#     print(r)
#
# lista=[1,4,2,8,1,2]
# print(lista)
# lista.sort()
# print(lista)

#
# lista=[1,4,2,8,1,2]
# print(lista)
# posortowane=sorted(lista)
# print(posortowane)
# print(lista)


# lista=[1,4,2,8,1,2]
# print(lista)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)
#
# lista=[1,4,2,8,1,2]
# print(lista)
# lista.sort(reverse=True)
# print(lista)
#
# #
# lista=[1,4,2,8,1,2]
# print(lista)
# posortowane=sorted(lista,reverse=True)
# print(posortowane)

#
# lista=['z','b','d','a']
# print(lista)
# lista.sort()
# print(lista)


# lista=['z','b','d','a',1]
# print(lista)
# lista.sort()
# print(lista)
#
# lista=['z','b','d','a','1']
# print(lista)
# lista.sort()
# print(lista)

#
# lista=['z','b','d','a',str(1)]
# print(lista)
# lista.sort()
# print(lista)

#24.Wygeneruj listę 10 elementów o losowej wartości liczbowej,
# posortuj listę i wyświetl jej zawartość element po elemencie
# import random
# data=[random.randint(1,1000) for _ in range(10)]
# print(data)
# data.sort()
# print(data)
# for d in data:
#     print(d)

#
# import random
# data=[random.randint(1,1000) for _ in range(10)]
# print(data)
# posortowane=sorted(data)
# print(posortowane)
# for d in posortowane:
#     print(d)

#
#
# import random
# data=[random.randint(1,1000) for _ in range(10)]
# for d in sorted(data):
#     print(d)


#
# import random
# for d in sorted( [random.randint(1,1000) for _ in range(10)] ):
#     print(d)



# import random
# for d in sorted( [random.randint(1,1000) for _ in range(10)] ): print(d)

#(a > b, 1,2)

#if 1==1: print('true')
#
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
#
# print(result)
# print(sorted(result))

#
# from operator import itemgetter
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]

# import operator
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# operator.itemgetter

#
# from operator import itemgetter
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(result)
# result.sort(key=itemgetter(1))
# print(result)


#
# from operator import itemgetter
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(result)
# posortowane=sorted(result,key=itemgetter(1))
# print(posortowane)


#
# from operator import itemgetter
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(result)
# posortowane=sorted(result,key=itemgetter(1),reverse=True)
# print(posortowane)

# class Person:
#     first_name=None
#     last_name=None
#
# p=Person()
# p.first_name='Andrew'
# p.last_name='Klusiewicz'
# print(p.last_name,p.first_name)
#
# class Person:
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln

# p=Person('Andrzej','Klusiewicz')
# print(p.last_name,p.first_name)




# class Person:
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#
# data=[
#     Person('Andrzej','Klusiewicz'),
#     Person('Zenek','Martyniuk'),
#     Person('Matka','Stalina'),
#     Person('Maniek','Adowski')
# ]
# for d in data:
#     print(d.first_name,d.last_name)
#
#
#
# from operator import itemgetter
# class Person:
#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln
#
#
# data = [
#     Person('Andrzej', 'Klusiewicz'),
#     Person('Zenek', 'Martyniuk'),
#     Person('Matka', 'Stalina'),
#     Person('Maniek', 'Adowski')
# ]
#
# data.sort(key=itemgetter(1))
#
# for d in data:
#     print(d.first_name, d.last_name)
#


#
# class Person:
#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln
#
#
# data = [
#     Person('Andrzej', 'Klusiewicz'),
#     Person('Zenek', 'Martyniuk'),
#     Person('Matka', 'Stalina'),
#     Person('Maniek', 'Adowski')
# ]
#
# data.sort(key=lambda d:d.last_name)
#
# for d in data:
#     print(d.first_name, d.last_name)
#

#
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# result.sort(key=lambda e:e[1].upper())
# print(result)



# def my_fun(x):
#     return x[1]
#
# result=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# result.sort(key=lambda e:my_fun(e))
# print(result)

#24. Wczytaj do listy kolejne wiersze z pliku data.csv.
# Dane posortuj po wadze i wyswietl linia po linii na konsoli.
#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# for d in data:
#     print(d)

# from operator import itemgetter
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# data.sort(key=itemgetter(4))
# for d in data:
#     print(d)

#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# data.sort(key=lambda x:x[4])
# for d in data:
#     print(d)

#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# data.sort(key=lambda x:float(x[4]))
# for d in data:
#     print(d)

#
# lista=[22,11,1,2]
# lista.sort()
# print(lista)
#
#
#
# lista=['22','11','1','2']
# lista.sort()
# print(lista)

#25. Wyświetl na konsoli linia po linii dane z pliku data.csv ale posortowane  malejąco wg. bmi

# 1. Wczytać dane z pliku jako listę list
# 2. Do każdego elementu listy dodać obliczone bmi
# 3. Sortowanko
# 4. Wyświetlanko
#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# for d in data:
#     h=float(d[3])
#     w=float(d[4])
#     bmi=round(w/ h ** 2,2)
#     d.append(bmi)
# data.sort(key=lambda e:e[5])
# for d in data:
#     print(d)


#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# for d in data:
#     h=float(d[3])
#     w=float(d[4])
#     bmi=round(w/ h ** 2,2)
#     d.append(bmi)
# data.sort(key=lambda e:e[5],reverse=True)
# for d in data:
#     print(d)


#
# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# for d in data: d.append(round(float(d[4])/ float(d[3]) ** 2,2))
# data.sort(key=lambda e:e[5],reverse=True)
# for d in data:
#     print(d)



# data=[e.strip().split(';') for e in open('files/data.csv',encoding='utf-8')]
# for d in data:
#     d.append(round(float(d[4])/ float(d[3]) ** 2,2))
# data.sort(key=lambda e:e[5],reverse=True)
# for d in data:
#     print(d)
#
# import os
# os.mkdir('g:\\whatever')
#
# import os
# for e in os.walk('G:\\'):
#     print(e)
#
# lista=['a','b','c']
# print(lista[1])
# krotka=('a','b','c')
# print(krotka[1])
#krotka.append('cośtam') #to nie zadziala bo to krotka (niemutowalna)



# import os
# for e in os.walk('G:\\'):
#     print(e)
#
# import os
# for e in os.walk('G:\\'):
#     print(e[0])

#
# import os
# for e in os.walk('G:\\'):
#     print(e)


#
# import os
# for e in os.walk('G:\\'):
#     sciezka=e[0]
#     pliki = e[2]
#     print(sciezka,'pliki=',pliki)
#     for p in pliki:
#         if p=='moto.txt':
#             print(f'znalazłem w {sciezka}')

#
# import re
# cos='aaaaaa 1234 aaaaaa'
# print(re.findall('\d{1,}',cos))

#
# import os
# for e in os.walk('G:\\'):
#     sciezka=e[0]
#     pliki = e[2]
#     print(sciezka,'pliki=',pliki)
#     for p in pliki:
#         if p=='moto.txt':
#             print(f'znalazłem w {sciezka}')

#
# lista=['cos','toperz','nietoperz','moto','moto.txt','moto.png','moto.wtf','cos jeszcze','cos tam jeszcze innego']
# if 'moto' in lista:
#     print('jest')
# else:
#     print('nie ma')


#
# lista=['cos','toperz','nietoperz','moto.txt','moto.png','moto.wtf','cos jeszcze','cos tam jeszcze innego']
# if 'moto' in lista:
#     print('jest')
# else:
#     print('nie ma')


# lista=['cos','toperz','nietoperz','moto.txt','moto.png','moto.wtf','cos jeszcze','cos tam jeszcze innego']
#
# string='siała baba mak'
# if 'baba' in string:
#     print('jest baba')

# lista=['cos','toperz','nietoperz','moto.txt','moto.png','moto.wtf','cos jeszcze','cos tam jeszcze innego']
# for l in lista:
#     if 'moto' in l:
#         print(l, 'tu jest')
#     else:
#         print(l,'tu nie ma')

# lista=['cos','toperz','nietoperz','Moto.txt','mOTO.png','moto.wtf','cos jeszcze','cos tam jeszcze innego']
# for l in lista:
#     if 'moto'.lower() in l.lower():
#         print(l, 'tu jest')
#     else:
#         print(l,'tu nie ma')

#26. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter


import os
for e in os.walk('G:\\'):
    print(e)