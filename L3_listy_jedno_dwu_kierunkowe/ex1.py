import random


office = []
counter_types = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'E']

for num in range(1, 11):
    type = random.choice(counter_types)
    queue_time = random.randint(1, 31)
    counter = f'{num}:{type}:{queue_time}'
    counter_types.remove(type)
    office.append(counter)

print(office)

queue = []
client_types = ['A', 'B', 'C']

for client_no in range(1, 31):
    client_type = random.choice(client_types)
    task_complexity = random.randint(1, 11)
    client = f'{client_no}:{client_type}:{task_complexity}'
    queue.append(client)

print(queue)

