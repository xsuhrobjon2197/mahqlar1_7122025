#1-misol
i = int(input("Haroratni kiriting!: "))

if i > 30:
    print("Juda ham issiq Iltimos uyda qoling!")
elif 20 < i < 30:
    print("Havo yahshi sayr qiling!")
elif 10 < i < 20:
    print("Havo salqin, Ko'ylak kiying!")
if i < 0:
    print("Juda sovuq extiyot bo'ling!")

#2-misol
i = input("Ovqat turini kiriting: ")

if i == "Pizza":
    print("50-ming so'm")
elif i == "burger":
    print("30-ming so'm")
elif i == "salad":
    print("20-ming so'm")
else:
    print("bizda unday narsa yo'q")

#3-misol
i = int(input("Yoshingizni kiriting: "))

if i < 18:
    print("Sizga 50% chegirma mavjud")
elif 18 < i < 60:
    print("Chegirma yo'q to'liq narxi: 100-ming so'm")
elif i > 60:
    print("Keksalarga 30% foiz chegirma bor!")
