import math
for radio in range(10, 110, 10):
    longitud = 2*math.pi*radio
    area = math.pi*radio*radio
    print(radio, longitud, area)