import string
import random

from model.project import Project
def test_login(app,db):

    app.project.open_project_page()
    get_old_list = db.get_project_id()
    app.project.create_new_project(Project(name=random_string("name",10), description=random_string("description",10)))
    get_new_list = db.get_project_id()

    assert len(get_old_list)+1 == len(get_new_list)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])
