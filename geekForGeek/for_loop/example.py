clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"washing {item}")
paired_socks.append("socks")
print(f"washing {paired_socks}")

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(distance)
    print(f"Day {day}: Run {distance: .1f} Miles")