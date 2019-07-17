# django-contact-form
Django Contact Form with Google Recaptcha v3 - integration.

## How it looks:
![contact-form-vid-presentation](https://user-images.githubusercontent.com/40589021/61354422-6d991d80-a872-11e9-8e51-d88881a23523.gif)

## Install

Easy install with pip:
```python
pip install django-contact-recaptcha-v3
```


Quick start
-----------

1. Add "contact-form" to your INSTALLED_APPS setting like this::

```python
	 INSTALLED_APPS = [
        	...
        	'contact-form',
	]
`````

2. Include the polls URLconf in your project urls.py like this::

```python
	path('', include('contact-form.urls')),
`````

3. Run `python manage.py migrate` to create the form models.

4. For finding Templates add this line into TEMPLATES in settings.py::

```python
	TEMPLATES = [
             {
              ...
             'DIRS': [os.path.join(BASE_DIR, 'templates')],
              ...
             }
         ]
````

5. To setup Email and Recaptcha just paste this code with your keys in settings.py::


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

6. Visit http://127.0.0.1:8000/contact/ to check the contact-form.
