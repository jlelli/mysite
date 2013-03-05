from django.http import HttpResponse
from django.template import Context, loader
import datetime

def home(request):
    template = loader.get_template('home/index.html')
    title = """
    Welcome!
    """
    content = """
    <p>I'm a PhD student at <a href="http://www.sssup.it/" target=_blank>Scuola Superiore Sant'Anna</a>
       in Pisa (Italy). I'm part of the Real-Time Systems Laboratory (<a href="http://retis.sssup.it/"
       target=_blank>ReTiS Lab</a>) of the <a href="http://ceiicp.sssup.it/" target=_blank>Institute of
       Communication, Information and Perception Technologies</a>. My supervisor is <a
       href="http://feanor.sssup.it/~lipari" target=_blank>Giuseppe Lipari</a>.</p>
    <p>My research interests are in Real-Time Systems, Real-Time Operating Systems and Scheduling
       Algorithms.</p>
    """
    context = Context({
        'title': title,
        'content': content
    })

    return HttpResponse(template.render(context))
