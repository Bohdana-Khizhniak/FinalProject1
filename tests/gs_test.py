from time import sleep
from gs_testing.Model import gs

# @allure.title('Тест для перевірки головної сторінки')
def test_main_page():
    # with allure.step('Відкриваємо сайт Gstore'):
    gs.open()
    assert gs.should_be('https://gstore.ua/')
    sleep(1)

def test_authorization():
    # with allure.step('Відкриваємо сторінку авторизації'):
    gs.authorization('khizhniak.bohdana@gmail.com', 'dana310785')
    assert gs.should_be('bohdana khizhniak')
    sleep(1)
def test_serch():
    # with allure.step('Перевірка пошуку'):
    gs.serch('iphone 13')
    assert gs.should_be('iphone 13')
    sleep(1)
def test_basket():
    gs.basket()
    sleep(5)

def test_chenge_data():
    gs.data_change('Хижняк Богдана', '380981111111')
    assert gs.should_be('хижняк богдана')

def test_bad_authorization():
    gs.invalid_authorization('khizhniak.bohdana@g.com', 'dana310785')
    assert gs.should_be('Неправильна комбінація е-пошти та паролю')
