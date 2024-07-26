import csv
from main.models import Pigment, Material
from pathlib import Path

def run():
	 with open('main/CSV/PIGMENTS2.csv',) as csvfile:
	 	reader= csv.reader(csvfile, delimiter=';')
	 	next(reader) #skip the headers

	 	for row in reader:

	 		print("Data entry:", row)

	 		qs = Pigment.objects.filter(id=row[0]) # check row (existing element)

	 		#This function checks if the image exists in the folder
      		#If it exists, it links to that image, otherwise to the default image
	 		number=str(row[0])
	 		img='IMGB_'+number+'.png'
	 		file = Path('main/static/IMGB/'+img)
	 		image = 'static/IMGB/'+img

	 		if file.is_file():
	 			file = file
	 		else:
	 			file = 'static/IMGB/defaultbottle.png'

	 		if qs:
	 			print("Pigment", str(row[4]) , "already exists in database")
	 			pigment = Pigment.objects.get(id=row[0])
	 			# pigment.label_picture = row[1]
	 			pigment.bottle_picture = image
	 			pigment.archive_id = row[3]
	 			pigment.specific_name = row[4]
	 			pigment.description = row[5]
	 			pigment.color = row[6]
	 			pigment.shade = row[7]
	 			pigment.stopper = row[8]
	 			pigment.geographical_origins = row[9]
	 			pigment.date_of_production = row[10]
	 			pigment.chemical_composition = row[11]
	 			pigment.physical_properties = row[12]
	 			pigment.archive_description = row[13]

	 			pigment.save()
	 			print("Pigment", str(row[4]),"update.\n")
	 		else: 

	 			print("Pigment", str(row[4]) , "do not exist in database")
	 			pigment = Pigment(
	 				id = row[0],
				    # label_picture = row[1],
				    bottle_picture = image,
				    archive_id = row[3],
				    specific_name = row[4],
				    description = row[5],
				    color = row[6],
				    shade = row[7],
				    stopper = row[8],
				    geographical_origins = row[9],
				    date_of_production = row[10],
				    chemical_composition = row[11],
				    physical_properties = row[12],
				    archive_description = row[13],
	 				)

	 			pigment.save()
	 			print("Pigment", str(row[4]),"added to database.\n")