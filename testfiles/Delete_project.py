import random
import string
from random import choice
from model.project import Project
#
def test_delete_project(app,db):
    app.project.open_project_page()

    get_id_list = db.get_project_id()
    get_old_list = db.get_project_id()
    if len(get_id_list) == 0:
        app.project.create_new_project(
            Project(name=random_string("name", 10), description=random_string("description", 10)))
        app.project.open_project_page()
        get_id_list = db.get_project_id()
        id = choice(get_id_list).id
        app.project.delete_selected_project(id)

        new_list = db.get_project_id()
        assert len(get_old_list) - 1 == len(new_list)
    else:
        id = choice(get_id_list).id
        app.project.delete_selected_project(id)
        new_list = db.get_project_id()
        assert len(get_old_list) - 1 == len(new_list)





def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])
