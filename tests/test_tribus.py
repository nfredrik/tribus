from tribus import approx_pi


def test_pi():
    assert 22 / 7 == approx_pi()
