# test_lesson-32.py

import module  
result_add = module.add(10, 5)
result_subtract = module.subtract(10, 5)

print("Addition result:", result_add)
print("Subtraction result:", result_subtract)

calc = module.Calculator()
print("Initial value:", calc.get_value())

calc.add(15)
print("After adding 15:", calc.get_value())

calc.subtract(5)
print("After subtracting 5:", calc.get_value())
