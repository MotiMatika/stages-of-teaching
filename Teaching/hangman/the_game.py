#פתיחת קובץ לקריאה ולכתיבה

# with open("nisayon.txt","w")   as file:    # פתיחת קובץ חדש לכתיבה.אפשר לראות שהוא נוצר בשוליים השמאליים 
#     file.write("abcd\nefgh\nijkl\nmnop\nqrst\nuvw\nxyzbb")          #כתיבת תוכן
# with open("nisayon.txt","r")   as file:       #יציאה מהבלוק של הפתיחה. ואז פתיחת הקובץ לקריאה
#     print(file.read())


# with open("nisayon.txt","w")   as file:    # פתיחת קובץ חדש לכתיבה.אפשר לראות שהוא נוצר בשוליים השמאליים 
#     file.write("abcdefghijklmnopqrstuvwxyzbb")          #כתיבת תוכן
# with open("nisayon.txt","r")   as file:       #יציאה מהבלוק של הפתיחה. ואז פתיחת הקובץ לקריאה
#     x=file.read()
#     print(x)
#     all_parts=x.split(" ")


# with open("nisayon.txt","w")   as file:    # פתיחת קובץ חדש לכתיבה.אפשר לראות שהוא נוצר בשוליים השמאליים 
#     file.write("ab,cde,fghijkl,mnopqrstuvwxyzbb")          #כתיבת תוכן
# with open("nisayon.txt","r")   as file:       #יציאה מהבלוק של הפתיחה. ואז פתיחת הקובץ לקריאה
#     x=file.read()
#     comma=","
#     all_parts=x.split(",")      #פיצול רצף ע"י פסיק.הפיצול יוצר רשימה של איברים
#     print(all_parts[1])         #ניתן לקרוא לכל איבר ברשימה שנוצרה
   

# with open("Teaching\hm\painting","r")   as file:       #יציאה מהבלוק של הפתיחה. ואז פתיחת הקובץ לקריאה
#     x=file.read()
#     print(x)
    # comma=","
    # all_parts=x.split(",")      #פיצול רצף ע"י פסיק.הפיצול יוצר רשימה של איברים
    # print(all_parts[0])     



# new_dict={"copy": "cntr+c","paste": "cntr+v"}   #יצירת מילון עם מפתח וערך

# print((new_dict["paste"]))                      # הדפסת הערך כשהמפתח נתון   קריאה למפתח תיתן את ערכו

# print("to know what is paste :",(new_dict["paste"])) 
# new_dict["cut"]="cntr+x"                        #הוספה של מפתח+ערך
# print((new_dict))                               #הדפסת המילון



HANGMAN_PHOTOS = {
    "1": """
    x-------x
    """,
    "2": """
    x-------x
    |
    |
    |
    |
    |
    """,
    "3": """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    "4": """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    "5": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
    """,
    "6": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
    """,
    "7": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \\
    |
    """
}




word="window"
all_letters=[]
i=1
while i<=30:
    letter=input("guess a letter   ")
    if letter not in word:
        print(HANGMAN_PHOTOS[str(i)])
        i+=1
    else:
        all_letters.append(letter)
        print(all_letters)






















# with open("myfile.txt","w") as f:

#     f.write("my first line\n")

# with open("myfile.txt", "a") as f:

#     f.write("my second line\t")

#     f.write("tab in second")

# with open("myfile.txt","r") as f:

#     for line in f:

#         print(line)


# comma=","
# with open("Teaching\hm\painting","r") as paint:

    
#     for row in paint:
#         pic=row.split(comma)

#         print(pic)













# print("\n\n")
# p=open("Teaching\ext.txt","r")
# print(p.mode)           #תצורה של הקובץ:קריאה,כתיבה
# print(p.name)           #מיקום הקובץ
# print(p.closed)         #מצב הקובץ:פתוח או סגור
# print(p.read())         #קריאת כל הקובץ
# print(p.read(2))        #קריאת 2 אותיות בלבד
# print(p.readline())
# p.close()
# print(p.closed)    