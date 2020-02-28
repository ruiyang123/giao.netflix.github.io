import csv
import operator
import json

def load_data_country(csv_file_name):

	with open (csv_file_name + ".csv", "r", encoding="utf8", newline="") as csv_file:
		first_line = True
		reader = csv.DictReader(csv_file, delimiter=",")
		countries = build_json_object_country(csv_file_name)
		for row in reader:
			if not first_line:
				row["country"] = row["country"].strip() 
				if row["country"] == '':
					continue 
				list_countries = row["country"].split(",")
				for val in list_countries:
					val = val.strip()
					row["release_year"] = row["release_year"].strip()
					is_exist = False        			
					for i in range(0, len(countries[val])):
						if countries[val][i]["date"] == row["release_year"]:
							is_exist = True
							break					         			        			 
					if is_exist: 
						row["type"] = row["type"].strip()
						if row["type"] == "Movie":
							countries[val][i]["movie"] += 1
						else:
							countries[val][i]["tv"] += 1
					else:
						if row["type"] == "Movie":
							new_element = {
											"date" : row["release_year"],
											"movie" : 1,
											"tv" : 0
											}
						else:
							new_element = {
											"date" : row["release_year"],
											"movie" : 0,
											"tv" : 1
											}
						countries[val].append(new_element)	

			else:
				first_line = False

		print(countries["Serbia"])
	with open("data_date_country.json", "w") as json_file:
		json.dump(countries, json_file)        


def build_json_object_country(csv_file_name):
	with open (csv_file_name + ".csv", "r", encoding="utf8", newline="") as csv_file:
		first_line = True
		reader = csv.DictReader(csv_file, delimiter=",")
		countries = {}
		cmp = 0
		for row in reader:
			if not first_line:
				if row["country"] == '':
					continue 
				list_countries = row["country"].split(",")
				cmp += len(list_countries)
				for val in list_countries:
					val = val.strip()
					countries[val] = []	
			else:
				first_line = False
	print(cmp)
	print(len(countries))
	return countries		
   	
def load_data_all(csv_file_name):

	with open (csv_file_name + ".csv", "r", encoding="utf8", newline="") as csv_file:
		first_line = True
		reader = csv.DictReader(csv_file, delimiter=",")
		countries = {"dates" : []}
		for row in reader:
			if not first_line:
				row["release_year"] = row["release_year"].strip()        			
				row["type"] = row["type"].strip()
				is_exist = False
				for i in range(0, len(countries["dates"])):
					if countries["dates"][i]["date"] == row["release_year"]:
						is_exist = True
						break					
				if is_exist:
					if row["type"] == "Movie":
						countries["dates"][i]["movie"] += 1
					else:
						countries["dates"][i]["tv"] += 1
				else:
					if row["type"] == "Movie":
						new_element = {	"date" : row["release_year"],
										"movie" : 1,
										"tv" : 0
										}	
					else:
						new_element = {	"date" : int(row["release_year"]),
										"movie" : 0,
										"tv" : 1
										}
					countries["dates"].append(new_element)																			
			else:
				first_line = False

		print(countries["dates"])
	with open("data_date_all.json", "w") as json_file:
		json.dump(countries, json_file)    

load_data_country("netflix_titles") 
load_data_all("netflix_titles")
