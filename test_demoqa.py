import os
from selene import browser, be, have


def test_demo_qa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Vin')
    browser.element('#lastName').should(be.blank).type('Diesel')
    browser.element('#userEmail').should(be.blank).type('mr.diesel@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="7"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--015').click()
    browser.element('#subjectsInput').should(be.blank).type('M')
    browser.all('.subjects-auto-complete__option')[2].click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('person1.jpg'))
    browser.element('#currentAddress').should(be.blank).type('32449 Herzog Heights Suite 572')
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form'))

    browser.element('.table.table-dark.table-striped.table-bordered.table-hover').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Vin Diesel',
            'Student Email mr.diesel@mail.ru',
            'Gender Male',
            'Mobile 9999999999',
            'Date of Birth 15 August,1995',
            'Subjects Computer Science',
            'Hobbies Sports',
            'Picture person1.jpg',
            'Address 32449 Herzog Heights Suite 572',
            'State and City Haryana Panipat'
        )
    )

