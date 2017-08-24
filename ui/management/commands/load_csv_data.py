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
            
            data = {
               'city_name': row[3],
                'lat': row[5],
                'lng': row[6],
            }
            
            City.objects.get_or_create(data)
            
            if counter % 1000 == 0:
                print("imported {} entries".format(counter))
            counter += 1