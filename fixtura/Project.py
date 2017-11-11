
#
class projecthelp:

    def __init__(self, app):
        self.app = app


    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8443/mantisbt-2.8.0/manage_proj_page.php")

    def delete_selected_project(self, id):
        wd=self.app.wd
        wd.get("http://localhost:8443/mantisbt-2.8.0/manage_proj_edit_page.php?project_id=%s" % id)
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@class='row']/div/div[2]/form/input[4]").click()

    def create_new_project(self, project):
        wd=self.app.wd
        wd.find_element_by_xpath("//div[@class='row']//button[.='создать новый проект']").click()
        wd.find_element_by_xpath("//input[@id='project-name']").click()
        wd.find_element_by_xpath("//input[@id='project-name']").clear()
        wd.find_element_by_xpath("//input[@id='project-name']").send_keys(project.name)
        if not wd.find_element_by_xpath("//select[@id='project-status']//option[3]").is_selected():
            wd.find_element_by_xpath("//select[@id='project-status']//option[3]").click()
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)
        wd.find_element_by_xpath("//form[@id='manage-project-create-form']/div/div[3]/input").click()