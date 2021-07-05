year = 0
count = 10000
while True:
    year += 1
    count *= 1.0325
    print(year,count)
    if count >= 20000:
        print(f"10000元连本带息{year}年能翻倍......")
        break
