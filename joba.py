from random import shuffle
from sys import exit

Game_Name="Жасырылған сөз"
Anon_Name="Anone_name"
Alphabet="аәбвгғдеёжзийкқлмнңоөпрстуүұфхһцчшщъьыіэюя"
FILENAME='test.txt.txt'
Min_Lenght=5
BS="\\"

want_to_play=True
hit=0
miss=0

x=(39-len(Game_Name))//2
y=1 if len(Game_Name)%2==0 else 0

print("*"*40+"*")
print("*" + " "*39+"*")
print("*" + " " * x + Game_Name.upper() + " " * (x+y) + "*")
print("*" * 40 + "*")
print()

print(f" \"{Game_Name}\" Ойынына қош келдіңіз!\n")

name=input("Есімің кім ?")
if not name:
    name="ANON_NAME"

print(f"\n{name}, ойын ережесімен таныс болыңыз!")
print("Мен сөз жасырамын және оның құрамында неше әріп бар екенін көрсетемін")
print("әрбір әріпті бір реттен аитып шығасыз .Егер әріп табылса онда, иә ")
print("саған оны көрсететін боламын.Сіз ойында 7 рет қателесе аласыз.")

words=[]
file=open("test.txt.txt", encoding="utf-8")
for line in file:
    line=line.lower().strip()
    if len(line) >= Min_Lenght:
        kazakh_word=True
        for letter in line:
            if letter not in Alphabet:
                kazakh_word=False
        if kazakh_word:
            words.append(line)  #тексерілген әріпті тізім соңына қосу
file.close()

if len(words)==0:
    print("файлда ешқандай әріп жоқ!")
    input("программа аяқталуы үшін ENTER сөзін басыңыз")
    exit()

shuffle(words)

while want_to_play:
    if len(words) == 0:
        print("\n Өкінішке орай, мендегі сөздер аяқталды!")
        want_to_play = False
    else:
        word = words.pop()
        current_word = "-" * len(word)
        print()
        print(f"{name}, мен {len(word)} әріптен тұратын сөз жасырдым")
        mistakes = 0
        letters = ""

        while not (word == current_word or mistakes > 6):
            print()
            print(f"----------")
            print(f"|/       {'|' if mistakes > 0 else ' '}")
            print(f"|        {'o' if mistakes > 1 else ' '}")
            print(f"|       {'/' if mistakes > 2 else ' '}{'|' if mistakes > 3 else ' '}{BS if mistakes > 4 else ' '}")
            print(f"|       {'/' if mistakes > 5 else ' '} {BS if mistakes > 6 else ' '}")
            print(f"|\\")
            print(f"|_\_")
            print()
            print(f"Слово:{current_word}")
            print(f"Қателіктер:{mistakes} 7 ден")
            print(f"Әріп атауы:", end="")

            if len(letters) == 0:
                print("-")
            else:
                print(*letters)

            letter = input("Әріп енгіз").lower()
            while not (len(letter) == 1 and letter in Alphabet):
                letter = input("Қазақша 1 әріп енгіз").lower()

            letter_in_word = False
            for i in range(len(word)):
                if letter == word[i]:
                    current_word = current_word[:i] + letter + current_word[i + 1:]
                    letter_in_word = True
            if not letter_in_word:
                mistakes += 1
            if not letter in letters:
                letters += letter

        print()
        print(f"Сөз {current_word}")
        print(f"7 ден кеткен қателік {mistakes}")
        print(f"Айтылғвн әріптер ", end="")

        if len(letters) == 0:
            print("-")
        else:
            print(*letters)

        print()
        if word == current_word:
            print(f"{name}, Құттықтаймын! Сіз сөзді таптыңыз!")
            hit += 1
        else:
            print(f"{name}, өкінішке орай сіз сөзді таба алмадыңыз...")
            miss += 1
        print(f"Дұрыс сөз: \"{word}\".")

        print()
        again = input("Тағы ойнағыңыз келема? (иа/жоқ)").lower()
        while not (again == "иа" or again == "жоқ"):
            again = input("Жай ғана таңда \"иа\" немесе \"жоқ\":").lower()
        if again == "жоқ":
            want_to_play = False

    print()
    print(f"{name}, ойын үшін рахмет! Келесі жолда сенің нәтижелерің")
    print(f" Табылған сөз саны: {hit}, қате кеткен сөздер саны: {miss}")
    print("Келесі кездескенше")
    print()
    input("Ойыннан шығу үшін ENTER бас")