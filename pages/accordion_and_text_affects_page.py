from playwright.sync_api import Page 


class Accordion_and_text_affects:

    def __init__(self, page: Page):
        self.page = page
        self.manual_testing_btn = page.locator('//*[@id="manual-testing-accordion"]')
        self.manual_testing_accordion = page.locator('//*[@id="manual-testing-description"]/p')
        self.manual_testing_text = 'Manual testing has for some time been the most popular way to test code. For this method, the tester plays an important role of end user and verifies that all the features of the application work correctly. Manual testing however is on the decline. Companies and developers have realised the efficiency, accuracy and cost savings that is possible by adopting the use of automation testing.'
        
        self.cucumber_BDD_btn = page.locator('//*[@id="cucumber-accordion"]')
        self.cucumber_BDD_accordion = page.locator('//*[@id="cucumber-testing-description"]/p')
        self.cucumber_BDD_text = 'Cucumber (BDD) simplifies the requirement capturing process. Requirements can be captured, broken down and simplified effortlessly; making the captured requirements readable to anyone within the organisation and in turn providing the required details and backbone to develop accurate test cases also known as ‘Feature Files’.'

        self.automation_testing_btn = page.locator('//*[@id="automation-accordion"]')
        self.automation_testing_accordion = page.locator('//*[@id="automation-testing-description"]/p')
        self.automation_text = 'Automation testing has been steadily grown in popularity these past few years thanks to the time/ cost savings and efficiency that it offers. Companies throughout the world have or plan to use automation testing to rapidly speed up their test capabilities. Automation test engineers are in great demand and offer an average salary of £45,000+ (2018). Now is a great time to learn about automation test engineering and this course has been carefully developed to slowly introduce you from the basics, all the way to building advanced frameworks.'

        self.keep_cliking_btn = page.locator('//*[@id="click-accordion"]')
        self.keep_cliking_accordion = page.locator('//*[@id="timeout"]')
        self.keep_cliking_text = 'This text has appeared after 5 seconds!'

        self.loading = page.locator(' //*[@id="hidden-text"]')
       
       
    def check_manual_testing_text_appear(self, element, text) -> None:
        element.wait_for(state="visible")
        assert element.text_content() == text
