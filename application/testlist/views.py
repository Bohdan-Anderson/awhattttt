from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from testlist.models import *
import json, time
from random import randint

# Create your views here.

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def meta_to_string(request):
	out = {}
	for key in request.META:
		if request.META[key]:
			try:
				out[key] = str(request.META[key])
				# print "\n%s\n\t%s"%(key,request.META[key])
			except Exception, e:
				pass

	return json.dumps(out)

def home(request):
	print "\n\n"
	if request.method == 'POST':
		print "is post"
		form = ArticleForm(request.POST)
		# time.sleep(3)
		if form.is_valid():
			print "is valid"

			newSubmission = form.save()
			newSubmission.newIp = get_client_ip(request)
			newSubmission.meta_info = meta_to_string(request)
			newSubmission.save()

			if not newSubmission.emailAddress and ((newSubmission.firstName and not newSubmission.lastName) or (not newSubmission.firstName and newSubmission.lastName)):
				return render(request, 'index.html', {'message': "There was no %d matches for your quiery, be more specific"%randint(0,5000)})
			return render(request, 'index.html', {'message': "There was no matches for your quiery"})

		else:
			return render(request, 'index.html', {'errors': form})

	return render(request, 'index.html', {'message': ""})

from django.forms import ModelForm

class ArticleForm(ModelForm):
	class Meta:
		model = Submission
		fields = ['emailAddress', 'firstName', 'lastName', 'usertime']