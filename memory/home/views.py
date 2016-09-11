from django.shortcuts import render

from django.views.generic import View
# Create your views here.

from django.http import HttpResponse

from raspicode.code import Memory

class Index(View):
        template_name = 'home/index.html'
        def get(self, request, *args, **kwargs):
            m = Memory()
            m.offLed()
            with open('assets/run.txt', 'w+') as f:
                f.write("0")
            return render(request, self.template_name,)
