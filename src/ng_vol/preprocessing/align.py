# Aligns all datasets to a daily panel
def build_daily_panel(prices, curve, storage, fundamentals, weather):
    idx = prices.index
    return (
        prices
        .join(curve.reindex(idx).ffill())
        .join(storage.reindex(idx).ffill())
        .join(fundamentals.reindex(idx).ffill())
        .join(weather.reindex(idx).ffill())
        .dropna()
    )
