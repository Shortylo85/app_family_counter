import csv
import os

from django.core.management.base import BaseCommand
from ui.models import City


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, **args):
        print("Start")
        
        directory = "/home/danijel/Downloads/csv_files/family_counter/GeoLite2-City-CSV_20170801"
        
        locations = open(os.path.join(directory, 'GeoLiteCity-Location.csv'))
        
        csv_file = csv.reader(locations)
        
        counter = 0
        
        for row in csv_file:
            city = City()
#             data = {
#                'city_name': row[3],
#                 'lat': row[5],
#                 'lng': row[6],
#             }
            city.country = row[1]
            city.city_name = row[3]
            city.lat = row[5]
            city.lng = row[6]
            
            city.save()
            
            if counter > 2000:
                break
                print("imported {} entries".format(counter))
            counter += 1