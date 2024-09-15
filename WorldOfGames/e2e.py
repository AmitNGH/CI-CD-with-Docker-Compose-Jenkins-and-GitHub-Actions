from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys
import traceback


def test_scores_service(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Debugging: Print page source
        print("Page source:", driver.page_source)

        # Find the element and retrieve its text
        score_element = driver.find_element(by="id", value="score")
        score_text = score_element.text
        print(f"Score element text: '{score_text}'")

        # Convert score to integer and validate
        score = int(score_text)
        driver.quit()

        print(f"Score: {score}")
        return 1 < score < 1000
    except WebDriverException as e:
        print(f"WebDriverException: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception: {e}")
        traceback.print_exc()
    return False

def main_function(host, port):
    try:
        if test_scores_service(f"http://{host}:{port}"):
            exit(0)
        else:
            exit(1)
    except Exception as e:
        print(f"Main Function Exception: {e}")
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <host> <port>")
        exit(1)

    host = sys.argv[1]
    port = sys.argv[2]

    main_function(host, port)