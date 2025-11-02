# with open ('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

import pandas
data = pandas.read_csv('weather_data.csv')
# data["temp"] = data["temp"] * 9/5 + 32
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# #average_temp = sum(temp_list) / len(temp_list)
# #print(f"The average is {average_temp}")

# print(f"The average is {data['temp'].mean()}")
# print(f"The max is {data['temp'].max()}")

# #Get data in columns
# print(data.condition)
# print(data["condition"])

# #Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)

print(monday.temp[0] * 9/5 + 32)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}   
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)
