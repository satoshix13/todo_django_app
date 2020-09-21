from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')


class NewVisitorTest(unittest.TestCase):
    '''test new user'''

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Title', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Add Item', header_text)


        inputbox = self.browser.find_element_by_id('inlineFormInput')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Type Here'
        )
        inputbox.send_keys('test item selenium')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        list_data = self.browser.find_elements_by_tag_name('li')
        self.assertTrue(
            any(row.text == 'test item selenium' for row in list_data)
        )
        # self.assertIn('test item selenium', list_data)

        self.fail('Finish test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')


