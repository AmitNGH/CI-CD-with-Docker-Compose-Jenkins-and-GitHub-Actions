from selenium import webdriver


def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    score = int(driver.find_element(by="id", value="score").text)

    return 1 < score < 1000


def main_function():
    if test_scores_service("http://localhost:5000"):
        exit(0)

    exit(-1)


main_function()