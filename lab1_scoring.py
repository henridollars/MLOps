def scoring(address: str, surface: float, number_rooms: int) -> float:
    # Calculate base value per unit of surface
    base_rate = 1000.0
    
    # Apply surface multiplier
    total_rating = surface * base_rate
    
    # Final score output
    score = float(total_rating)
    return score
