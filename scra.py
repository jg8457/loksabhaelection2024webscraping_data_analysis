from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_type_1(driver):
    results = []
    try:
        table_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        rows = table_body.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) > 6:
                constituency = cells[0].text
                candidate = cells[2].text
                party = cells[3].text
                margin = cells[6].text
                second_candidate = cells[4].text
                second_party = cells[5].text
                previous_winner = cells[7].text
                previous_party = cells[8].text

                results.append({
                    'constituency': constituency,
                    'candidate': candidate,
                    'party': party,
                    'winning_margin': margin,
                    'second_candidate': second_candidate,
                    'second_party': second_party,
                    'previous_winner': previous_winner,
                    'previous_party': previous_party
                })
    except TimeoutException:
        print("TimeoutException: Unable to locate the table body for type 1 structure.")
    return results

def scrape_type_2(driver):
    results = []
    try:
        table_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        rows = table_body.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) > 4:
                constituency = cells[0].text
                candidate = cells[1].text
                party = cells[2].text
                margin = cells[3].text
                second_candidate = cells[4].text
                second_party = cells[5].text
                previous_winner = cells[6].text
                previous_party = cells[7].text

                results.append({
                    'constituency': constituency,
                    'candidate': candidate,
                    'party': party,
                    'winning_margin': margin,
                    'second_candidate': second_candidate,
                    'second_party': second_party,
                    'previous_winner': previous_winner,
                    'previous_party': previous_party
                })
    except TimeoutException:
        print("TimeoutException: Unable to locate the table body for type 2 structure.")
    return results

url_function_pairs = [
    ('https://results.eci.gov.in/pcresultgenjune2024/statewiseS241.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS041.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS061.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU011.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS021.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS021.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS031.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU021.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS261.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU031.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS051.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU061.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU091.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS111.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS101.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS271.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS271.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU081.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS081.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS081.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS121.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU051.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS131.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS141.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS151.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS161.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS171.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS181.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU071.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS253.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS281.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS291.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS221.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS211.htm',scrape_type_2),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS201.htm',scrape_type_1),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS191.htm',scrape_type_2)
]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

all_results = []

for url, scrape_function in url_function_pairs:
    driver.get(url)
    state_results = scrape_function(driver)
    all_results.extend(state_results)

driver.quit()

df = pd.DataFrame(all_results)
df.to_csv('lok_sabha_election_results_2024.csv', index=False)

print("Data scraping complete and saved to lok_sabha_election_results_2024.csv")




