#for num_table in range(1, 10):
 #   for mul_factor in range(1, 10):
  #      result = num_table * mul_factor
   #     print(f"{num_table} * {mul_factor} = {result}")
        
shopping = ['Agua','Huevos', 'Aceite', 'Sal', 'Limon']
print(list(shopping))
print(list(reversed(shopping)))
print(shopping.reverse())

even_number = []
for i in range(20):
    if i % 2 == 0:
        print(even_number.append(i))
        print(even_number)
print(even_number)

word ='python'
if len(word) > 4 and word.startswith('p') and word.count('y') >= 1:
    print('Cool word!')