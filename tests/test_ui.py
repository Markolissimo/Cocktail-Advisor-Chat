import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from rich.console import Console

console = Console()

def wait_for_server(url, timeout: int=10) -> webdriver.Chrome:
    """Wait for the FastAPI server to start before running Selenium tests.
    Args:
        url (str): URL to check.
        timeout (int): Timeout in seconds.
    Returns:
        webdriver.Chrome: Selenium WebDriver instance.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            return driver
        except WebDriverException:
            time.sleep(1)
    raise RuntimeError("Server did not start in time")

def test_ui() -> None:
    """Test the frontend UI.
    Returns:
        None
    """
    console.rule("[bold cyan]Testing Frontend UI")

    driver = wait_for_server("http://localhost:8000/static/index.html")

    input_field = driver.find_element(By.ID, "userInput")
    send_button = driver.find_element(By.TAG_NAME, "button")

    input_field.send_keys("What is in a Margarita?")
    send_button.click()

    time.sleep(2)
    chat_box = driver.find_element(By.ID, "chatBox")
    assert len(chat_box.text) > 0

    console.print("[green]✅ UI test passed![/green]")
    driver.quit()
