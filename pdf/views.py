from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from polls.models import Poll, Choice

from .utils import render_to_pdf


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        polls = Poll.objects.all()
        choice = Choice.objects.all()
        context = {
            # "invoice_id": 123,
            # "customer_name": "John Cooper",
            # "amount": 1399.99,
            # "today": "Today",
            'poll': polls,
            'choice': choice,

        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
