from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site


# this command is used during provisioning to make sure the sites are
# properly configured
class Command(BaseCommand):
    help = 'create a site with the correct id'
    args = 'site_id site_name'

    def handle(self, *args, **kwargs):
        Site.objects.get_or_create(
            id=args[0],
            domain=args[1],
            name=args[1],
        )
