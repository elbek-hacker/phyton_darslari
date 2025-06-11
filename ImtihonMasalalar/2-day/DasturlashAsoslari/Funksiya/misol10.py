def uchta_yigindi_nol(lst):
    n = len(lst)
    triplet = []
    used_indices = set()

    # Uchlikni topish
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if lst[i] + lst[j] + lst[k] == 0:
                    triplet = [lst[i], lst[j], lst[k]]
                    used_indices = {i, j, k}
                    break
            if triplet:
                break
        if triplet:
            break

    if not triplet:
        return [[], lst]  # Agar topilmasa

    # Qolgan elementlarni yig'ish
    remaining = [lst[i] for i in range(n) if i not in used_indices]
    return [triplet, remaining]
