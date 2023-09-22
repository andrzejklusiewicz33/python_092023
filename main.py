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


# import os
#
# find_me='cośtam'
# for e in os.walk('G:\\'):
#     print(e)
#     katalogi=e[1]
#     for k in katalogi:
#         #tu sprawdz czy find_me znajduje się w k (lower() maybe)
#         pass

# #os.path.join
# import os
# katalog='g:\\costam'
# plik='jakistam'
# print(katalog,plik)
# print(os.path.join(katalog,plik))




#
# import os
# find_me='C'
# for e in os.walk('G:\\'):
#     katalogi=e[1]
#     for k in katalogi:
#         if find_me.lower() in k.lower():
#             print(e[0],k)
# #
# import os
# print( os.path.getctime('G:\\whatever\\moto.txt') )

#
# import os
# find_me='whate'
# for e in os.walk('G:\\'):
#     katalogi=e[1]
#     for k in katalogi:
#         if find_me.lower() in k.lower():
#             #print(e[0]+'\\'+k)
#             print(os.path.join(e[0],k))

#
# import os
# find_me='whate'
# for e in os.walk('G:\\'):
#     katalogi=e[1]
#     pliki=e[2]
#     for k in katalogi:
#         if find_me.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in pliki:
#         if find_me.lower() in p.lower():
#             print(os.path.join(e[0],p))



# import os
# find_me='whate'
# for e in os.walk('G:\\'):
#     for k in e[1]:
#         if find_me.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if find_me.lower() in p.lower():
#             print(os.path.join(e[0],p))


# import os
# find_me=input('czego szukać?\n')
# where=input('gdzie mam szukać?\n')
# for e in os.walk(where):
#     for k in e[1]:
#         if find_me.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if find_me.lower() in p.lower():
#             print(os.path.join(e[0],p))
#
#
# import os
# for e in os.walk('g:\\'):
#     for p in e[2]:
#         if p.endswith('.txt'):
#             full_path=os.path.join(e[0],p)
#             x=0
#             for line in open(full_path,encoding='utf-8'):
#                 x+=1
#                 if 'koza' in line:
#                     print(f'line={x}',full_path,line)
#
# lista=[2,6,1,2,3]
# lista.append(7777)
# print(lista,type(lista))
# krotka=(2,6,1,2,3)
# krotka.append(5)
# print(krotka,type(krotka))

# lista=[2,6,1,2,3]
# lista.sort()
# krotka=(2,6,1,2,3)
# posortowane=sorted(krotka)
# print(posortowane)
#
# krotka=(2,6,1,2,3)
# print(krotka)
# lista=list(krotka)
# print(lista)
# #lista.sort()
# lista.append('cośtam')
# print(lista)
# krotka=tuple(lista)
# print(krotka)
#
# krotka=(2,6,1,2,3)
# for k in krotka:
#     print(k)
# if 6 in krotka:
#     print('jest')
# print(krotka[4])
# print(krotka[0:4])

#27. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli
#
# krotka=(e for e in range(1,11))
# print(krotka)


# krotka=tuple([e for e in range(1,11)]
# print(krotka)
#
# import random
# k1=tuple([random.randint(1,10) for x in range(1,11)])
# k2=tuple([random.randint(11,21) for x in range(1,11)])
# k3=(*k1,*k2)
# print(*k1)
# print(*k2)
# print(*k3)
#
# def fun():
#     import random
#     result=[]
#     while True:
#         result.append(random.randint(1,10))
#     return result
#
# r=fun()

# def generator():
#     import random
#     while True:
#         yield random.randint(1,10)
#
# for g in generator():
#     print(g)

#
# krotka = (e for e in range(1, 11))
# print(type(krotka))
#
# krotka = tuple([e for e in range(1, 11)])
# print(type(krotka))


#27. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli
# import random
# k1=tuple([random.randint(1,10) for _ in range(10)])
# k2=tuple([random.randint(11,20) for _ in range(10)])
# print(k1,type(k1))
# print(k2,type(k2))
# #k3=(*k1,*k2)
# k3=tuple([*k1,*k2])
# print(k3,type(k3))

#28. ⦁	Załaduj zawartosc data.csv do postaci listy krotek, a nasterpnie przeiteruj
#osobna petla po tej liscie i wyswietl jej elementy.
#
# # result=[]
# # for l in open('files/data.csv',encoding='utf-8'):
# #     result.append(l.strip().split(';'))
#
# result=[l.strip().split(';') for l in open('files/data.csv',encoding='utf-8')]
#
# for r in result:
#     print(r)

