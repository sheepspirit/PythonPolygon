from ast import While
import string
import time
maxPercentLearnability = 100 # Максимальный процент прироста базовой характеристики "Обучаемость"
minPercentLearnability = 10 # Минимальный процент прироста базовой характеристики "Обучаемость"
maxPercentProfitability = 150 # Максимальный процент прироста базовой характеристики "Доходность"
minPercentProfitability = 70 #минимальный процент прироста базовой характеристики "Доходность"
ageOfDeath = 100 #год смерти игрока
ageOfMaxSalary = 45
ageOfCareerStart = 18
minYearsTillDeath = 20 #минимальный срок до наступления смерти. используется при расчётах во время регистрации игрока
print("\033[H\033[J", end="")
print("Привет! Это симулятор тестировщика.")

print("Как тебя зовут?")
userName = str(input())
print(f"Приятно познакомиться, {userName}!\nТеперь скажи, сколько тебе лет. От возраста будет зависеть твоя способность к обучению и ставка. Введи возраст в диапазоне с {ageOfCareerStart} по {ageOfDeath-minYearsTillDeath}:)")
userAge = 0

while userAge < ageOfCareerStart or userAge > ageOfDeath-minYearsTillDeath:
    userAge = int(input())
    print(f"Тут у нас игра для взрослых в пределах  {ageOfCareerStart} - {ageOfDeath-minYearsTillDeath} лет. \nТак сколько тебе?")

print("\033[H\033[J", end="")
i = 0
j = 1
while i < 20:
    print("Генерируем характеристики:"+" "*j+"."*j)
    time.sleep(0.01)
    print("\033[H\033[J", end="")
    i = i + 1
    if j >= 10:
        j = 1
    else:
        j = j + 1

print(f"Имя: {userName}")
print(f"Возраст: {userAge}")
learnability = round((((minPercentLearnability/maxPercentLearnability)**(1/(100-18)))**(userAge-18))*maxPercentLearnability)
print(f"Обучаемость: {learnability}%")
if userAge <= 45:
    profitability = round((((maxPercentProfitability/minPercentProfitability)**(1/(ageOfMaxSalary-18)))**(userAge-18))*minPercentProfitability)
else:
    profitability = round((((minPercentProfitability/maxPercentProfitability)**(1/(ageOfDeath-ageOfMaxSalary+1)))**(userAge-18))*maxPercentProfitability)
print(f"Доходность: {profitability}%")