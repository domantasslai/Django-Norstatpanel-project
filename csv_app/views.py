import csv
from django.http import HttpResponse
from polls.models import Poll

# Simple CSV Write Operation
def csv_simple_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_Poll_question_query.csv"'

    writer = csv.writer(response)
    # writer.writerow(['first_name', 'last_name', 'email'])
    # writer.writerow(['Domantas', 'Slaiciunas', 'domantas@gmail.com'])
    # writer.writerow(['Lukas', 'Kavaliauskas', 'lukas@gmail.com'])
    # writer.writerow(['Gytis', 'Putvinskas', 'gytis@gmail.com'])

    polls = Poll.objects.all()
    writer.writerow(['Polls question query:'])
    writer.writerow([polls])


    return response
