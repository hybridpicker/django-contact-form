# django-contact-form
Django Contact Form with Google Recaptcha v3 - integration.

# Instructions:

To setup Email and Recaptcha just paste this code with your keys in settings.py:

```python
# Email Settings:
EMAIL_HOST = 'smtp.foo.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'foo@gfoo.com'
EMAIL_HOST_PASSWORD = 'swordfish'

# Recaptcha Key's #
RECAPTCHA_SITE_KEY = ""
RECAPTCHA_SECRET_KEY = ""
```

Finally copy your Site Key into the recaptcha script in **contact/email.html**:

```html
<script src='https://www.google.com/recaptcha/api.js?render=RECAPTCHA_SITE_KEY'></script>
```
