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
from accounts.forms import CustomUserChangeForm
from django.shortcuts import redirect


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

def edit_profile_view(request,username):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('profile_view', kwargs={"username": request.user.username } ))
	else:
		if username == request.user.username:
			form = CustomUserChangeForm(instance=request.user)
			args = {'form': form}
			return render(request, 'account/edit_profile.html', args)
		else:
			return redirect(reverse('profile_view', kwargs={'username': request.user.username}))
