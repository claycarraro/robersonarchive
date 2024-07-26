import csv
from main.models import Transcription
from pathlib import Path

def run():
   with open('main/CSV/TRANSCRIPTIONS.csv',) as csvfile:
    reader= csv.reader(csvfile, delimiter=';')
    next(reader)

    for row in reader:

      print("Data entry:", row)

      qs = Transcription.objects.filter(id=row[0]) # check row (existing element)

      #This function checks if the image exists in the folder
      #If it exists, it links to that image, otherwise to the default image
      ms=str(row[1])
      page_number=str(row[2])
      img=ms+'_'+page_number+'.jpg'
      file = Path('main/static/Rectos/'+img)
      image = 'static/Rectos/'+img

      if file.is_file():
        file = file
      else:
        file = None

      if qs:
        print("Transcription", str(row[1]+', p:'+row[2]) , "already exists in database")
        transcription = Transcription.objects.get(id=row[0])
        transcription.ms_number = row[1]
        transcription.image = image
        transcription.pagenumber = row[2]
        transcription.transcription = None
      
        transcription.save()
        print("Transcription", str(row[1]+', p:'+row[2]),"updated.\n")
      else: 
        print("Transcription", str(row[1]+', p:'+row[2]) , "do not exist in database")
        transcription = Transcription(
          id = row[0],
          ms_number = row[1],
          image = image,
          pagenumber = row[2],
          transcription = None
          )

        transcription.save()
        print("Transcription", str(row[1]+', p:'+row[2]),"added to database.\n")