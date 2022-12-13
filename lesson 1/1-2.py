#Напишите программу для проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#для всех значений предикат

values = [True, False]
for x in values:
    for y in values:
        for z in values:
            if (not (x or y or z)) != (not (x) and not (y) and not (z)):
                print('Утверждение ложь!')
            else:
                print('Утверждение истинно!')


