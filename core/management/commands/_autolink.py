from django.core.management.base import BaseCommand, CommandError
from core.models import Term


class Command(BaseCommand):
    help = 'Check for link and add hyperlink automagically'

    def get_list(self):
        terms_queryset = Term.objects.all().values('term')
        terms_list = [x for x in terms_queryset]
        return terms_list

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))