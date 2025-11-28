from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice

# Home page — list all polls
def welcome(request):
    polls = Poll.objects.all()
    return render(request, 'votes/welcome.html', {'polls': polls})

# Survey page — show a specific poll and choices
def survey(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'votes/survey.html', {'poll': poll})

# Vote processing
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        choice_id = request.POST['choice']
        selected_choice = poll.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votes/survey.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to results page
        return redirect('results', poll_id=poll.id)

# Results page
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'votes/results.html', {'poll': poll})

# Optional: thank you page after voting
def thank_you(request):
    return render(request, 'votes/vote.html')
