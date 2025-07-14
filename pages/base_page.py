from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from data import browser_name
from locators import OVERLAY

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_element(self, locator):
        if browser_name == "Chrome":
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        else:
            target = self.wait.until(EC.element_to_be_clickable(locator))
            click = ActionChains(self.driver)
            click.move_to_element(target).click().perform()

    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def wait_for_overlay_to_disappear(self):
        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located(OVERLAY)
        )

    def fill_input(self, locator, text):
        input_field = self.wait_for_element(locator)
        input_field.send_keys(text)

    def drag_and_drop_element(self, source_element, target_element):
            script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
            self.driver.execute_script(script, source_element, target_element)
