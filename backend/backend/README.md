##  DJANGO TDD
Using pytest to run django tests

### Settings
- Create a test settings alongside the main settings where we will define 
the database to set up on so we do not have to mock up values
Also change the email backend to be inmemory so that it does not send  emails to active receipients
- Create a .coveragerc file and include the files that should not be included in checking for coverage because we wont test them.

- Create a pytest.ini next to manage.py to have terminal commands that will be appended to pytest upon running

### installations
install 
    pytest, 
    pytest-django 
    git+git://github.com/mverteuil/pytest-ipdb.git
    pytest-cov
    mixer
- pytest-ipdb is used to deal with actual db in memory other than mock ups
- pytest-cov shows coverage
- mixer - creates seed to the database based on your definition of models without manually adding values


### Tests
- in the app create tests folder and in it create files starting with test_ then followed by the file name you are testing, eg test_model.py

- import mixer from mixer.backend.django 
 mixer calls .save method when run which pytest rejects since tests should not communicate to any external service and db is an external service
 - so to allow for this,  include
 pytestmark = pytest.mark.django_db

