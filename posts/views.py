from django.shortcuts import render
from posts.forms import PostCreateForm

# Create your views here.
def myview(request):
	if request.method == 'POST':
		form = PostCreateForm(request.POST, extra=request.POST.get('extra_field_count'))
		print("hello")
		if form.is_valid():
			form.save()

	else:
		form = PostCreateForm()
	return render(request, "posts/post_new.html", { 'form': form })