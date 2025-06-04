while True:
    son = input("Son kiriting: ")
    try:
        son = int(son)
        print("Rahmat")
        break
    except ValueError:
        print("Xato. Son kiritishingiz kerak!")
