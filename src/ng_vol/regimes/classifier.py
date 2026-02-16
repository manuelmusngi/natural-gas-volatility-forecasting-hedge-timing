def classify_vol_regime(series):
    q40, q70 = series.quantile([0.4, 0.7])
    return series.apply(
        lambda x: "low" if x <= q40 else "medium" if x <= q70 else "high"
    )
