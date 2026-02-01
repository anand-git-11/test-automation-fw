import pytest
import requests
import mysql.connector
from mysql.connector import Error
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_user_api_and_exp_data():
    # User data can be defined in json file or stored in database
    # return list of data. Each list element is the data to be 
    # simulated(written to api layer)
    # Each list element has 4 keys for each user input
    # - input data for api layer
    # - expected es data
    # - expected db data
    # - expected api data
    return user_api_and_exp_data

PARAMS = get_user_api_and_exp_data()

def pytest_generate_tests(metafunc):
    if "input_param" in metafunc.fixturenames:
        metafunc.parametrize(
            "input_param",
            PARAMS,
            scope="session"
        )

@pytest.fixture(scope="session")
def server_connection():
    print("Establishing connection to api layer")
    conn = connect_and_authorize()
    yield conn
    print("Closing connection to api layer")
    conn.close()

@pytest.fixture(scope="session", autouse=True)
def setup_for_input(input_param, server_connection):
    print(f"\n=== SETUP for input {input_param} ===")
    prepare_environment(server_connection, input_param)

    yield  

    print(f"\n=== TEARDOWN for input {input_param} ===")
    cleanup_environment(server_connection, input_param)

def connect_and_authorize():
    print("Connecting to server...")
    # e.g. login(), get token, open session
    return ServerClient(token="abc123")

def prepare_environment(conn, param):
    base_url = "http://localhost:9200"
    res = requests.put(urljoin(base_url, path), header, data=param.input_data)

def cleanup_environment(conn, param):
    print(f"Cleaning up environment for {param}")


@pytest.fixture(scope='session')
def get_db_handle():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="test_db"
        )
    except Exception as e:
        print(f'Exception {e} in get_db_handle ')
        con = False
    yield con
    try:
        con.close()
    except Exception as e:
        print(f'Exception {e} in get_db_handle ')


@pytest.fixture(scope='session')
def get_es_handle():
    ES_HOST = "http://localhost:9200"
    USERNAME = "elastic"
    PASSWORD = "password"
    yield client
    client.close()

@pytest.fixture(scope='session')
def get_api_handle():
    base_url = "http://localhost:9200"
    data = [("username", "123"), ("password", "pass")]
    res = requests.post(urljoin(base_url, path), header, data)
    yield res

@pytest.fixture(scope='session')
def get_browser_driver_handle():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
