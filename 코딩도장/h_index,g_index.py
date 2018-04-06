quotations = [0, 15, 4, 0, 7, 10, 0]

# h-index
for h in range(min(max(quotations), len(quotations)), 0, -1):
    count = 0
    for number in quotations:
        if number >= h:
            count += 1
    if count == h:
        print("h-index =", h)
        break

# g-index
quotations.sort(reverse=True)
for g in range(len(quotations), 0, - 1):
    if sum(quotations[0:g]) >= g**2:
        print("g-index =", g)
        break