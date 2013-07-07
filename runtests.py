import os, sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG = True,
                   DATABASES = {
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                           'NAME': os.path.join(DIRNAME, 'reformation-test.db'),
                       }
                   },
                   INSTALLED_APPS = ('django.contrib.contenttypes',
                                     'django.contrib.sessions',
                                     'reformation',))

from django.test.utils import setup_test_environment, get_runner, teardown_test_environment

setup_test_environment()
runner = get_runner(settings)()

failures = runner.run_tests(['reformation',], verbosity=1)

# teardown_test_environment()

if failures:
    sys.exit(failures)
