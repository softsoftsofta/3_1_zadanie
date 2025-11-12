from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняем обязательные поля с уникальными селекторами
        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Введите имя']")
        first_name.send_keys("Иван")

        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Введите фамилию']")
        last_name.send_keys("Петров")

        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Введите Email']")
        email.send_keys("test@example.com")

        # отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # проверяем, что смогли зарегистрироваться
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        print(f"Тест на странице {link} прошел успешно!")
        return True

    except Exception as e:
        print(f"Тест на странице {link} упал с ошибкой: {type(e).__name__}")
        return False
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


print("=" * 50)
print("ТЕСТИРОВАНИЕ ФОРМЫ РЕГИСТРАЦИИ")
print("=" * 50)

# тестируем на первой странице (должен пройти)
print("\n1. Тестируем страницу registration1.html:")
result1 = test_registration("http://suninjuly.github.io/registration1.html")
if result1:
    print("ТЕСТ ПРОЙДЕН УСПЕШНО")
else:
    print("ТЕСТ НЕ ПРОЙДЕН")

# тестируем на новой странице (должен упасть)
print("\n2. Тестируем страницу registration2.html:")
result2 = test_registration("https://suninjuly.github.io/registration2.html")
if result2:
    print("ТЕСТ ПРОЙДЕН УСПЕШНО")
else:
    print("ТЕСТ УПАЛ (это ожидаемое поведение - обнаружен баг!)")

print("\n" + "=" * 50)
if result1 and not result2:
    print("ВСЕ ТЕСТЫ СРАБОТАЛИ КОРРЕКТНО!")
    print("• registration1.html: тест прошел ✓")
    print("• registration2.html: тест упал ✓ (обнаружен баг)")
else:
    print("Что-то пошло не так")
print("=" * 50)