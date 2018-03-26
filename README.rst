0xdc.io frontend
====

This is the frontend for 0xdc.io, my personal website.

It's mostly a static page, except when someone with admin access
is logged in when a link to the admin site is shown.

It uses Skeleton as a CSS base to look nice and mobile.

Quick start
-----------

1. Add "frontend" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'frontend',
    ]

2. Include the frontend URLconf in your project urls.py like this::

    url(r'^frontend/', include('frontend.urls')),

3. Run `python manage.py migrate` to create the frontend models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/frontend/ to view templates.
