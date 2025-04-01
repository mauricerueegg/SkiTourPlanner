# Zelle 1: Imports & Setup
import random
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Parameter
NUM_IDS = 10
ID_RANGE = (1, 3000)

# Zufällige URLs generieren
random_ids = random.sample(range(ID_RANGE[0], ID_RANGE[1] + 1), NUM_IDS)
route_urls = [f"https://www.skitourenguru.ch/track-view?area=ch&id={i}" for i in random_ids]

# Webdriver konfigurieren
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Zelle 2: Extraktionsfunktion
def extract_tour_data(driver, url):
    driver.get(url)
    time.sleep(2)  # Wartezeit fürs Laden

    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = {"url": url}

    def get_value(label):
        for row in soup.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) >= 2 and cols[0].get_text(strip=True) == label:
                return cols[1].get_text(strip=True)
        return None

    result["Gipfel"] = get_value("Gipfel")
    result["Start"] = get_value("Start")
    result["Höhendifferenz"] = get_value("Höhendifferenz")
    result["Routenlänge"] = get_value("Routenlänge")
    result["Aufstiegszeit"] = get_value("Aufstiegszeit")
    result["Schwierigkeitsgrad"] = get_value("Schwierigkeitsgrad")

    # Schnee-Wert extrahieren
    schnee_label = soup.find("td", string=lambda text: text and "Schnee" in text)
    schnee_element = schnee_label.find_next_sibling("td") if schnee_label else None
    result["Schnee"] = schnee_element.get_text(strip=True) if schnee_element else None

    lawine = soup.select_one("span.v-chip__content")
    result["Lawinenrisiko"] = lawine.get_text(strip=True) if lawine else None

    return result

# Zelle 3: Scraping & Speichern
all_tours = []
with open("skitouren_daten.jl", "w", encoding="utf-8") as f:
    for url in route_urls:
        print(f"Scraping: {url}")
        try:
            tour_data = extract_tour_data(driver, url)
            all_tours.append(tour_data)
            f.write(json.dumps(tour_data, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"❌ Fehler bei {url}: {e}")
        time.sleep(1)

print("✅ Alle Daten erfolgreich gespeichert in skitouren_daten.jl")

# Webdriver schließen
driver.quit()