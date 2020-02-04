from zoo_goods import zoo_goods, zoo_animals, zoo_items

zoo_market=zoo_goods("Шиншилка")
zoo_market.display_info()

animal=zoo_animals("Кошка")
animal.breed("Шотландская")

item_for_care=zoo_items("Миска")
item_for_care.amount("1")

item_for_care=zoo_items("Корм")
item_for_care.amount("3")

item_for_care=zoo_items("Туалет")
item_for_care.amount("1")

animal=zoo_animals("Кошка")
animal.breed("Британская")

item_for_care=zoo_items("Миска")
item_for_care.amount("1")

item_for_care=zoo_items("Корм")
item_for_care.amount("4")

item_for_care=zoo_items("Туалет")
item_for_care.amount("1")
