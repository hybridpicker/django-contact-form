# django-contact-form
Django Contact Form with Google Recaptcha v3 - integration.

# How it looks:
![contact_form_vid](https://user-images.githubusercontent.com/40589021/61306132-544d8e00-a7ec-11e9-8e0f-5a7cfeb29f68.gif)

# Install

Easy install with pip:
```python
pip install django-contact-recaptcha-v3
```

Registering in **settings.py***

```python
INSTALLED_APPS = [
        	...
        	'contact-form',
	]
```

# Instructions:

For finding Templates add this line into TEMPLATES in **settings.py**:
```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

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