#
# result=[]
# for l in open('files/data.csv',encoding='utf-8'):
#     result.append(    tuple(l.strip().split(';'))   )

# result=[ tuple(l.strip().split(';')) for l in open('files/data.csv',encoding='utf-8')]
#
# for r in result:
#     print(r)
#
# print(result)
#
# lista=[1,1,1,1,2,2,2,2]
# zbior={1,1,1,1,2,2,2,2}
#slownik={"klucz1": 'costam', "klucz2": 12334}
#
# print(lista)
# print(zbior)


# lista=[1,1,1,1,2,2,2,2]
# zbior=set(lista)
# zbior.add(3)
# zbior.add(3)
# zbior.add(3)
# print(zbior)

#
# z1={1,2,3,4}
# z2={3,4,5,6}
# print('czesc wspolna',z1.intersection(z2))
# print('czesc wspolna',z2.intersection(z1))
# print('suma',z1.union(z2))
# print('roznica z1-z2',z1.difference(z2))
# print('roznica z2-z1',z2.difference(z1))

#
# lista=[1,2,2,3,3,3,3,3,4,4,4,4]
# z=set(lista)
# print(z)
# lista=list(z)
# print(lista)
#
# lista=[1,2,2,3,3,3,3,3,4,4,4,4]
# lista=list(set(lista))
# print(lista)

#
# lista=list(set([1,2,2,3,3,3,3,3,4,4,4,4]))
# print(lista)
#
# print(list(set([1,2,2,3,3,3,3,3,4,4,4,4])))

#29 ⦁	Wygeneruj dwa zestawy, dodaj do nich po 20
# (w przypadku duplikatów zestaw może być mniejszy niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną
#
# import random
# z1=set()
# z2=set()
# for _ in range(20):
#     z1.add(random.randint(1,40))
#     z2.add(random.randint(1, 40))
#
# print('czesc wspolna',z2.intersection(z1))
# print('suma',z1.union(z2))
# print('roznica z1-z2',z1.difference(z2))
# print('roznica z2-z1',z2.difference(z1))
#
#
# import random
# z1=set([random.randint(1,40) for _ in range(20)])
# z2=set([random.randint(1,40) for _ in range(20)])
#
#
# print('czesc wspolna',z2.intersection(z1))
# print('suma',z1.union(z2))
# print('roznica z1-z2',z1.difference(z2))
# print('roznica z2-z1',z2.difference(z1))
#

#
# import random
# z1={random.randint(1,40) for _ in range(20)}
# z2={random.randint(1,40) for _ in range(20)}
#
#
# print('czesc wspolna',z2.intersection(z1))
# print('suma',z1.union(z2))
# print('roznica z1-z2',z1.difference(z2))
# print('roznica z2-z1',z2.difference(z1))


#30 ⦁	Zduplikuj jeden z wierszy w pliku data.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.
# Nastepnie przejdz po tej liscie wynikowej i wyswietl jej elementy.
#
# lista=[
#     (1,'A'),
#     (2,'B'),
#     (1,'A')
# ]
#
# print(lista)
# lista=list(set(lista))
# print(lista)

#
# result=[tuple(e.strip().split(';')) for e in open('files/data.csv',encoding='utf-8')]
# result=list(set(result))
# print(type(result))
# for r in result:
#     print(r)


# for r in list(set([tuple(e.strip().split(';')) for e in open('files/data.csv',encoding='utf-8')])):
#     print(r)

# file=open('results.csv',mode='w',encoding='utf-8')
# file.close()

# with open('results.csv',mode='w',encoding='utf-8') as file:
#     pass
# print('ok')
#
# with open('results.csv',mode='w',encoding='utf-8') as file:
#     file.write('whatever')
# print('ok')

#
# with open('results.csv',mode='w',encoding='utf-8') as file:
#     for x in range(1,11):
#         file.write(f'x={x}\n')
# print('ok')

#
# element=['1','Andrzej','Klusiewicz',1.76,80]
# string=f'{element[0]};{element[1]};{element[2]};{element[3]};{element[4]}\n'
# print(string)
#
# with open('results.csv',mode='w',encoding='utf-8') as file:
# print('ok')

