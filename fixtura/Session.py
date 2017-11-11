#####
class aut_helper:

    def __init__(self, app):
        self.app = app

    def login_q(self, login_sys, pass_sys):
        wd = self.app.wd
        self.app.go_on_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(login_sys)
        wd.find_element_by_xpath("//form[@id='login-form']/fieldset/input[2]").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(pass_sys)
        wd.find_element_by_xpath("//form[@id='login-form']/fieldset/input[3]").click()

    def logout_q(self):
        wd=self.app.wd
        wd.find_element_by_link_text("administrator").click()
        wd.find_element_by_link_text("выход").click()
#------------------------------------------------------
    def ensure_logout(self):
        wd = self.app.wd
        if len(wd.find_element_by_link_text("ace-icon fa fa-sign-out")) > 0:
            self.logout_q()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, login_syss):
        wd = self.app.wd
        return self.get_logged_user() == login_syss

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("user-info").text

    def ensure_login(self, login_syss, pass_syss):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(login_syss):
                return
            else:
                self.logout_q()
        self.login_q(login_syss, pass_syss)
