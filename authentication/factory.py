from sqlite3 import Cursor
import factory

from django.db import connection
from .models import User

def get_last_id_table_sqlite3(table):
    with connection.cursor() as c:
        cursor: Cursor = c
        cursor.execute("SELECT seq FROM sqlite_sequence WHERE name=%s", (table,))
        row = cursor.fetchone()
        
    return row[0] if row else 0

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user-{n}")
    email = factory.LazyAttribute(lambda o: f'{o.username}@gmail.com')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
        
    @classmethod
    def _setup_next_sequence(cls):
        return get_last_id_table_sqlite3("authentication_user")
    
    class Meta:
        model = User
        abstract = False
