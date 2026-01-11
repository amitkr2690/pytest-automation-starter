import pytest
app_version=""
def pytest_addoption(parser):
    parser.addini("version", "Application version")

def pytest_configure(config):
    global app_version
    app_version=int(config.getini("version"))