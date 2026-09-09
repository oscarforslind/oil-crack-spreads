GALLONS_PER_BARREL = 42
crude = [78.50, 79.10, 77.80, 80.20] #$/barrel
gasoline = [2.35, 2.41, 2.28, 2.44] #$/gallon
distillate = [2.52, 2.58, 2.49, 2.61] #$/gallon

gasoline_barrel = []
for price in gasoline:
    gasoline_barrel.append(price*GALLONS_PER_BARREL)

distillate_barrel = []
for price in distillate:
    distillate_barrel.append(price*GALLONS_PER_BARREL)

crack_321 = []
for i in range(len(crude)):
    crack = (gasoline_barrel[i]*2+distillate_barrel[i])/3-crude[i]
    crack_321.append(crack)
for i in range(len(crack_321)):
    print(f"Day {i+1}: $ {crack_321[i]:.2f}")

print(f"Average: $ {sum(crack_321) / len(crack_321):.2f}")