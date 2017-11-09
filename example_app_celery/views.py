from django.http import HttpResponse
from django.views import View

from .tasks import fake_send_mail

class FakeSendMailView(View):
    def get(self, request, *args, **kwargs):
        html = '''
            <form method="post">
            <input type="submit" value="Enviar Correo Fake" />
            </form>
        '''
        return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        # Juega cambiando la forma de ejecutar la funcion
        #Con celery
        fake_send_mail.delay()
        #Sin celery
        # fake_send_mail()

        html = 'Su Correo Fake Se esta procesando'
        return HttpResponse(html)

