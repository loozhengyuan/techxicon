from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.http import HttpResponse
from .models import Term, ImproveLog, FeedbackLog, SuggestLog, SearchLog
import string


def index(request):
    return render(request, 'core/base_index.html')


def search(request):
    if request.POST:
        if request.POST.get('keyphrase', False) is not False:
            searched = request.POST['keyphrase']
            s = SearchLog(search_phrase=searched)
            s.save()
            vector = SearchVector('term', weight='A') + \
                     SearchVector('acronym', weight='A') + \
                     SearchVector('definition', weight='D') + \
                     SearchVector('explanation', weight='D') + \
                     SearchVector('examples', weight='D') + \
                     SearchVector('see_also', weight='D') + \
                     SearchVector('tags', weight='B')
            query = SearchQuery(" | ".join(str(searched).split()))
            exact_match = Term.objects.filter(term__iexact=searched)
            fts_match = Term.objects.exclude(pk__in=exact_match).annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.05).order_by('-rank')
            results = list(exact_match) + list(fts_match)
            alphabets = list(string.ascii_lowercase)
            return render(request, 'core/base_search.html', {'results': results,
                                                             'searched': searched,
                                                             'alphabets': alphabets})
        if request.POST.get('suggest_keyphrase', False) is not False:
            sg_response = SuggestLog(name="",
                                     dept="",
                                     suggestion=request.POST['suggest_keyphrase'])
            sg_response.save()
            return HttpResponse(status=200)
    alphabets = list(string.ascii_lowercase)
    return render(request, 'core/base_search.html', {'alphabets': alphabets})


def term(request, term_str):
    term = Term.objects.get(term=term_str)
    if request.POST:
        if request.POST['improve_text']:
            comments = request.POST['improve_text']
            improvement = ImproveLog(term=term, comments=comments)
            improvement.save()
    return render(request, 'core/base_term.html', {'term': term})


def about(request):
    return render(request, 'core/base_about.html')


def suggest(request):
    if request.POST:
        if request.POST['suggest_keyphrase'] not in ['']:
            sg_response = SuggestLog(name=request.POST['suggest_name'],
                                     dept=request.POST['suggest_dept'],
                                     suggestion=request.POST['suggest_keyphrase'])
            sg_response.save()
    return render(request, 'core/base_suggest.html')


def feedback(request):
    if request.POST:
        if request.POST['feedback_text'] not in ['']:
            fb_response = FeedbackLog(name=request.POST['feedback_name'],
                                      dept=request.POST['feedback_dept'],
                                      feedback=request.POST['feedback_text'])
            fb_response.save()
    return render(request, 'core/base_feedback.html')


def explore(request, alphabet):
    results = Term.objects.filter(term__istartswith=alphabet)
    alphabets = list(string.ascii_lowercase)
    return render(request, 'core/base_search.html', {'results': results,
                                                     'alphabets': alphabets})
