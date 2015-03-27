import random

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from base.models import Kudo

class Command(BaseCommand):
    help = 'simulate people giving a whole lotta kudos'

    simulated_user_prefix = "bot-"
    n_simulated_users = 10

    def handle(self, *args, **kwargs):

        # the set of existing users in the database. if they don't yet exist,
        # throw a nice error to remind people to register a user first so they
        # can actually see the results of the simulation
        self.existing_users = self.get_existing_users()

        # create a bunch of simulation users if they don't exist
        self.simulated_users = self.get_or_create_simulated_users()

        # give kudos from the new simulated users
        for n in range(1000):
            giver, receiver = self.simulate_giver_receiver()
            kudo = Kudo.objects.create(
                giver=giver,
                count=self.simulate_count(),
                message=self.simulate_message(),
            )
            kudo.receivers.add(receiver)
            kudo.save()

    def get_existing_users(self):
        existing_users = User.objects.exclude(
            username__startswith=self.simulated_user_prefix,
        )
        if existing_users.count()==0:
            raise CommandError("yo. create a user by logging into the site")
        return existing_users

    def get_or_create_simulated_users(self):
        simulated_users = list(User.objects.filter(
            username__startswith=self.simulated_user_prefix,
        ))
        if not simulated_users:
            for n in range(self.n_simulated_users):
                username = self.simulated_user_prefix + str(n)
                User.objects.create_user(username)
            return self.get_or_create_simulated_users()
        return simulated_users

    def simulate_giver_receiver(self):
        giver = random.choice(self.existing_users)
        receiver = random.choice(self.simulated_users)
        if random.random() < 0.5:
            temp = giver
            giver = receiver
            receiver = temp
        return giver, receiver

    def simulate_count(self):
        return random.randint(1,3)

    def simulate_message(self):
        return random.choice([
            # i can't make this shit up. took the "thank yous" <140 chars from
            # http://smstosay.com/thanks-sms/20-sms-to-say-thank-you-sms-to-say-thanks/
            "Even if every flower in the world had a voice I could not send as many as it would take to say thanks enough! So Thank You",
            "A thankful person is thankful under all circumstances. A complaining soul complains even if he lives in paradise.",
            "Words can't express the gratitude I feel when I think about what you have done. I'll just say thanks.",
            "Thank you for sacrificing for us. You have set aside your own needs Just to let us have the best that we can have.",
            "Please, accept my heartfelt thanks, my dear family, for your allegiance and devotion.",
            "Thank you much more, than a greeting can say, because you were thoughtful In such a nice way!",
            "Thank you always being there for me. You mean so much to me.",
            "Thank you for the warm and lovely wishes, your thoughtfulness and for joining us on the lovely occasion. You are very special.",
            "Have you thanked your parents for taking care of you? If not, go ahead and give them a hug. They will already feel what you wanted to say.",
            "For your cordiality, trust and whole-hearted support, Please, accept my deep appreciation.",
            "May God give you the best things that you deserve because you have touched our lives so meaningfully. Thank you!",
            "Thanks for being my friend. Thanks for thinking of me you shouldn't have but I'm so glad you did.",
            "A simple 'thank you' goes a long way. It uplifts someone's spirit and makes him do more good things!",
            "I'm grateful to know you and want to say thanks again for always be there for me and being my best friend.",
            "Your irreplaceable heartiness. Love and understanding are the sources of my strength. Please, accept my heartfelt thanks for that.",
            "I know it wasn't always easy but for loving me, I owe you my best thanks.",
            "For always being on my side, for your protection and support, for sharing my dreams I do thank you, my friend.",
            "We will always be thankful to you for all the hard work and efforts you have put in, for educating us.",
        ])
