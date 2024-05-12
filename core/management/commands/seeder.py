from django.core.management.base import BaseCommand, CommandParser
from core.seeder import seeder

class SeederCommand(BaseCommand):

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("--seeder_name", type=str)

    def handle(self, *args, **options):
        if options["seeder_name"]:
            self.execute_seeder(options["seeder_name"])
            return
        self.execute_all_seeders()
    
    def execute_seeder(self, class_name):
        obj = seeder.get_seeder_by_name(class_name)
        self.stdout.write(f"Execute {class_name}.", ending="\n")
        obj().seed_data()
        del obj
        self.stdout.write(self.style.SUCCESS("The seeder executed successfully."), ending="\n")
            
    def execute_all_seeders(self):
        for name, seeder_class in seeder.get_seeders().items():
            self.stdout.write(f"Execute {name}.", ending="\n")
            seeder_class().seed_data()
        
        self.stdout.write(self.style.SUCCESS("All seeders executed successfully."), ending="\n")
