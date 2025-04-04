from bs4 import BeautifulSoup
import time

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
