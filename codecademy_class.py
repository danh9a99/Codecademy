brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items ={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items ={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "{a} is avalable from {b} to {c}".format(a = self.name, b = self.start_time, c = self.end_time)
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def ___repr__(self):
    return "The address is {a}".format(a = self.address)
  def available_menus(self, time):
    mm = [menu for menu in self.menus if time >= menu.start_time and time <=menu.end_time]
    return mm

  

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises  
 
  
brunch = Menu("brunch", brunch_items, 11, 16)
early_bird = Menu("early_bird", early_bird_items, 15, 18)
dinner = Menu("dinner", dinner_items, 17, 23)
kids = Menu("kids", kids_items, 11, 21)



flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", Menu('arepas_menu', arepas_menu, 10, 20))


business_a = Business("Basta Fazoolin", [flagship_store, new_installment])
business_b = Business("Take a' Arepa", arepas_place)

brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird_bill = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

print(flagship_store.available_menus(17))
print(brunch_bill)
print(early_bird_bill)
print(brunch)


