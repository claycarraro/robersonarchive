import csv
from main.models import Pigment, Material
from pathlib import Path

def run():
   with open('main/CSV/MATERIALS2.csv',) as csvfile:
    reader= csv.reader(csvfile, delimiter=';')
    next(reader)

    for row in reader:

      print("Data entry:", row)

      qs = Material.objects.filter(id=row[0]) # check row (existing element)

      #This function checks if the image exists in the folder
      #If it exists, it links to that image, otherwise to the default image
      number=str(row[0])
      img='IMGM_'+number+'.png'
      file = Path('main/static/IMGM/'+img)
      image = 'static/IMGM/'+img

      if file.is_file():
        file = file
      else:
        file = 'static/IMGM/defaultmaterial.png'

      if qs:
        print("Material", str(row[4]) , "already exists in database")
        material = Material.objects.get(id=row[0])
        material.archive_id = row[1]
        material.name = row[2]
        material.m_pictures = image
        material.type_of_material = row[4]
        material.factory = row[5]
        material.geographical_origins = row[6]
        material.physical_properties = row[7]
      
        material.save()
        print("Material", str(row[2]),"updated.\n")
      else: 

        print("Material", str(row[2]) , "do not exist in database")
        material = Material(
          id = row[0],
            archive_id = row[1],
            name =row[2],
            m_pictures = image,
            type_of_material= row[4],
            factory= row[5],
            geographical_origins = row[6],
            physical_properties = row[7],
          )

        material.save()
        print("Material", str(row[4]),"added to database.\n")