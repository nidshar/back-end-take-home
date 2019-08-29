from django.core.management.base import BaseCommand, CommandError
from shortestPath.models import Airline, Airport, Route
import csv
import psycopg2

class Command(BaseCommand):
    help = 'Import Data'

    def handle(self, *args, **options):
        import_obj = DataImport()
        self.stdout.write("Importing Airlines...")
        import_obj.airline("../data/test/airlines.csv")
        self.stdout.write(self.style.SUCCESS('Successfully imported airlines'))

        self.stdout.write("Importing Airports...")
        import_obj.airport("../data/test/airports.csv")
        self.stdout.write(self.style.SUCCESS('Successfully imported airports'))
        
        self.stdout.write("Importing Routes...")
        import_obj.route("../data/test/routes.csv")
        self.stdout.write(self.style.SUCCESS('Successfully imported routes'))
        
    
class DataImport:
    
    def airline(self,file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row.
            airline_data = {}
            for row in reader:
                airline_data["name"] = row[0]
                airline_data["digit_code"] = row[1]
                airline_data["three_digit_code"] = row[2]
                airline_data["country"] = row[3]
                
                try:
                    Airline.objects.get(**airline_data)
                except Airline.DoesNotExist:
                    Airline.objects.create(**airline_data)
            f.close()
                    
    def airport(self,file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            airport_data = {}
            for row in reader:
                airport_data["name"] = row[0]
                airport_data["city"] = row[1]
                airport_data["country"] = row[2]
                airport_data["code"] = row[3]
                airport_data["latitude"] = row[4]
                airport_data["longitude"] = row[5]
                    
                try:
                    Airport.objects.get(**airport_data)
                except Airport.DoesNotExist:
                    Airport.objects.create(**airport_data)
                
            f.close()
        
    def route(self,file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            route_data = {}
            for row in reader:
                route_data["airline"] = Airline.objects.get(digit_code=row[0])
                route_data["origin"] = Airport.objects.get(code=row[1])
                route_data["destination"] = Airport.objects.get(code=row[2])
                try:
                    Route.objects.get(**route_data)
                except Route.DoesNotExist:
                    Route.objects.create(**route_data)
                
            f.close()            
    

