from django.shortcuts import render, redirect, HttpResponse

# Create your views here. THIS IS THE CONTROLLER!!!
# import all the good stuff here!!

def index(request):
	return render(request, 'surveyform/index.html')
	# redirect("/")

# def runThis():
#     return redirect('/')

def result(request):
 	return render(request, 'surveyform/result.html')
	#  this is the results page from the form


def surveyPost(request):
		# before using this you must migrate !!
		# >> python ../../manage.py migrate
	# request.session['name'] = request.form['name']

	if request.method == 'POST':
		something = "This is a string! ************"
		context = {
			'something': something
		}
		print context
		request.session['name'] = request.POST['name']
		if request.session['counter']:
			counter = request.session['counter']
		else:
			counter = 0
		counter += 1
		request.session['counter'] = counter

		return redirect('/result')
	else:
		return 'sorry this did not work right...'


def show(request, id):
	context = {
		"id": id
	}
	return render(request, "surveyform/show.html", context)
