import csv
import gzip
import os

from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'this command will download a source archive, extract it and populate items into the database'

    def __init__(self):
        self.source = 'http://download.db-ip.com/free/dbip-city-2017-08.csv.gz'

    def downloadFile(self):
        try:
            file_data = requests.get(self.source, auth=(u'user', u'password'), stream=True)
            total_size = int(file_data.headers['Content-Length'])
            dowloaded_size = 0
            if(file_data.status_code == 200):
                filename = '{}'.format(self.source.strip().split('/')[-1])
                with open(filename, 'wb') as f:
                    for chunk in file_data.iter_content(chunk_size=1024):
                        if chunk:
                            dowloaded_size += len(chunk)
                            print('\r{:.02f} % ...'.format((dowloaded_size/total_size) * 100), end='')
                            f.write(chunk)
                    print(' DONE!')
                return filename
            else:
                print('download status code = {}\nfor URL: {}'.format(file_data.status_code, self.source))
        except Exception as ex:
            self.exception(str(ex))
        return None

    def handle(self, **args):
        # try to open the csv file
        csv_file = os.path.split(self.source )[-1].strip('.gz')
        if not os.path.isfile(csv_file):
            # try to open the archive
            filename = os.path.split(self.source )[-1]
            if not os.path.isfile(filename): 
                # download archive file from it's source
                filename = self.downloadFile()
            
            with gzip.open(filename, 'rb') as gz:
                with open(filename.strip('.gz'), 'wb') as csvf:
                    csvf.write(gz.read())
        
        csvf = csv.reader(open(csv_file))
        counter = 0
        for row in csvf:
            print(row)
            if counter > 20:
                break
            counter += 1