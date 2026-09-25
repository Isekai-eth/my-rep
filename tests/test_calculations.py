import pytest

from clinical_tools import bmi, cockcroft_gault, weight_based_dose


def test_bmi():
    assert bmi(80, 1.75) == pytest.approx(26.1224, rel=1e-4)


def test_weight_based_dose():
    assert weight_based_dose(24, 15) == pytest.approx(360)


def test_cockcroft_gault():
    assert cockcroft_gault(26, 80, 1.02) == pytest.approx(124.18, rel=1e-3)


@pytest.mark.parametrize(
    ("fn", "args"),
    [
        (bmi, (0, 1.75)),
        (weight_based_dose, (24, 0)),
        (cockcroft_gault, (26, 80, 0)),
    ],
)
def test_rejects_non_positive_inputs(fn, args):
    with pytest.raises(ValueError):
        fn(*args)
