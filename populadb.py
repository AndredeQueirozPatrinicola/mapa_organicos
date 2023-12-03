import os
import django
import random

# Set up Django environment
# settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from accounts.models import Produtor
from django.conf import settings


def generate_brazilian_name():
    # Replace this with a list of Brazilian names
    first_names = ["João", "Maria", "José", "Ana", "Carlos", "Fernanda"]
    last_names = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Lima"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return first_name, last_name

def generate_random_email(username):
    # Replace this with your domain
    domain = "example.com"
    return f"{username}@{domain}"

def populate_database():
    for _ in range(10):  # Change the number based on how many users you want to create
        # Generate random user details
        username = f"user_{random.randint(1000, 9999)}"
        password = "Presuntinho123"
        email = generate_random_email(username)
        first_name, last_name = generate_brazilian_name()

        # Create a Django user
        user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name)

        # Create a Produtor instance
        latitude = round(random.uniform(-23.800214, -23.450131), 6)
        longitude = round(random.uniform(-46.818128, -46.424073), 6)
        tipo_produtor = random.choice(['F', 'P', 'C'])
        nome_fantasia = f"{first_name} {last_name}'s Farm"
        logradouro = f"Rua {random.randint(1, 100)}"
        numero = random.randint(10, 1000)

        produtor = Produtor.objects.create(
            nome_fantasia=nome_fantasia,
            user=user,
            latitude=str(latitude),
            longitude=str(longitude),
            tipo_produtor=tipo_produtor,
            logradouro=logradouro,
            numero=numero
        )

        print(f"User '{username}' and Produtor '{nome_fantasia}' created successfully.")

if __name__ == "__main__":
    populate_database()