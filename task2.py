# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(x, y, z)
            left = not(x or y or z)
            right = (not x) and (not y) and (not z)
            result = left == right
            print(result)
