import selenium


def test_scores_service(url):
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    score = int(driver.find_element(by="id", value="score").text)

    return 1 < score < 1000


def main_function():
    if test_scores_service("localhost:5000"):
        exit(0)

    exit(-1)
