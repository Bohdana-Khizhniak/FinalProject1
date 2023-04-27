from time import sleep
from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')

class gstore:
    def __init__(self):
        self.base_url = 'https://gstore.ua/'

    def open(self):
        browser.open(self.base_url)
        browser.driver.maximize_window()
        sleep(5)
        return self

    def authorization(self, login, pas):
        browser.element('body > div.container > div.header > div > div.header__middle > div > div > div.header__column.header__column--right > div:nth-child(5) > div > div > a > svg > use').click()
        sleep(1)
        browser.element('#login_form_id > dl > dd:nth-child(2) > input').type(login).press_tab()
        sleep(2)
        browser.element('#login_form_id > dl > dd:nth-child(4) > input').type(pas).press_tab()
        sleep(1)
        browser.element('#login_form_id > dl > dd.form-item.__submit > span.btn.__special > input').press_enter()
        sleep(5)
        return self

    def serch(self, st):
        browser.element('[placeholder="пошук товарів"]').type(st)
        sleep(1)
        browser.element('[placeholder="пошук товарів"]').press_enter()
        return self

    def basket(self):
        browser.all('[class="catalog-grid__item"]')[0].element('a').click()
        sleep(1)
        browser.element('#j-buy-button-widget-12335 > span').click()
        sleep(1)
        browser.element('[class="icon icon--plus"]').click()
        sleep(1)
        browser.element('[class="icon icon--minus"]').click()
        sleep(1)
        browser.element('[class="icon icon--minus"]').click()
        sleep(2)
        browser.driver.switch_to.alert.accept()
        return self

    def data_change(self, usname, tel):
        browser.element('[class="userbar__button"]').click()
        browser.element('[class="userbar__menu-link"]').click()
        browser.element('#main > div > div > div > div > section > div > form > dl > dd:nth-child(2) > input').type(usname).press_tab()
        browser.element('[class ="field j-phone j-phone-masked"]').type(tel).press_tab()
        browser.element('#current_profile-pass').type('dana310785').press_tab()
        browser.element('#profile-pass').type('dana310785').press_tab()
        browser.element('#profile-pass2').type('dana310785').press_tab()
        browser.element('#main > div > div > div > div > section > div > form > dl > dd.form-item.__submit > span > input').click()
        return self

    def invalid_authorization(self, login, pas):
        browser.element('[class="userbar__button"]').click()
        browser.element('[class ="userbar__menu-link j-widget-ajax-link"]').click()
        browser.element('body > div.container > div.header > div > div.header__middle > div > div > div.header__column.header__column--right > div:nth-child(5) > div > div > a > svg > use').click()
        browser.element('#login_form_id > dl > dd:nth-child(2) > input').type(login).press_tab()
        sleep(2)
        browser.element('#login_form_id > dl > dd:nth-child(4) > input').type(pas).press_tab()
        sleep(1)
        browser.element('#login_form_id > dl > dd.form-item.__submit > span.btn.__special > input').press_enter()
        sleep(5)
        assert browser.element('#login_form_id > div > div').should(have.exact_text('Неправильна комбінація е-пошти та паролю'))
        return self
    def should_be(self, st):
        p_count = browser.driver.page_source.lower().count(st)
        if p_count > 0:
            print('Ok')
        else:
            print('Error')
        return self
