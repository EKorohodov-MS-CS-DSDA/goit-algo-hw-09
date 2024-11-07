# Виконання домашнього завдання
Згідно з умовою домашнього завдання, імплементовано дві функції: 
  1. find_coins_greedy - імплементація жадібного алгоритму
  2. find_min_coins - імплементація алгоритму методом динамічного

## Виконання
***find_coins_greedy*** ітеративно для кожної монети починаючи з найбільшої перебирає задане параметром значення і визначає скільки разів можна поділити це значення без остачі, 
що і є кількістю необхідних монет номіналу поточної ітерації. Далі значення заміняється на остачу від вищезгадонаго ділення і починається наступна ітерація.


***find_min_coins*** - для імплементації обрано верхній підхід з мемоізацією. Функція викликає вкладену функцію ***find_min_coins_impl*** , що є рекурсивною. 
На кожному рівні виклику відбувається перевірка базових випадків і наявність значення в словнику збережених значень.

## Тести і результати тестів
Для кожної з імплементації відбувались запуски для 10 значень в діапазоні між 100 та 100000. Для кожного зі значень відбувалось по 1000 запусків.

### Результати тестів

Нижче наводжу результати для декількох з тестів, котрі не мають занадто близькі вхідні значення:

|Test Function |Test value|Coins needed|Test Time (sec.) x10000|
|:---:|:---:|:---:|:---:|
|find_coins_greedy|547|{50: 10, 25: 1, 10: 2, 2: 1}|0.005591|
|find_min_coins|547|{50: 10, 2: 1, 10: 2, 25: 1}|0.003506|
|find_coins_greedy|11686|{50: 233, 25: 1, 10: 1, 1: 1}|0.005851|
|find_min_coins|11686|{50: 233, 1: 1, 10: 1, 25: 1}|0.003338|
|find_coins_greedy|22529|{50: 450, 25: 1, 2: 2}|0.006134|
|find_min_coins|22529|{50: 450, 2: 2, 25: 1}|0.003274|
|find_coins_greedy|54663|{50: 1093, 10: 1, 2: 1, 1: 1}|0.005786|
|find_min_coins|54663|{50: 1093, 1: 1, 2: 1, 10: 1}|0.003788|
|find_coins_greedy|74766|{50: 1495, 10: 1, 5: 1, 1: 1}|0.006843|
|find_min_coins|74766|{50: 1495, 1: 1, 5: 1, 10: 1}|0.004131|
|find_coins_greedy|98510|{50: 1970, 10: 1}|0.006851|
|find_min_coins|98510|{50: 1970, 10: 1}|0.003916|

## Висновки
У обох алгоритмів часова складність O(n * m), де n - вхідне значення, а m - кількість монет. У динамічного верхнього підходу просторова складність O(n), оскільки є необхідність зберігати закешовані значення.
Виходячи з результатів тестів можемо зробити висновок, що динамічний верхній підхід впорався із задачею швидше, але має обмеження. А саме, як зазначалось, він вимагає більше пам'яті, а також він обмежений 
глибиною розгортання рекурсивних викликів. Тому можемо сказати, що великі суми менше впливають на ефективність динамічного верхнього підходу, 
і він є ефективнішим за жадібний алгоритм, але він має межу визначену глибиною рекурсивних викликів та розміром стеку. Тож для дійсно великих значень (вище за 100000), ефективнішим, 
все ж, вийшов би жадібний алгоритм, через меншу кількість обмежень. 

### Примітки
Насправді, я не зовсім зрозумів, чому вийшло обробити значення вище 50000, оскільки без зміни лімітів рекурсивних викликів (**sys.setrecursionlimit**), 
ще на значенні 50000 мав би отримати **RecursionError: maximum recursion depth exceeded**. Буду вдячний за підказку в коментарях до завдання.