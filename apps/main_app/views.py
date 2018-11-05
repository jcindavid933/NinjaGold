from django.shortcuts import render,redirect
from random import randrange
from time import strftime, localtime

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['profit'] = 0
        request.session['activity'] = []
    return render(request, 'main_app/index.html')

def process_money(request):
    time = strftime("%I:%M:%S, %B %d %Y", localtime())


    if request.method == 'POST':
        if request.POST['hidden'] == 'casino':
            request.session['profit'] = randrange(-100,101)
            request.session['total_gold'] += request.session['profit']
            if request.session['profit'] < 0:
                data = {
                    'word': 'Entered a casino and lost' + str(request.session['profit']) + ' golds... OUCH. (' + time + ')',
                    'color': 'red'
                }
            else:
                data = {
                    'word': 'Entered a casino and gained' + str(request.session['profit']) + ' golds... NICE!! (' + time + ')',
                    'color': 'green'
                }
            request.session['activity'].append(data)
            request.session.modified = True
        elif request.POST['hidden'] == 'farm':
            request.session['profit'] = randrange(10,21)
            request.session['total_gold'] += request.session['profit']
            data = {
                'word': 'Entered a farm and made ' + str(request.session['profit']) + ' golds from the farm! (' + time + ')',
                'color': 'green'
            }
            request.session['activity'].append(data)
            request.session.modified = True
        elif request.POST['hidden'] == 'cave':
            request.session['profit'] = randrange(5,11)
            request.session['total_gold'] += request.session['profit']
            data = {
                'word': 'Entered a cave and made ' + str(request.session['profit']) + ' golds from the cave! (' + time + ')',
                'color': 'green'
            }
            request.session['activity'].append(data)
            request.session.modified = True
        elif request.POST['hidden'] == 'house':
            request.session['profit'] = randrange(2,6)
            request.session['total_gold'] += request.session['profit']
            data = {
                'word': 'Entered a house and made ' + str(request.session['profit']) + ' golds from the house! (' + time + ')',
                'color': 'green'
            }
            request.session['activity'].append(data)
            request.session.modified = True
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
