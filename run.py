from ui.ui import run
from model import Model

try:
    model = Model("model.keras")
except: 
    model = Model()
run(model=model)