#
# element=['1','Andrzej','Klusiewicz','1.76','80']
# string=f'{element[0]};{element[1]};{element[2]};{element[3]};{element[4]}\n'
# nowy_string=";".join(element)
# print(string)
# print(nowy_string)

#
# element=['1','Andrzej','Klusiewicz',str(1.76),str(80)]
# nowy_string=";".join(element)
# print(nowy_string)

#31. Przepisz zawartość data.csv do pliku results.csv linia po linii
#
# plik=open('results.csv',encoding='utf-8',mode='w')
# for w in open('files/data.csv'):
#     plik.write(w)


#
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for w in open('files/data.csv'):
#         file.write(w)
#
# data=[e for e in open('files/data.csv',encoding='utf-8')]
# for d in data:
#     print(d)

#
# data=[e for e in open('files/data.csv',encoding='utf-8')]
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         file.write(d)


# result=[]
# for l in open('files/data.csv',encoding='utf-8'):
#      result.append(l)
#
# with open('results.csv',mode='w',encoding='utf-8') as file:
#    for r in result:
#         file.write(f'{r}')


#32. Zaladuj zawartosc pliku data.csv do postaci listy stringów, ale
# nie ładuj pustych linii i wszystkie wystąpienia "," zamień na ".".
# Następnie przeiteruj po liście i zrzuć jej zawartość do pliku results.csv

#https://github.com/andrzejklusiewicz33/python_092023/blob/main/main.py
#
# data=[e.replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         file.write(d)

#33. Przerób rozwiązanie poprzedniego ćwiczenia w taki sposób, by pozbyć się też duplikatów

#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         file.write(f'{d}\n')
#         print(d)


# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     x=0
#     for d in data:
#         x+=1
#         if x<len(data):
#             file.write(f'{d}\n')
#         else:
#             file.write(d)
#         print(d)

#34. Wyświetl na konsoli dane z pliku data.csv wzbogacone o bmi. Zadbaj po drodze
#o usunięcie pustych linii, usunięcie duplikatów i zamianę ',' na '.'

# lista=[4,3,1,2]
# z=set(lista)
# print(lista)
# print(z)

# s={
#     (1,2),
#     (3,4)
# }
#
# s={
#     [1,2],
#     [3,4]
# }


# #
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         print(d)


#34. Wyświetl na konsoli dane z pliku data.csv wzbogacone o bmi. Zadbaj po drodze
#o usunięcie pustych linii, usunięcie duplikatów i zamianę ',' na '.'
#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         h=float(l[3])
#         w=float(l[4])
#         bmi=round(w/pow(h,2),2)
#         print(*l,bmi)


#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         h=float(l[3])
#         w=float(l[4])
#         bmi=round(w/pow(h,2),2)
#         l.append(bmi)
#         print(*l)


#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         h=float(l[3])
#         w=float(l[4])
#         bmi=round(w/pow(h,2),2)
#         l.append(bmi)
#         #print(*l)
#         print(f'{l[0]};{l[1]};{l[2]};{l[3]};{l[4]};{l[5]}')


#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         h=float(l[3])
#         w=float(l[4])
#         bmi=round(w/pow(h,2),2)
#         l.append(str(bmi))
#         #print(*l)
#         line=";".join(l)
#         print(line)
#         #print(f'{l[0]};{l[1]};{l[2]};{l[3]};{l[4]};{l[5]}')
#
#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         l.append(str(round(float(l[4])/pow(float(l[3]),2),2)))
#         print(";".join(l))

#35. ⦁	Przetwórz plik data.csv w taki sposób by w efekcie umieścić w pliku results.csv
# dane z pliku data.csv wzbogacone o obliczone BMI,
# bez duplikatów, pustych wierszy i rozwiązując problem podania
# przecinka w miejsce kropki we wzroście i masie.
#
# data=list(set([e.strip().replace(',','.') for e in open('files/data.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('results.csv',encoding='utf-8',mode='w') as file:
#     for d in data:
#         l=d.split(';')
#         l.append(str(round(float(l[4])/pow(float(l[3]),2),2)))
#         file.write(";".join(l)+"\n")
#
# from faker import Faker
# f=Faker("PL_pl")
# print(f.first_name(),f.last_name(),f.company(),f.email(),f.city())
# print(f.paragraph())

#36. Wygeneruj plik csv z 10000 wierszy zawieracymi id, imie, nazwisko, nazwa firmy, email, telefon, miasto

