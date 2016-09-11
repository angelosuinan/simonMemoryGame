from django.shortcuts import render

from django.views.generic import View
# Create your views here.

from django.http import HttpResponse
import threading
from raspicode.code import Memory

class Index(View):
        template_name = 'game/index.html'
        def get(self, request, *args, **kwargs):
            m= Memory()
            with open('assets/run.txt', 'w+') as f:
                    f.write("1")
            t =threading.Thread(target=m.start)
            t.start()
            return render(request, self.template_name,)
