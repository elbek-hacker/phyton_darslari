royxat = [1, 2, 3]

while True:
    try:
        index = int(input("index kiriting: "))
        print(royxat[index])
        break
    except IndexError:
        print(f"index noto'g'ri kiritildi. 0 va {len(royxat) - 1} oraligida son kiriting!")
    except ValueError:
        print("Xato. Son kiriting.")