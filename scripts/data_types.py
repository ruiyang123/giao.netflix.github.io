import csv
import operator
import json

def load_data(json_file_name):
	with open(json_file_name + ".json") as json_data:
		data = json.load(json_data)
	total = 0  	
	var = 0.5
	for i in range(0, len(data)):
		total += data[i]["value"]

	print(total)	
	new_element = {
					"name" : "others",
					"value": 0	
				}	
	new_data = []	
	for i in range(0, len(data)):
		per = (data[i]["value"] * 100) // total
		
		if per <= var:
			new_element["value"] += data[i]["value"]
		else:
			if data[i]["name"].find("TV") == -1:	 	
				new_data.append(data[i])

	
	#if new_element["value"] != 0:
		#new_data.append(new_element)			
			
	with open("new_data_type.json", "w") as json_file:
		json.dump(new_data, json_file)

	print(len(data))
	print(len(new_data))
	print(new_data)

def load_data_country(json_file_name):
	with open(json_file_name + ".json") as json_data:
		data = json.load(json_data)
	
	new_data = []
	
	for i in range(0, len(data)):
		new_country = {
						"country" : data[i]["country"],
						"value" : []	
					}

		nb_types = len(data[i]["value"])
		
		if nb_types > 15:
			new_element = filter_country_type_nb(data[i]["value"])
			if new_element:
				new_country["value"] = new_element 				
		else:
			new_element = filter_country_type_format(data[i]["value"])			
			if new_element:
				new_country["value"] = new_element

		new_data.append(new_country)

	print(new_data)		
	with open("new_data_type_country.json", "w") as json_file:
		json.dump(new_data, json_file)		
			

def filter_country_type_nb(values):
	new_values = []
	total = 0  	
	var = 0.5
	for i in range(0, len(values)):
		total += values[i]["value"]
	for i in range(0, len(values)):
		per = (values[i]["value"] * 100) // total
		if per > var:
			if values[i]["name"].find("TV") == -1 and values[i]["name"] != "International Movies":	 	
				new_values.append(values[i])
	return new_values			

def filter_country_type_format(values):
	new_values = []
	one_element = False
	if len(values) <= 2:
		one_element = True
	for i in range(0, len(values)):
		if one_element:
			new_values.append(values[i])
		else:
			if values[i]["name"].find("TV") == -1 and values[i]["name"] != "International Movies":	 	
				new_values.append(values[i])		
	return new_values


#load_data("data_type")	
load_data_country("data_type_country")

