from celery import shared_task

@shared_task()
def print_text_hello_world():
    print('Hello world from user')


# from user_app.tasks import print_text_hello_world
# print_text_hello_world.delay()
