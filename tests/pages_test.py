"""This test the homepage"""


def test_request_home(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200


def test_request_cicd(client):
    """This makes the CICD page"""
    response = client.get("/cicd")
    assert response.status_code == 200


def test_request_docker(client):
    """This makes the Docker page"""
    response = client.get("/docker")
    assert response.status_code == 200


def test_request_flask(client):
    """This makes the Docker page"""
    response = client.get("/flask")
    assert response.status_code == 200


def test_request_git(client):
    """This makes the Github page"""
    response = client.get("/git")
    assert response.status_code == 200

def test_request_git(client):
    """This makes the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200

def test_request_git(client):
    """This makes the Pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200

def test_request_git(client):
    """This makes the OOP page"""
    response = client.get("/oop")
    assert response.status_code == 200

def test_request_git(client):
    """This makes the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This checks for a non-hosted page"""
    response = client.get("/page5")
    assert response.status_code == 404
