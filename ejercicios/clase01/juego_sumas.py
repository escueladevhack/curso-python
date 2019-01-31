from datetime import datetime
from random import randint, choice
from operator import add, sub, mul

start_date = datetime.utcnow()
hits = 0

for _ in range(10):
    operator1 = randint(0, 10)
    operator2 = randint(0, 10)
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
    }
    current_operation = choice(list(operations.keys()))
    user_result = input("{} {} {} = ".format(operator1, current_operation, operator2))
    if operations[current_operation](operator1, operator2)== int(user_result):
        hits += 1
end_date = datetime.utcnow()
print("===========")
print("==={}/10===".format(hits))
print("{}".format(end_date-start_date))