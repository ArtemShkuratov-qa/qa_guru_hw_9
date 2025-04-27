from selene import browser, be, have
import os


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def should_registered_user_info(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_and_city
            )
        )
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'[value="{year}"]').click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(day)).click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value)
        browser.all('.subjects-auto-complete__option')[2].click()
        return self

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_img(self, value):
        browser.element('#uploadPicture').send_keys(os.path.join(os.path.abspath('resources'), value))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text(value))
        return self






