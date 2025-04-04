import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def generate_route_urls(num_ids, id_range):
    random_ids = random.sample(range(id_range[0], id_range[1] + 1), num_ids)
    return [f"https://www.skitourenguru.ch/track-view?area=ch&id={i}" for i in random_ids]

def setup_driver():
    options = Options()
    options.headless = False
    return webdriver.Chrome(options=options)
