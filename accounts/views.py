from django.shortcuts import render
from .models import CustomUser
from posts.models import Post
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.urls import reverse
from allauth.account.views import LoginView as AllauthLoginView
from allauth.account.utils import get_next_redirect_url

# Create your views here.
def profile_view(request, username):
	u = CustomUser.objects.get(username=username)
	user_posts = Post.objects.filter(author=u).order_by('-date')
	return render(request, "account/profile.html", {"posts":user_posts})




class LoginView(AllauthLoginView):
	def form_valid(self, form):
		self.user = form.user # Get the forms user
		return super().form_valid(form)
	
	def get_success_url(self):
		ret = (get_next_redirect_url(self.request, self.redirect_field_name)
			or reverse('profile_view', kwargs={'username': self.user.username}))
		return ret