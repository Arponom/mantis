from fixtura.Project import projecthelp
from fixtura.Session import aut_helper
from selenium import webdriver

class testing:

    def __init__(self, browser,base_url):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Error" %browser)

        self.auth = aut_helper(self)
        self.base_url = base_url
        self.project = projecthelp(self)
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def go_on_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroyer(self):
        wd = self.wd
        wd.quit()

