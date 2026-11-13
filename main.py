import diagram 
from data import create_data 

data_list = create_data() 

print("Hur många värden som finns i res:", len(data_list)) 
print("Första tio värdenrna:", data_list[:10])

diagram.show_histogram(data_list) 