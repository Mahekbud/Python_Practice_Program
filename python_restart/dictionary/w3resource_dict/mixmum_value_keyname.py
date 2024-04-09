dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}


Key_max = max(zip(dict.values(), dict.keys()))[1] 
Key_min = min(zip(dict.values(), dict.keys()))[1]  

print("max : ", Key_max)
print("min :",Key_min)