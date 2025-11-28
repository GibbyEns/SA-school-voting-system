from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice

# Home page
def welcome(request):
    return render(request, 'votes/welcome.html')

# Survey page (optional feedback or surveys)
def survey(request):
    return render(request, 'votes/survey.html')

# List all polls
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'votes/poll_list.html', {'polls': polls})

# Show poll details and vote form
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'votes/vote.html', {'poll': poll})

# Handle voting POST
def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    
    if request.method == "POST":
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = poll.choice_set.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll_results', poll_id=poll.id)
        else:
            error = "You didn't select a choice."
            return render(request, 'votes/vote.html', {'poll': poll, 'error': error})
    
    return redirect('poll_detail', poll_id=poll.id)

# Show poll results
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'votes/results.html', {'poll': poll})
