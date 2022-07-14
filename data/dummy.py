from faker import Faker
import pandas as pd
import random



dummy_data = Faker(['id_ID'])
rating = 'ABCDEF'
user_database = []

for i in range(100):
    id = str(i + 1)
    name = dummy_data.name()
    address = dummy_data.address()
    rate = random.choice(rating)
    text = dummy_data.text()
    
    user_database.append({
        'ID': id,
        'Name' : name,
        'Address': address,
        'Rating': rate,
        'Review': text
    })
    # user_database.append(user_data)

df = pd.DataFrame(user_database)
df.to_csv('user_review.csv')
print('Ready to Use')