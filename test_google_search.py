from selene.support.shared import browser
from selene import be, have

def test_google_should_find_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_anything(open_browser):
    search_string = 'sdfhasyfafjehfiohKLFW'
    browser.element('[name="q"]').should(be.blank).type(search_string).press_enter()
    browser.element('[id="rcnt"]').should(have.text(f'Your search - {search_string} - did not match any documents'))