import psycopg2
#
# from faker import Faker
# f=Faker("PL_pl")
# with open('persons.csv',encoding='utf-8',mode='w') as file:
#     for x in range(1,10001):
#         lcsv=f'{x};{f.first_name()};{f.last_name()};{f.company()};{f.email()};{f.phone_number()};{f.city()}'
#         #print(lcsv)
#         file.write(lcsv+"\n")

#print(config['listen_addresses'])
#
# d=dict()
# d['encoding']='utf-8'
# print(d['encoding'])
# d['lista']=[1,2,3,4]
# d['krotka']=(5,6,7,8)
# d['liczba']=1234567890
# print(d)
# for k in d:
#     print(k,d[k])
# for v in d.values():
#     print(v)

#37. Stwórz plik config.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
#
# ⦁	Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze
# a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
#
# data=[e.strip().split("=") for e in open('config.conf',encoding='utf-8')]
# cf=dict()
# for d in data:
#     print('klucz=',d[0],'wartosc=',d[1])

# Python program to read
# json file
#
# import json
#
# # Opening JSON file
# f = open('config.conf')
# data = json.load(f)
# print(data)
#
#
# conf=dict([e.strip().split("=") for e in open('config.conf',encoding='utf-8')])
# print(conf)


#37. Stwórz plik config.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
#
# ⦁	Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze
# a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
#
# data=[e.strip().split("=") for e in open('config.conf',encoding='utf-8')]
# cf=dict()
# for d in data:
#     klucz=d[0]
#     wartosc=d[1]
#     print('klucz=', klucz, 'wartosc=', wartosc)
#     cf[klucz]=wartosc
# print(cf)
#
# data=[e.strip().split("=") for e in open('config.conf',encoding='utf-8')]
# cf=dict()
# for d in data:
#     klucz=d[0]
#     wartosc=d[1]
#     cf[klucz]=wartosc
# for k in cf:
#     print(k,cf[k])


# data=[e.strip().split("=") for e in open('config.conf',encoding='utf-8')]
# cf=dict()
# for d in data:
#     cf[ d[0] ]=d[1]
# # for k in cf:
# #     print(k,cf[k])
#
# print(cf['encoding'])

#38. ⦁	Wczytaj do słownika dane z pliku data.csv tak by kluczem
# było imię sklejone z nazwiskiem rozdzielone spacja, a całe wiersze znalazły się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

#print(dane['Andrzej Klusiewicz'])
#
# data=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# sl=dict()
# for d in data:
#     key=d[1]+" "+d[2]
#     value=d
#     sl[key]=value
# for k in sl:
#     print(k,sl[k])


#
# data=[d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]
# sl=dict()
# for d in data:
#     sl[d[1]+" "+d[2]]=d
# for k in sl:
#     print(k,sl[k])


#
# sl=dict()
# for d in [d.strip().split(';') for d in open('files/data.csv',encoding='utf-8')]:
#     sl[d[1]+" "+d[2]]=d
# for k in sl:
#     print(k,sl[k])
#
# linia='1*Andrzej*Klusiewicz'
# print(linia,type(linia))
# lista=linia.split('*')
# print(lista,type(lista))

#39. ⦁	Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej wspólnej listy.
#       Czyli po prostu lista wszystkich słów (z powtórzeniami)
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#       Zunifikuj tez wielkosc liter
#       wynik: ['slowo1','slowo2','tadeusz','cokolwiek','slowo1']
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
#
#

# str='a b c\nd'
# print(str.split())
# Tadeusz
# Tadeusz!
# Tadeusz?
# Tadeusz.
#
# Slowo
# slowo
#
# sl=dict()
# sl['key']='cośtam'
#
# if 'key' in sl:
#     print('jest')
# else:
#     print('nie ma')

# all=open('tadzio.txt',encoding='utf-8').read().lower()
# not_wanted=[',','.','!','?','/','%',')','(','-',':']
# for n in not_wanted:
#     all=all.replace(n,'')
# words=all.split()
# print(words)

#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#

# lista=['koza','nietoperz','czas na grzybobranie','koza']
# print(lista.count('koza'))
#
# import time
# s=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# not_wanted=[',','.','!','?','/','%',')','(','-',':']
# for n in not_wanted:
#     all=all.replace(n,'')
# words=all.split()
# sl=dict()
# for w in words:
#     x=words.count(w) #fuuuuu - złożoność obliczeniowa
# k=time.time()
# print(f'czas trwania {k-s}s')

