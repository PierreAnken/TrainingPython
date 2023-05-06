# 5 Autos
# 2 Garagen
# Garagen müssen wissen welche Autos sie haben

auto1 = ["Audi", 11]
auto2 = ["BMW", 12]
auto3 = ["Mercedes", 13]
auto4 = ["Lambo", 14]
auto5 = ["Ferrari", 25000]

garage_1 = [auto1, auto2, auto3]
garage_2 = [auto4, auto5]


# Function übernimmt den Paramater Garage und printet alle Autos

def print_garage(some_garage):
    for auto in some_garage:
        print(f'{auto[0]} hat {auto[1]} Kilometer')

for auto in garage_1:
    auto[1] += 10000

print_garage(garage_1)
print_garage(garage_2)
