def recommend_size(foot_length, product):

    base = foot_length + 0.7  # marge confort

    adjustment = 0

    if product.get("runs_small"):
        adjustment += 0.5
    if product.get("runs_large"):
        adjustment -= 0.5

    final_size = round(base + adjustment)

    confidence = 80

    if product.get("runs_small") or product.get("runs_large"):
        confidence -= 10

    return final_size, confidence
