data = [
    {"id": "111", "name": "laptop", "cost": 50000, "rating": 2, "discount": 40, "category": "Electronics", "brand": "Asus"},
    {"id": "222", "name": "laptop", "cost": 69999, "rating": 4, "discount": 30, "category": "Electronics", "brand": "Acer"},
    {"id": "333", "name": "laptop", "cost": 79999, "rating": 5, "discount": 10, "category": "Electronics", "brand": "Acer"},
    {"id": "444", "name": "phone", "cost": 32999, "rating": 2, "discount": 60, "category": "Electronics", "brand": "Asus"},
    {"id": "555", "name": "phone", "cost": 35999, "rating": 4, "discount": 20, "category": "Electronics", "brand": "Acer"},
    {"id": "666", "name": "shirt", "cost": 1999, "rating": 3.4, "discount": 30, "category": "Lifestyle", "brand": "Polo"},
    {"id": "777", "name": "shirt", "cost": 1599, "rating": 4, "discount": 20, "category": "Lifestyle", "brand": "Raymond"},
    {"id": "888", "name": "pant", "cost": 2999, "rating": 4, "discount": 20, "category": "Lifestyle", "brand": "Polo"},
    {"id": "999", "name": "pant", "cost": 2599, "rating": 3, "discount": 30, "category": "Lifestyle", "brand": "Raymond"}
]


class Product:

    def __init__(self, id , name, cost, rating, discount, category, brand):
        self.id = id
        self.name = name
        self.cost = cost
        self.rating = rating
        self.discount = discount
        self.category = category
        self.brand = brand

    def showproduct(self):
        print(self.id, " ", self.name, " ", self.cost, " ", self.rating, "", self.discount)

liobj = []
for dd in data:
    liobj.append(Product(**dd))

fields = {1: ["cost", False], 2: ["cost", True], 3: ["rating", True], 4: ["discount", False], 5: ["discount", True]}
inp = -1
while inp != 0:
    print("Press 1. to sort by cost Low to High")
    print("Press 2. to sort by cost High to Low")
    print("Press 3. to sort Rating")
    print("Press 4. to sort by Discount Low to High")
    print("Press 5. to sort by Discount High to Low")
    print("Press 0 to exit")
    inp = int(input("Enter your option "))
    if inp != 0:
        liobj.sort(key=lambda ele: ele.__getattribute__(fields[inp][0]), reverse=fields[inp][1])
        for li in liobj:
            li.showproduct()
