class WhCookie(unittest.TestCase):

@classmethod
def setUpClass(cls):
    cls.driver = webdriver.Firefox()
    # Deleting all cookies, making sure cookie 'cdb' is not present initially
    cls.driver.delete_all_cookies()
    cls.cookies_name = 'cdb'
    cls.url_es = "https://sports.williamhill.es/betting/es-es"
    cls.url_en = "https://sports.williamhill.com/betting/en-gb"

def test_cookies_addedES(self):
    ## There is an issue with the English local the cookie popup does not appear, therefore for the purpose of        implementation is used the Spanish locale
    print('There is an issue with the English local, the popup does not appear, therefore for the purpose of implementation is used DE local')
    self.url = self.url_es
    self.cookie_successfully_added(self.cookies_name, self.url)

def loadPage(self, url):
    self.driver.get(url)
    self.driver.implicitly_wait(15)

def cookie_successfully_added(self, cookies_name,url):

    ### 1. OPEN "http://sports.williamhill.com/betting/en-gb' ###
    print(' 1. OPEN http://sports.williamhill.com/betting/en-gb  ')
    self.loadPage(url)

    ### 2. ASSERT PRESENCE OF COOKIE NOTICE POP-UP ###
    print(' 2. ASSERT PRESENCE OF COOKIE NOTICE POP-UP  ')
    popup = self.driver.find_element_by_class_name('cookie-disclaimer')
    self.elemExists(popup)

    print('       The cookie notice pop-up is displayed: ', popup.is_displayed())
    button = self.driver.find_element_by_class_name("cookie-disclaimer__button")
    self.elemExists(button)
    self.cookieDoesntExist(self.getCookie(cookies_name))

    ### 3. CLOSE COOKIE NOTICE  ###
    print(' 3. CLOSE COOKIE NOTICE ')
    self.clickElem(button)

    ### 4. ASSERT PRESENCE OF CDB COOKIE  ###
    print(' 4. ASSERT PRESENCE OF CDB COOKIE ')
    cdb_cookie = self.getCookie(cookies_name)
    print('       The new cookie added is: ', cdb_cookie)
    self.cookieExists(cdb_cookie)

def elemExists(self, elem):
    self.assertTrue(elem.is_displayed())

def clickElem(self, elem):
    elem.click()

def getCookie(self, cookie):
    return self.driver.get_cookie(cookie)

def cookieExists(self, cookie):
    self.assertFalse(cookie is None)

def cookieDoesntExist(self, cookie):
    self.assertTrue(cookie is None)

def tearDown(cls):
    file = './screenshots/' + 'WhCookieTest_on_exit' + str(int(round(time.time() * 1000))) +'.png'
    cls.driver.get_screenshot_as_file(file)
    cls.driver.quit()
    print('TEST PASSED')

if __name__ == '__main__':
    unittest.main()