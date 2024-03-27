import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)


    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Temukan tombol login di dalam menu
        # button_login = self.driver.find_element(By.ID, "login")
        # button_login.click()

        time.sleep(2)

        # Mencari elemen input username dan password menggunakan ID
        # username_input = self.driver.find_element(By.ID, "username")
        # password_input = self.driver.find_element(By.ID, "password")

        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        # button = self.driver.find_element(By.ID, "btnLogin")

        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def test_login(self):
        # Membuka halaman web
        # self.driver.get("http://127.0.0.1:5501/")
        self.driver.get("https://intermoni.my.id/")

        time.sleep(2)

        # Tunggu hingga navbar-burger menjadi klikable
        # navbar_burger = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "navbar-burger")))
        # navbar_burger.click()

        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signIn.html']")
        button.click()

        # time.sleep(2)

        # Login dengan username dan password tertentu
        # self.login("dimas", "secret")
        self.login("dimasmhs@gmail.com", "fghjkliow")
        self.detail_magang()

#list_page
    def detail_magang(self):
        # Temukan tombol login di dalam menu
        # button_login = self.driver.find_element(By.ID, "login")
        # button_login.click()

        time.sleep(2)

        # Mencari elemen input username dan password menggunakan ID
        # username_input = self.driver.find_element(By.ID, "username")
        # password_input = self.driver.find_element(By.ID, "password")

        button = self.driver.find_element(By.XPATH, "//a[@href='cariInternship.html']")
        button.click()

        time.sleep(2)

        

if __name__ == "__main__":
    unittest.main()