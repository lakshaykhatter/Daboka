from django.views.generic import TemplateView
from pages.forms import CodeSearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# class HomePageView(TemplateView):
#     template_name = 'pages/home.html' 

def HomePageView(request):
	if request.method == "POST":
		form = CodeSearchForm(request.POST)
		if form.is_valid():
			urlhash = form.cleaned_data['urlhash']

			if len(urlhash) == 7:
				return HttpResponseRedirect(reverse('post_detail',kwargs={'urlhash': urlhash}))
			else:
				context = {}
				context["form"] = form
				context['message'] = 'Please enter 7 digit code'
				return render(request, "pages/home.html", context) 



	else:
		form = CodeSearchForm()
	return render(request, "pages/home.html", {"form": form})
	

class AboutPageView(TemplateView):
	template_name = 'pages/about.html'