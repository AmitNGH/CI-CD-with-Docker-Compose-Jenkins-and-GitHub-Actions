from selenium import webdriver
import sys


def test_scores_service(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    score = int(driver.find_element(by="id", value="score").text)

    driver.quit()

    return 1 < score < 1000


def main_function(host, port):
    if test_scores_service(f"http://{host}:{port}"):
        exit(0)

    exit(1)



if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]

    main_function(host, port)