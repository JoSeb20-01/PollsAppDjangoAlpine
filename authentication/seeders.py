from core.seeder.seeder import Seeder
from .factory import UserFactory

class UserSeeder(Seeder):
    
    def seed_data(self):
        UserFactory.create_batch(20)
