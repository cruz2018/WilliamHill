import unittest from selenium import webdriver import time

class WhJoinButton(unittest.TestCase):

@classmethod
def setUpClass(cls):
    cls.driver = webdriver.Firefox()
    url_en = "https://sports.williamhill.com/betting/en-gb"
    cls.driver.get(url_en)
    cls.driver.implicitly_wait(50)
    print('THE USER HAD OPENED http://sports.williamhill.com/betting/en-gb  ')

def test_join_btn(self):
    print(' 1. HE ASSERTS PRESENCE OF JOIN BUTTON  ')
    self.joinBtnExist()

    language_pairs = [('de','Anmelden'), ('ja', '登録'), ('el', 'Εγγραφή')]
    i = 0
    n = len(language_pairs)
    while (i < n):
        pair = language_pairs[i]
        short_text = str(pair[0])
        text = str(pair[1])
        self.switchLanguageAndAssertTranslation(short_text, text)
        i = i + 1

def switchLanguageAndAssertTranslation(self, language, label):
    print(' 2. HE SWITCHES THE LANGUAGE TO ', language)
    print(' 3. AND HE SEES JOIN BUTTON')
    print(' 4. HE ASSERTS THE JOIN BUTTON LABEL IS TRANSLATED AS: ',label)
    self.expandLanguageList()
    self.selectLanguage(language)
    self.joinBtnExist()
    self.joinBtnLabelTranslatedTo(label)


def joinBtnLabelTranslatedTo(self, translation):
    join_new = self.getJoinBtnLabel()
    self.driver.implicitly_wait(10)
    #self.assertTrue(join_new == translation)
    self.assertEqual(join_new,translation)

def getJoinBtnLabel(self):
    return self.driver.find_element_by_id('joinLink').text

def selectLanguage(self, language):
    language_selector = self.driver.find_element_by_id(language)
    self.driver.implicitly_wait(10)
    self.elemExists(language_selector)
    self.clickElem(language_selector)
    self.driver.implicitly_wait(50)

def expandLanguageList(self):
    language_list = self.driver.find_element_by_class_name('js-language-button')
    self.driver.implicitly_wait(10)
    self.elemExists(language_list)
    self.clickElem(language_list)
    self.driver.implicitly_wait(50)

def joinBtnExist(self):
    join = self.driver.find_element_by_id('joinLink')
    self.assertTrue(join.is_displayed())

def elemExists(self, elem):
    self.assertTrue(elem.is_displayed())

def clickElem(self, elem):
    elem.click()

def tearDown(cls):
    file = './screenshots/' + 'WhCookieTest_on_exit' + str(int(round(time.time() * 1000))) + '.png'
    cls.driver.get_screenshot_as_file(file)
    cls.driver.quit()
    print('TEST PASSED')

if __name__ == '__main__':
    unittest.main()