from qa_guru_hw_9.pages.registration_page import RegistrationPage


def test_demo_qa():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Vin')
    registration_page.fill_last_name('Diesel')
    registration_page.fill_email('mr.diesel@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_number('9999999999')
    registration_page.fill_date('7', '1995', '15')
    registration_page.fill_subjects('M')
    registration_page.fill_hobbies('Sports')
    registration_page.upload_img('person1.jpg')
    registration_page.fill_current_address('32449 Herzog Heights Suite 572')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    registration_page.submit()
    registration_page.should_have_title('Thanks for submitting the form')

    registration_page.should_registered_user_info(
        'Vin Diesel',
        'mr.diesel@mail.ru',
        'Male',
        '9999999999',
        '15 August,1995',
        'Computer Science',
        'Sports',
        'person1.jpg',
        '32449 Herzog Heights Suite 572',
        'Haryana Panipat'
    )


