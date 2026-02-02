# 24. Oziq-ovqat xarajatlari

class Grocery:
    def __init__(self, item_type, cost):
        self.item_type = item_type    # "Go‘sht", "Sut", "Sabzavot" va h.k.
        self.cost = cost              # narx ($)

    def get_cost(self):
        """Mahsulotning narxi"""
        return self.cost

    def __str__(self):
        return f"{self.item_type:14} | {self.cost:6.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class Meat(Grocery):
    def __str__(self):
        return f"🥩 {self.item_type:12} → {self.cost:6.2f}$"


class Dairy(Grocery):
    def __str__(self):
        return f"🥛 {self.item_type:12} → {self.cost:6.2f}$"


# Qo‘shimcha kategoriyalar (foydali bo‘lishi mumkin)
class Vegetable(Grocery):
    def __str__(self):
        return f"🥕 {self.item_type:12} → {self.cost:6.2f}$"


class Fruit(Grocery):
    def __str__(self):
        return f"🍎 {self.item_type:12} → {self.cost:6.2f}$"


# --------------------------------------------------
# Haftalik xarajatlar ro‘yxatini chiqarish
# --------------------------------------------------

def show_grocery_expenses(items):
    print("\n" + "═" * 55)
    print("   HAFTALIK OZIq-OVQAT XARAJATLARI   ".center(55))
    print("═" * 55)
    print("Mahsulot turi          Narxi ($)")
    print("─" * 55)

    total = 0

    for item in items:
        print(item)
        total += item.get_cost()

    print("─" * 55)
    print(f"Jami xarajat:                       {total:8.2f}$")
    print("═" * 55 + "\n")


# Test ma'lumotlari (haftalik xarid misoli)
xarajatlar = [
    Meat("Mol go‘shti", 18.50),
    Meat("Tovuq filesi", 9.80),
    Dairy("Sut 2L", 3.20),
    Dairy("Qatiq", 2.10),
    Vegetable("Pomidor", 4.50),
    Fruit("Olma", 5.00),
    Meat("Qo‘y go‘shti", 22.00),
    Dairy("Pishloq", 7.90),
]

show_grocery_expenses(xarajatlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol xarajatlaringiz:\n")
misol_xarajatlar = [
    Meat("Go‘sht", 15),
    Dairy("Sut", 3),
]

show_grocery_expenses(misol_xarajatlar)
