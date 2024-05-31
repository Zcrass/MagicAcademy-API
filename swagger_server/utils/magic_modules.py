import logging
import random

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


GRIMORIO_PROBABILITIES = {
    "Oscuridad": 0.5,
    "Luz": 0.15,
    "Fuego": 0.2,
    "Agua": 0.2,
    "Viento": 0.2,
    "Tierra": 0.2
}

def assing_grimorio():
    grimorios = list(GRIMORIO_PROBABILITIES.keys())
    probabilities = list(GRIMORIO_PROBABILITIES.values())

    assigned_grimorio = random.choices(grimorios, weights=probabilities, k=1)[0]
    logger.info(f"Assigned grimorio: {assigned_grimorio}")
    return assigned_grimorio