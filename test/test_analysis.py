from kornect.analysis import install_pypackages


def test_install_pypackage():
    assert install_pypackages('numpy') == 1, "Unexpected error"
