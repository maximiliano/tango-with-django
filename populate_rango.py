import os


def populate():
    python_category = add_category('Python', views=128, likes=64)

    add_page(category=python_category,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    add_page(category=python_category,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(category=python_category,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_category = add_category("Django", views=64, likes=32)

    add_page(category=django_category,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(category=django_category,
             title="Django Rocks",
             url="http://www.djangorocks.com/")

    add_page(category=django_category,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/")

    frame_category = add_category("Other Frameworks", views=32, likes=16)

    add_page(category=frame_category,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/")

    add_page(category=frame_category,
             title="Flask",
             url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print("- {0} - {1}".format(str(category), str(page)))


def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title, url=url,
                                      views=views)[0]
    return page


def add_category(name, views, likes):
    category = Category.objects.get_or_create(name=name, views=views,
                                              likes=likes)[0]
    return category

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'tango_with_django.settings')
    from rango.models import Category, Page
    populate()
