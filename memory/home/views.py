from django.shortcuts import render

from django.views.generic import View
# Create your views here.

from django.http import HttpResponse

from raspicode import code

class Index(View):
        template_name = 'home/index.html'
        def get(self, request, *args, **kwargs):
            return render(request, self.template_name,)
