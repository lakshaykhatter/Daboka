from django.views.generic import TemplateView
from pages.forms import CodeSearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from posts.models import Post
from django.conf import settings



# class HomePageView(TemplateView):
#     template_name = 'pages/home.html' 

def HomePageView(request):
	if request.method == "POST":
		form = CodeSearchForm(request.POST)
		context = {}

		if form.is_valid():
			urlhash = form.cleaned_data['urlhash'].upper()

			if len(urlhash) == 7 and Post.objects.filter(urlhash=urlhash).exists()  :
				return HttpResponseRedirect(reverse('post_detail',kwargs={'urlhash': urlhash}))
			else:
				context["form"] = form
				if Post.objects.filter(urlhash=urlhash).exists() == False:
					context['message'] = 'Please retry another code'

				return render(request, "pages/home.html", context) 



	else:
		form = CodeSearchForm()

	return render(request, "pages/home.html", {"form": form})
	

class AboutPageView(TemplateView):
	template_name = 'pages/about.html'