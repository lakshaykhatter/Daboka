from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.forms import PostCreateForm, LinkForm
from django.forms.models import modelformset_factory # model form for querysets
from posts.models import Link, Post
from django.shortcuts import redirect, render, get_object_or_404


@login_required
def post_create_view(request):
	form = PostCreateForm(request.POST or None)
	LinkFormset = modelformset_factory(Link, form=LinkForm, extra=0)
	formset = LinkFormset(request.POST or None,queryset=Link.objects.none())

	context = {
		"form": form,
		"formset": formset

	}
	if all([form.is_valid(), formset.is_valid()]):
		parent = form.save(commit=False)
		parent.author = request.user
		parent.save()
		# formset.save()
		for form in formset:
			child = form.save(commit=False)
			child.post = parent
			child.save()
		context['message'] = 'Data saved.'
		return redirect('post_detail', urlhash=parent.urlhash)
	return render(request, "posts/post_new.html", context)


@login_required
def post_detail_view(request, urlhash):
	context={}
	obj = get_object_or_404(Post, urlhash=urlhash)
	context = {
		"object": obj
	} 
	return render(request, "posts/post_detail_view.html", context)


@login_required
def post_update_view(request, urlhash=None):
	obj = get_object_or_404(Post, urlhash=urlhash, author=request.user)
	form = PostCreateForm(request.POST or None, instance=obj)
	LinkFormset = modelformset_factory(Link, form=LinkForm, extra=0)
	qs = obj.links.all()
	formset = LinkFormset(request.POST or None, queryset=qs)
	context = {
		"form": form,
		"formset": formset,
		"object": obj
	}
	if all([form.is_valid(), formset.is_valid()]):
		parent = form.save(commit=False)
		parent.save()
		# formset.save()
		for form in formset:
			child = form.save(commit=False)
			child.post = parent
			child.save()
		context['message'] = 'Data saved.'
	return render(request, "posts/post_update.html", context) 
