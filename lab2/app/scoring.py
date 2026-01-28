def score_apartment(size_m2: float, rooms: int, distance_center_km: float) -> float:
    score = 0.0
    score += min(size_m2, 100) * 0.5
    score += rooms * 5
    score += max(0, 30 - distance_center_km) * 1.5
    return round(score, 2)

