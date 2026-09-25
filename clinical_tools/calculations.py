"""Validated clinical calculations.

These functions provide arithmetic only. Clinical interpretation, contraindications,
and dosing limits must be determined from the relevant clinical context.
"""

def _positive(value: float, name: str) -> float:
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return float(value)


def bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI in kg/m²."""
    weight_kg = _positive(weight_kg, "weight_kg")
    height_m = _positive(height_m, "height_m")
    return weight_kg / (height_m ** 2)


def weight_based_dose(weight_kg: float, dose_mg_per_kg: float) -> float:
    """Return a calculated dose in mg from weight and a prescribed mg/kg factor."""
    weight_kg = _positive(weight_kg, "weight_kg")
    dose_mg_per_kg = _positive(dose_mg_per_kg, "dose_mg_per_kg")
    return weight_kg * dose_mg_per_kg


def cockcroft_gault(
    age_years: float,
    weight_kg: float,
    serum_creatinine_mg_dl: float,
    *,
    female: bool = False,
) -> float:
    """Estimate creatinine clearance (mL/min) using Cockcroft–Gault."""
    age_years = _positive(age_years, "age_years")
    weight_kg = _positive(weight_kg, "weight_kg")
    serum_creatinine_mg_dl = _positive(
        serum_creatinine_mg_dl, "serum_creatinine_mg_dl"
    )

    result = ((140 - age_years) * weight_kg) / (72 * serum_creatinine_mg_dl)
    return result * 0.85 if female else result
