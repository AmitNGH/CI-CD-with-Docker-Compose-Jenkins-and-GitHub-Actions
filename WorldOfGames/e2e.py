from selenium import webdriver


def test_scores_service(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    score = int(driver.find_element(by="id", value="score").text)

    return 1 < score < 1000


def main_function(host, port):
    if test_scores_service(f"http://${host}:port"):
        exit(0)

    exit(-1)