#
# import time
# s=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# not_wanted=[',','.','!','?','/','%',')','(','-',':']
# for n in not_wanted:
#     all=all.replace(n,'')
# words=all.split()
# sl=dict()
# for w in words:
#     if w in sl:
#         sl[w]=sl[w]+1 #zwiększ wartość dla tego klucza w słowniku o jeden
#     else:
#         sl[w]=1 #dodać do słownika wpis o takim kluczu jak to słowo z wartością 1
# for k in sl:
#     print(k,sl[k])
# k=time.time()
# print(f'czas trwania {k-s}s')


# data=[(1,'B'),(2,'A'),(3,'C')]
# sorted_data=sorted(data,key=lambda x:x[1])
# for sd in sorted_data:
#     print(sd)
#) Przepakuj dane ze słownika do listy i posortuj.
#
# import time
# s=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# not_wanted=[',','.','!','?','/','%',')','(','-','—',':']
# for n in not_wanted:
#     all=all.replace(n,'')
# words=all.split()
# sl=dict()
# for w in words:
#     if w in sl:
#         sl[w]=sl[w]+1 #sl[w]+=1
#     else:
#         sl[w]=1
# result=[]
# for k in sl:
#     row=[k,sl[k]]
#     result.append(row)
# result.sort(key=lambda e:e[1], reverse=True)
# for r in result:
#     print(r)
# k=time.time()
# print(f'czas trwania {k-s}s')

# print(ord('C'))
# print(chr(67))

#slownik['klucz']=1
#slownik['klucz']=slownik['klucz']+1
#slownik['klucz']+=1

# if 'key' in sl:
#     print('jest')
# else:
#     print('nie ma')

#klusiewicz@jsystems.pl
#
# print('start')
# print(1/0)
# print('koniec')

#40. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
# for x in range(-10,11):
#     print(x,1/x)
#
# print('start')
# try:
#     print(1/0)
#     print('coś jeszcze do zrobienia')
# except:
#     print('jakiś wyjątek!')
# print('koniec')


#
# print('start')
# try:
#     print(1/0)
#     print('coś jeszcze do zrobienia')
# except Exception as e:
#     print(f'jakiś wyjątek! {e} {type(e)}')
# print('koniec')


#
# print('start')
# try:
#     print(1/0)
#     print('coś jeszcze do zrobienia')
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# print('koniec')



# print('start')
# try:
#     print(1/0)
#     print('coś jeszcze do zrobienia')
# except FileNotFoundError:
#     print('nie ma takiego pliku')
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# print('koniec')
#
# import requests
# print('start')
# try:
#     requests.get('https://adresktoregoniema.gov')
#     print('coś jeszcze do zrobienia')
# except FileNotFoundError:
#     print('nie ma takiego pliku')
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# except:
#     print('jakiś inny wyjątek')
# print('koniec')

#
# import requests
# print('start')
# try:
#     requests.get('https://adresktoregoniema.gov')
#     print('coś jeszcze do zrobienia')
# except FileNotFoundError:
#     print('nie ma takiego pliku')
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# except Exception as e:
#     print(f'jakiś inny wyjątek. {e} {type(e)}')
# print('koniec')

#
# lista=['persons.csv','result.csv','niematakiego.csv','tadzio.txt','wynik.txt']
# for f in lista:
#     try:
#         print(f'przetwarzanie {f}')
#         open(f)
#     except FileNotFoundError:
#         print(f'############## nie moglem znalezc pliku {f}')

#
# print('start')
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# print('coś jeszcze do zrobienia')
# print('koniec')

#41. ⦁	Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10
# w taki sposob by w przypadku wyjatku nie przerywac dzialania petli
# a po prostu wyswietlic na konsoli informację o błędzie i przejsc
# do dalszego przetwarzania
#
# for x in range(-10,11):
#     print(1/x)

#
# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except:
#         print('error......')


# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except Exception as e:
#         print(f'error...... {type(e)}')


# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'nie dziel przez zero!')


#42. ⦁	Przetwórz wszystkie wiersze z data.csv
#  wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
#  Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się wyjątku dla
#  któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku errors.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;Klusiewicz;1,89;90;IOERROR

