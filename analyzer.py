import os
import pandas as pd
from requests import options

print(*[filename.split('.')[0] for filename in os.listdir('./opinions')], sep='\n')
product = input("podaj id produktu: ")

opinions = pd.read_json('opinions/'+product+'.json', 'w', encoding='UTF-8')
print(opinions)