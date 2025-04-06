
from utils import generate_route_urls, setup_driver
from extractor import extract_tour_data
import json
import time
import os

# Parameter
NUM_IDS = 20
ID_RANGE = (1, 1000)

# Speicherpfad für die Downloads
DOWNLOAD_DIR = "./downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(DOWNLOAD_DIR, "skitouren_daten.jl")

# Zufällige URLs generieren
route_urls = generate_route_urls(NUM_IDS, ID_RANGE)

# Webdriver konfigurieren
driver = setup_driver()

# Scraping & Speichern
all_tours = []
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for url in route_urls:
        print(f"Scraping: {url}")
        try:
            tour_data = extract_tour_data(driver, url)
            all_tours.append(tour_data)
            f.write(json.dumps(tour_data, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"❌ Fehler bei {url}: {e}")
        time.sleep(1)

print(f"✅ Alle Daten erfolgreich gespeichert in {OUTPUT_FILE}")

# Webdriver schließen
driver.quit()