# lista=['1','Andrzej','Klusiewicz']
# print(lista)
# print(';'.join(lista)+";ZeroDivisionError")


# print(1/0)
#
# print(1,68/2.5)
# print(1.68/2.5)
# print(1,2,3,4)


#
# data=[e.strip().split(';') for e in open('files/data.csv')]
# for d in data:
#     try:
#         height=float(d[3])
#         weight=float(d[4])
#         bmi=round(weight/height**2,2)
#         d.append(bmi)
#         print(d)
#     except ValueError:
#         print('fakap'+str(d))


#
# data=[e.strip().split(';') for e in open('files/data.csv')]
# for d in data:
#     try:
#         height=float(d[3])
#         weight=float(d[4])
#         bmi=round(weight/height**2,2)
#         d.append(bmi)
#         print(d)
#     except ValueError:
#         log_line=";".join(d)+";ValueError"
#         print(log_line)


#
# data=[e.strip().split(';') for e in open('files/data.csv')]
# for d in data:
#     try:
#         height=float(d[3])
#         weight=float(d[4])
#         bmi=round(weight/height**2,2)
#         d.append(bmi)
#         print(d)
#     except ValueError:
#         log_line=";".join(d)+";ValueError"
#         print(log_line)




# data=[e.strip().split(';') for e in open('files/data.csv')]
# for d in data:
#     try:
#         height=float(d[3])
#         weight=float(d[4])
#         bmi=round(weight/height**2,2)
#         d.append(bmi)
#         print(d)
#     except ValueError:
#         with open('errors.csv',mode="w",encoding='utf-8') as log:
#             log_line=";".join(d)+";ValueError"
#             print(log_line)
#             log.write(log_line+'\n')


# data=[e.strip().split(';') for e in open('files/data.csv')]
# for d in data:
#     try:
#         height=float(d[3])
#         weight=float(d[4])
#         bmi=round(weight/height**2,2)
#         d.append(bmi)
#         print(d)
#     except ValueError:
#         with open('errors.csv',mode="a",encoding='utf-8') as log:
#             log_line=";".join(d)+";ValueError"
#             print(log_line)
#             log.write(log_line+'\n')

#data=get_data('data.csv',';')

# data=[e.strip().split(';') for e in open('files/data.csv')]
# with open('errors.csv', mode="w", encoding='utf-8') as log:
#     for d in data:
#         try:
#             height=float(d[3])
#             weight=float(d[4])
#             bmi=round(weight/height**2,2)
#             d.append(bmi)
#             print(d)
#         except ValueError as ve:
#             log_line=";".join(d)+f";ValueError;{ve}"
#             log.write(log_line+'\n')


#DRY
#
# def dodawanie(a,b):
#     wynik=a+b
#     return wynik
#
# q=dodawanie(2,3)
# print(q)
#
# print(dodawanie(3,4))
#
# def witacz(imie):
#     print(f'siema {imie}! Ładnie dziś wyglądasz')
#
# witacz('Andrzej')
#
# def odejmowanie(a,b):
#     return a-b
#
# print(odejmowanie(10,8))
#
# def mnozenie(a,b):
#     return a*b
#     print('coś co nigdy nie nastapi')
#
# print(mnozenie(6,9))
#
# def fun():
#     data=[1,2,3,4,5]
#     return data
#
# q=fun()
# for d in q:
#     print(d)
#
# for d in fun():
#     print(d)

#44. ⦁	Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone
# do 2 miejsc po przecinku BMI. W przypadku pojawienia się wyjątku,
# wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.
#
# def dodatnia_ujemna(x):
#     if x<0:
#         return 'ujemna'
#     elif x==0:
#         return 'zero'
#     else:
#         return 'dodatnia'
#
# print(dodatnia_ujemna(1))
# print(dodatnia_ujemna(0))
# print(dodatnia_ujemna(-1))
#
# import re
# try:
#     print(1/0)
# except Exception as e :
#     #print(type(e.with_traceback()))
#     print(re.findall("'.*'",str(type(e)))[0].replace("'",''))
#
# def bmi(h,w):
#     try:
#         return round(w/pow(h,2),2)
#     except ....:
#         ....
#     except ....:
#         ....
#
# print(  bmi(1.76,80)  )
# print(  bmi(0,80)  )
# #print(  bmi(1.76,"gruby")  )

