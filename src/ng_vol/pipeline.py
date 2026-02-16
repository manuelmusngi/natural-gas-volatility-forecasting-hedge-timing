# Single orchestration entry point

from ng_vol.io.ingestion import *
from ng_vol.preprocessing.align import build_daily_panel
from ng_vol.features.volatility import realized_vol
from ng_vol.models.har import HARModel

def run_pipeline():
    prices = load_prices()
    curve = load_curve()
    storage = load_storage()
    fundamentals = load_fundamentals()
    weather = load_weather()

    panel = build_daily_panel(prices, curve, storage, fundamentals, weather)
    panel["rv_10d"] = realized_vol(panel["spot"], 10)

    model = HARModel().fit(panel[["rv_10d"]], panel["rv_10d"].shift(-10))
    return model
