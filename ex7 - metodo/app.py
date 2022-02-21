def soma(*num):
    s=0
    for i in num:
        s+= i
    print(f"somando valores {num} temos {s}")


soma(5, 6)
soma(8, 9, 2, 7)
soma(100, 999)