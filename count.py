import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SCripts.settings'
django.setup()
from Facebook_Pages.models import FacebookDatapages,Facebook_Category


def store_to_csv(text):
    f = open('ip_list/link.csv', 'a')
    f.write(text)
    f.write("\n")# Give your csv text here.
    ## Python will convert \n to os.linesep
    f.close()


for data in FacebookDatapages.objects.values('fb_page_link').filter(page_id__isnull=False):
   store_to_csv(str(data['fb_page_link']))


