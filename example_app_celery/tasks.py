import time
from celery import shared_task


@shared_task
def fake_send_mail():
    time.sleep(5*60) # simula que se demora 5 minutos
    return 'Correo enviado con exito'


@shared_task
def example_programmed_task():
    # Este sera un task que desde el panel del admin
    # colocas a ejecutarse cada x tiempo
    return 'la fecha es %s' % time.strftime("%y-%m-%d %H:%M")