#
#
# def bmi(h,w):
#     try:
#         return round(w/pow(h,2),2)
#     except ZeroDivisionError:
#         print('Podany wzrost wynosi 0')
#         return -1
#     except TypeError:
#         print("Podane wartości muszą być liczbami")
#         return -1
#     except Exception as e:
#         print(f"Inny wyjątek: {type(e)} {e}")
#
# a=1.75
# b=90
# try:
#     print( bmi(a,b,1) )
# except TypeError as t:
#     print(t)
#
#
# print("bmi=",  bmi(1.76,80)  )
# print("bmi=",  bmi(0,80)  )
# print("bmi=",  bmi(1.76,"gruby")  )
#
# def fun(arg):
#     file=open(arg)
#
# fun('errors.csv')

# def witacz(imie,nazwisko):
#     print(f"Witaj {imie} {nazwisko}!")
#
# witacz('Andrzej','Klusiewicz')


# def witacz(imie,nazwisko="Nie podano"):
#     print(f"Witaj {imie} {nazwisko}!")
#
# witacz("Andrzej","Klusiewicz")
# witacz('Andrzej')



# def witacz(imie="Nie podano",nazwisko="Nie podano"):
#     print(f"Witaj {imie} {nazwisko}!")
#
# witacz("Andrzej","Klusiewicz")
# witacz('Andrzej')
# witacz()

# def witacz(imie="Nie podano",nazwisko): #fuuuuu
#     print(f"Witaj {imie} {nazwisko}!")
#
# witacz("Andrzej","Klusiewicz")
# witacz('Andrzej')


#45. ⦁	 Napisz funkcję która zwróci pod postacią listy list zawartość pliku
  # którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
  # podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8


# def krotkowiec(v_file,v_encoding='utf-8'):
#     lista = [_ for _ in open(v_file, encoding=v_encoding)]
#     for l in lista:
#
#         k=tuple(l.split(';'))
#         print(k)
#     return lista

# def get_csv(file_name,enc='utf-8',delimiter=';'):
#     return [e.strip().split(delimiter) for e in open(file_name,encoding=enc)]
#
# #lista=[e.strip().split(';') for e in open('files/data.csv')]
# for l in get_csv('files/data.csv','utf-8',';'):
#     print(l)
#
# for l in get_csv('files/data.csv',delimiter=';'):
#     print(l)
#
# for l in get_csv(delimiter=';',enc='utf-8',file_name='files/data.csv'):
#     print(l)

#46. Przerób rozwiązanie poprzedniego ćwiczenia w taki sposób, by rozdzielacz tez był podany
# przez argument funkcji, a w przypadku jego niepodania przyjmował ";"
# def get_csv(file_name,enc='utf-8',delimiter=';'):
#     return [e.strip().split(delimiter) for e in open(file_name,encoding=enc)]

# #lista=[e.strip().split(';') for e in open('files/data.csv')]
# for l in get_csv('files/data.csv','utf-8',';'):
#     print(l)
#
# for l in get_csv('files/data.csv',delimiter=';'):
#     print(l)
#
# for l in get_csv(delimiter=';',enc='utf-8',file_name='files/data.csv'):
#     print(l)

#47. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.

# def get_csv(file_name,enc='utf-8',delimiter=';'):
#     return [e.strip().split(delimiter) for e in open(file_name,encoding=enc)]
#
# lista=[1,2,3,4]
# def print_list(data):
#     pass
#
# print_list(lista)





# def get_csv(file_name,enc='utf-8',delimiter=';'):
#     return [e.strip().split(delimiter) for e in open(file_name,encoding=enc)]
#
# def print_list(data):
#     for e in data:
#         print(e)

# data=get_csv('files/data.csv')
# print_list(data)
#
# print_list( get_csv('files/data.csv')  )

# lista=[1,2,3,4]
# print_list(lista)


# import stuff
#
# stuff.fun()



# import stuff as s
#
# s.fun()
#
# from stuff import fun
# fun()

#
# from stuff import fun,inna
# fun()
# inna()

#
# from stuff import *
# fun()
# inna()

# def funkcja():
#     print('pierwsza wersja')
#
# def funkcja():
#     print('druga wersja')
#
# from stuff import funkcja
# funkcja()
#
# import invoice_dao as idao
# import participant_dao as pdao
# idao.get_all()
# pdao.get_all()

# from invoice_dao import get_all
# from participant_dao import get_all
# get_all()
# get_all()

