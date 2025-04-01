# Zelle 1: Imports & Setup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time


# Zelle 2: Webdriver konfigurieren (Headless Chrome)
options = Options()
options.headless = True  # Setze auf False, wenn du den Browser sehen willst
driver = webdriver.Chrome(options=options)



route_urls = [
    f"https://www.skitourenguru.ch/track-view?area=ch&id={i}"
    for i in range(1, 10)
]

# Zelle 4: Extraktionsfunktion mit BeautifulSoup
def extract_tour_data(driver, url):
    driver.get(url)
    time.sleep(3)  # gib der Seite etwas Zeit zum Laden

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

    # Dynamischen Schnee-Wert extrahieren
    schnee_label = soup.find("td", string=lambda text: text and "Schnee" in text)
    if schnee_label:
        schnee_element = schnee_label.find_next_sibling("td")
        result["Schnee"] = schnee_element.get_text(strip=True) if schnee_element else None
    else:
        result["Schnee"] = None

    result["Schwierigkeitsgrad"] = get_value("Schwierigkeitsgrad")

    lawine = soup.select_one("span.v-chip__content")
    result["Lawinenrisiko"] = lawine.get_text(strip=True) if lawine else None

    return result


# Zelle 5: Scraping ausführen
all_tours = []
for url in route_urls:
    print(f"Scraping: {url}")
    try:
        tour_data = extract_tour_data(driver, url)
        all_tours.append(tour_data)
    except Exception as e:
        print(f"Fehler bei {url}: {e}")
    time.sleep(1)


    # Zelle 6: Speichere die Daten
with open("skitouren_daten.json", "w", encoding="utf-8") as f:
    json.dump(all_tours, f, ensure_ascii=False, indent=2)

print("✅ Alle Daten erfolgreich gespeichert.")



# Zelle 7: Webdriver schließen
driver.quit()