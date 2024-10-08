import pytest
import allure
import requests


@allure.title("Test Get Request-RestFull BOOKER Project#1")
@allure.description("TC#1 Verify that Get Request with valid ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Aditya Suman")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/2"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    print(response_data.json())
    assert response_data.status_code == 200

@allure.title("Test Get Request-RestFull BOOKER Project#1")
@allure.description("TC#2 Verify that Get Request with invalid ID ")
@pytest.mark.smoke
def testt_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/-2"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404

@allure.title("Test Get Request-RestFull BOOKER Project#1")
@allure.description("TC#3 Verify that Get Request with invalid ID ")
@pytest.mark.smoke
def testt_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/784512"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404