#import invoice_dao

#import this

#48. Oddeleguj do osobnego modulu "utils" funkcje z ostatnich 2 cwiczen (jedna zwaracajaca plik csv jako lista list,
# druga przyjmujaca liste list i drukujaca na ekranie). Następnie odbierz dane od pierwszej funkcji
# i przekaż do drugiej.
#
# import utils as u
#
# u.print_list( u.get_csv('files/data.csv')  )
#
# import dao.invoice_dao as idao
# idao.get_all()
#
# from dao.invoice_dao import *
# get_all()

#import dao.invoice_dao

#pl.jsystems.phoenix.dao

#49. Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było
# podawać nazwy pakietu ani modułu.
#
# import tools.body
# print(tools.body.bmi(1.76,90))
#
# #
# import tools.body  as tb
# print(tb.bmi(1.76,90))
#
# from tools.body import bmi
# print(bmi(1.76,90))

# import requests
# response=requests.get('https://jsystems.pl/static/blog/python/dane.json')
# print('kod odpowiedzi:',response.status_code)
# if response.status_code==200:
#     print('ok')

#
# import requests
# response=requests.get('https://jsystems.pl/static/blog/python/dane.json')
# print('kod odpowiedzi:',response.status_code)
# if response.status_code==200:
#     print('ok')
#     #print(response.text)
#     #print(response.json())
#     data=response.json()
#     print(data['imie'])
#     address=data['adres']
#     print(address['miasto'])
#     print(data['adres']['miasto'])
#     print('jezyki:')
#     # languages=data['jezyki']
#     # for l in languages:
#     #     print(l)
#     for l in data['jezyki']:
#         print(l)


#50. Pobierz dane z https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json
# wyświetl na konsoli aktualny kurs franka i pole effectiveDate

# import requests
# response=requests.get('https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json')
# if response.status_code==200:
#     data=response.json()
#     found=data['rates'][0]
#     print(found['effectiveDate'],found['mid'])

#51. ⦁	z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi badz duzymi
# literami "Python".
#
# import requests
# response=requests.get('https://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     data=response.json()
#     for d in data:
#         if "Python".lower() in d['tytul_szkolenia'].lower():
#             print(d['tytul_szkolenia'],d['termin'],d['miasto'])



# import requests
# response=requests.get('https://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     for d in [e for e in response.json() if "Python".lower() in e['tytul_szkolenia'].lower()]:
#          print(d['tytul_szkolenia'],d['termin'],d['miasto'])

#psycopg2
#cx_Oracle

import psycopg2
connection=psycopg2.connect(host="13.74.139.54",database="postgres",user="postgres",password="szkolenie_jsystems_2021")
#
# select current_timestamp;
#
#
# create table players_andrew(
# 	player_id serial primary key,
# 	first_name text not null,
# 	last_name text not null,
# 	height numeric not null,
# 	weight numeric not null
# );
#
# insert into players_andrew(first_name,last_name,height,weight)
# values ('Andrzej','Klusiewicz',1.76,80);
#
# insert into players_andrew(first_name,last_name,height,weight)
# values ('Chuck','Norris',1.82,78);
#
# insert into players_andrew(first_name,last_name,height,weight)
# values ('Krzysztof','Jarzyna',1.68,70);
#
# select * from players_andrew;
#
# create table cars_andrew(
# 	car_id serial primary key,
# 	brand text not null,
# 	model text not null,
# 	plates text not null,
# 	capacity numeric not null
# );
#
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Renault','Kadjar','WY 12345',1.6);
#
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Czarny','Ciągnik','WY 666',2.4);
#
#
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Czołg','7TP','UA 12345',5.6);
#
#
# select * from cars_andrew;
#
#
# begin work; --begin
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Renault','Kadjar','WY 12345',1.6);
#
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Czarny','Ciągnik','WY 666',2.4);
#
#
# insert into cars_andrew(brand,model,plates,capacity)
# values ('Czołg','7TP','UA 12345',5.6);
# commit;--rollback;
#
# do
# $$
# begin
# raise notice 'whatever';
# end $$;


# import psycopg2
# connection=psycopg2.connect(host="13.74.139.54",port=5432,database="postgres",user="postgres",password="szkolenie_jsystems_2021")


# import psycopg2
# connection=psycopg2.connect(host="localhost",port=5432,database="postgres",user="postgres",password="oracle")
