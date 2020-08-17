
from selenium import webdriver 


class CheckoutFlow:
    

    def __init__(self,driver):
        self.driver = driver


    def setup(self,base_url):
        self.driver.get(base_url)

    def signIn(self,hello_sign_in):
        self.driver.find_element_by_xpath(hello_sign_in).click()

    def signInPage(self, signInInputXpathData , signInFieldsData ,buttonXpaths ):
        for i in range(len(signInInputXpathData)):
            self.driver.find_element_by_id(signInInputXpathData[i]).send_keys(signInFieldsData[i])
            self.driver.find_element_by_xpath(buttonXpaths[i]).click()
            print ("signed in")

    def searchItem(self,searchInput ,search_button ,search_box):
        self.driver.find_element_by_id(search_box).send_keys(searchInput)
        self.driver.find_element_by_xpath(search_button).click()
    
    def selectItem(self,search_results):
        # driver.find_element_by_partial_link_text(searchLink).click()
        search_list = self.driver.find_element_by_xpath(search_results)
        children = search_list.find_elements_by_xpath("div/div")
        return children
        # childrenLink = children[3].find_element_by_tag_name("a")
        # #time.sleep(1)
        # childrenLink.click()
        

    def buyItem(self, buy_now_button ):
        self.driver.find_element_by_xpath(buy_now_button).click()
    
    def deliveryAddress(self,deliver_address):
        self.driver.find_element_by_xpath(deliver_address).click()
        
    def amazonHome(self,amazon_home):
       self.driver.find_element_by_xpath(amazon_home).click()

    def teardown(self):
        self.driver.quit()
       
        

