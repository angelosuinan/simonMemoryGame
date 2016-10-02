from django.shortcuts import render

from django.views.generic import View
# Create your views here.

from django.http import HttpResponse
import threading
from raspicode.code import Memory
m= Memory()
class Index(View):
        template_name = 'home/index.html'
       	def get(self, request, *args, **kwargs):
            t =threading.Thread(target=m.start)
            t.start()
            return render(request, self.template_name,)
