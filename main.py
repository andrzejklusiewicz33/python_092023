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
