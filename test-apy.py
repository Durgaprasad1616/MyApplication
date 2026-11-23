from app import welcome

def test_welcome():
    assert welcome() == "Welcome to Azure DevOps CI/CD Pipeline!"
