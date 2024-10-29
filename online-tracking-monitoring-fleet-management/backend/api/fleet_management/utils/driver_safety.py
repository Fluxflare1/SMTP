from .models import DriverSafetyScore

def calculate_driver_safety_score(driver_id, speeding, braking, acceleration):
    SPEEDING_WEIGHT = 0.4
    BRAKING_WEIGHT = 0.3
    ACCELERATION_WEIGHT = 0.3

    score = (
        SPEEDING_WEIGHT * (1 - speeding) +
        BRAKING_WEIGHT * (1 - braking) +
        ACCELERATION_WEIGHT * (1 - acceleration)
    ) * 100  # Normalize to 0-100 scale

    DriverSafetyScore.objects.create(driver_id=driver_id, score=score)
    return score
