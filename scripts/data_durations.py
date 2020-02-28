import csv
import operator
import json

def load_data_all(csv_file_name):

	with open (csv_file_name + ".csv", "r", encoding="utf8", newline="") as csv_file:
		first_line = True
		reader = csv.DictReader(csv_file, delimiter=",")
		durations = {"durations" : []}
		for row in reader:
			if not first_line: 
				if row["type"] == "":
					continue
				if row["type"] == "Movie":
					if row["duration"] == "":
						continue
					duration_object = row["duration"].split()
					duration = int(duration_object[0])
					if duration >= 10:
						nb = (duration // 10) * 10
						is_exist = False
						for i in range(0, len(durations["durations"])):
							if durations["durations"][i]["duration"] == nb:
								is_exist = True
								break
						if is_exist:
							durations["durations"][i]["value"] += 1
						else:
							new_element = {	
											"duration" : nb,
											"value" : 1
										}
							durations["durations"].append(new_element)				
			else:
				first_line = False

	print(durations["durations"])
	with open("data_duration_all.json", "w") as json_file:
		json.dump(durations, json_file)			

def load_data_country(csv_file_name):

	with open (csv_file_name + ".csv", "r", encoding="utf8", newline="") as csv_file:
		first_line = True
		reader = csv.DictReader(csv_file, delimiter=",")
		durations = build_json_object_country(csv_file_name)
		for row in reader:
			if not first_line:
				row["country"] = row["country"].strip() 
				if row["country"] == '':
					continue 
				list_countries = row["country"].split(",")
				for val in list_countries:
					val = val.strip()
					if row["type"] == "":
						continue
					if row["type"] == "Movie":
						if row["duration"] == "":
							continue
						duration_object = row["duration"].split()
						duration = int(duration_object[0])
						if duration >= 10:
							nb = (duration // 10) * 10
						is_exist = False
						for i in range(0, len(durations[val])):
							if durations[val][i]["duration"] == nb:
								is_exist = True
								break
						if is_exist:
							durations[val][i]["value"] += 1
						else:
							new_element = {	
											"duration" : nb,
											"value" : 1
										}
							durations[val].append(new_element)	

			else:
				first_line = False

		print(durations)
	with open("data_duration_country.json", "w") as json_file:
		json.dump(durations, json_file)

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

load_data_country("netflix_titles")	
load_data_all("netflix_titles")


				        