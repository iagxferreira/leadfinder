from leadfinder.signals import lead_signal


def test_no_website():
    assert lead_signal(None) == "no_website"


def test_http_only():
    assert lead_signal("http://example.com") == "no_https"


def test_has_website():
    assert lead_signal("https://example.com") == "has_website"
