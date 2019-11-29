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

i = -1
while i != 0:
    print("Press 1. to filter by category")
    print("Press 2. to filter by brand")
    print("Press 3. to filter by name")
    print("Press 0 to exit")
    i = int(input("Enter your option : "))
    f = input("Enter the filter name : ")
    if i == 1:
        newd = filter(lambda ele: ele["category"] == f, data)
        for d in newd:
            print(d)
    elif i == 2:
        newd = filter(lambda ele: ele["brand"] == f, data)
        for d in newd:
            print(d)
    elif i == 3:
        newd = filter(lambda ele: ele["brand"] == f, data)
        for d in newd:
            print(d)
    else:
        break
