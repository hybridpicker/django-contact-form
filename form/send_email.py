import re
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import ContactKeyword


'''
Contact Student
'''
def check_message(message):
    words = re.findall("\w+",message)
    keywords = ContactKeyword.objects.all()
    for keyword in ContactKeyword.objects.all():
        if keyword.keyword in words:
            answer_keyword = ContactKeyword.objects.get(keyword__contains=keyword)
            answer = answer_keyword.answer
            return answer

def contact_mail(from_email, subject, message, context, send_mail=True):
    #from_email = settings.EMAIL_HOST_USER
    subject = 'Thank you for your message!'
    message = message
    answer = check_message(message)
    name = context.get('first_name') + ' ' + context.get('last_name')
    location = context.get('location')
    today = context.get('today')
    instrument = context.get('subject')
    if answer == None:
        answer = ''
    html_message = render_to_string('templates/mail/answer_mail_template.html',
                                    {'context': 'values',
                                     'message': message, 'answer': answer})
    plain_message = strip_tags(html_message)
    to = from_email

    if send_mail:
        # Sending Message to User
        from django.core import mail
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        # Creating Mail to EMAIL_HOST_USER
        from_email = from_email = settings.EMAIL_HOST_USER
        subject = 'New Message'
        customer_email = context.get('from_email')
        html_message = render_to_string('templates/mail/mail_template.html',
                                        {'context': 'values', 'name': name,
                                         'location': location, 'today': today,
                                         'instrument': instrument, 'customer_email': customer_email,
                                         'message': message, 'answer': answer})
        plain_message = strip_tags(html_message)
        to = from_email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return html_message
