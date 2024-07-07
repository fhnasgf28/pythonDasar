clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"washing {item}")
paired_socks.append("socks")
print(f"washing {paired_socks}")