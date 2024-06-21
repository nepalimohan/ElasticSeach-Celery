import faker
from django.core.management.base import BaseCommand
from product.models import Product


class Command(BaseCommand):
    help = 'Insert 100 books into the database'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()

        books = []
        for _ in range(100000):
            book = Product(
                name=fake.sentence(nb_words=5),
                category=fake.name(),
                description=fake.text()
            )
            books.append(book)
        
        Product.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS('Successfully inserted 100000 books'))