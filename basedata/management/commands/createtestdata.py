import time

from faker import Faker
from progress.bar import ChargingBar

from django.core.management.base import BaseCommand
from basedata.models import Human, Dog, DogFriendHuman


class Command(BaseCommand):
    help = "Auto create test data"

    def handle(self, *args, **options):
        tm = time.time()
        faker = Faker()

        humans_ = []
        humans_bar = ChargingBar('Generating Humans', max=1_000_000)
        for _ in range(1_000_000):
            humans_.append(Human(name=faker.first_name()))
            humans_bar.next()
        humans_bar.finish()

        dogs_humans = []
        dogs_humans_bar = ChargingBar('Finding friends', max=1_000_000 * 10)
        for _ in range(1_000_000):
            friends_for_human = []
            for _ in range(10):
                friends_for_human.append(Dog(name=faker.first_name()))
                dogs_humans_bar.next()
            dogs_humans.append(friends_for_human)
        dogs_humans_bar.finish()

        humans = []
        humans_bar = ChargingBar('Inserting Humans into DB', max=1_000)
        for _ in range(0, 1_000_000, 1000):
            humans += Human.objects.bulk_create(humans_[_: _ + 1000], batch_size=1000)
            humans_bar.next()
        humans_bar.finish()

        friends_bar = ChargingBar('Find Friends for Humans', max=1_000_000)
        for dogs, human in zip(dogs_humans, humans):
            dogs = Dog.objects.bulk_create(dogs, batch_size=1000)
            friends = [DogFriendHuman(human=human, dog=dog) for dog in dogs]
            DogFriendHuman.objects.bulk_create(friends, batch_size=1000)
            friends_bar.next()
        friends_bar.finish()
        print('OK')
        print('Time: {:.2f}'.format(time.time() - tm))
