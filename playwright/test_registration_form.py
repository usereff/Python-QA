from playwright.sync_api import Page, expect
from consts import REGISTRATION_FORM

GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/9bcef875b222092b4f32c3599b7773e5d1aca48b/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"

def test_registration_form(page: Page):
    print("\n========== START REGISTRATION TEST ==========")

    print("\n[STEP 1] Opening registration form")
    page.goto(FILE_PATH)
    print("[PASS] Registration form opened successfully")

    print("\n[STEP 2] Checking accessibility tree")
    printAccessibilityTree(page)

    print("\n[STEP 3] Filling the registration form")
    fillInFullForm(page)

    print("\n[STEP 4] Validating reset functionality")
    validateResetForm(page)

    print("\n[STEP 5] Filling the registration form again")
    fillInFullForm(page)

    print("\n[STEP 6] Validating submit functionality")
    validateSubmitForm(page)

    print("\n========== REGISTRATION TEST PASSED ==========\n")

def test_header(page: Page):
    page.goto(FILE_PATH)
    verifyRegistrationLink(page)
    verifyPreferencesLink(page)
    verifyHelpLink(page)
    verifyPlaywrightDocsLink(page)


def fillInFullForm(page):
    print("\n--- Filling form fields ---")

    print(f"[ACTION] Filling First Name: {REGISTRATION_FORM.get('FirstName')}")
    fillInFirstName(page, REGISTRATION_FORM.get("FirstName"))
    print("[PASS] First Name filled")

    print(f"[ACTION] Filling Last Name: {REGISTRATION_FORM.get('LastName')}")
    fillInLastName(page, REGISTRATION_FORM.get("LastName"))
    print("[PASS] Last Name filled")

    print(f"[ACTION] Filling Email: {REGISTRATION_FORM.get('Email')}")
    fillInEmail(page, REGISTRATION_FORM.get("Email"))
    print("[PASS] Email filled")

    print("[ACTION] Filling Email Confirmation")
    fillInEmailConfirmation(page, REGISTRATION_FORM.get("Email"))
    print("[PASS] Email confirmation filled")

    print("[ACTION] Filling Password")
    fillInPassword(page, REGISTRATION_FORM.get("Password"))
    print("[PASS] Password filled")

    print(f"[ACTION] Filling Phone Number: {REGISTRATION_FORM.get('PhoneNumber')}")
    fillInPhoneNumber(page, REGISTRATION_FORM.get("PhoneNumber"))
    print("[PASS] Phone number filled")

    print(f"[ACTION] Filling Date of Birth: {REGISTRATION_FORM.get('DateOfBirth')}")
    fillInDateOfBirth(page, REGISTRATION_FORM.get("DateOfBirth"))
    print("[PASS] Date of birth filled")

    print(f"[ACTION] Selecting Country: {REGISTRATION_FORM.get('Country')}")
    selectCountry(page, REGISTRATION_FORM.get("Country"))
    print("[PASS] Country selected")

    print(f"[ACTION] Filling City: {REGISTRATION_FORM.get('City')}")
    fillInCity(page, REGISTRATION_FORM.get("City"))
    print("[PASS] City filled")

    print(f"[ACTION] Selecting Gender: {REGISTRATION_FORM.get('Gender')}")
    selectGender(page, REGISTRATION_FORM.get("Gender"))
    print("[PASS] Gender selected")

    print(f"[ACTION] Filling Personal Website: {REGISTRATION_FORM.get('PersonalWebsite')}")
    fillInPersonalWebsite(page, REGISTRATION_FORM.get("PersonalWebsite"))
    print("[PASS] Personal website filled")

    print(f"[ACTION] Selecting Occupation: {REGISTRATION_FORM.get('Occupation')}")
    selectOccupation(page, REGISTRATION_FORM.get("Occupation"))
    print("[PASS] Occupation selected")

    print("[ACTION] Filling Introduction")
    fillInIntroduction(page, REGISTRATION_FORM.get("Introduction"))
    print("[PASS] Introduction filled")

    print(f"[ACTION] Selecting Years of Experience: {REGISTRATION_FORM.get('YearsOfExperience')}")
    selectYearsOfExperience(page, REGISTRATION_FORM.get("YearsOfExperience"))
    print("[PASS] Years of experience selected")

    print(f"[ACTION] Selecting Favorite Browser: {REGISTRATION_FORM.get('FavoriteBrowser')}")
    selectFavoriteBrowser(page, REGISTRATION_FORM.get("FavoriteBrowser"))
    print("[PASS] Favorite browser selected")

    print(f"[ACTION] Selecting Topics: {REGISTRATION_FORM.get('Topics')}")
    selectTopics(page, REGISTRATION_FORM.get("Topics"))
    print("[PASS] Topics selected")

    print(f"[ACTION] Selecting Contact Method: {REGISTRATION_FORM.get('ContactMethod')}")
    selectContactMethod(page, REGISTRATION_FORM.get("ContactMethod"))
    print("[PASS] Contact method selected")

    print(f"[ACTION] Newsletter subscription: {REGISTRATION_FORM.get('Newsletter')}")
    subscribeToNewsletter(page, REGISTRATION_FORM.get("Newsletter"))
    print("[PASS] Newsletter preference set")

    print(f"[ACTION] Terms agreement: {REGISTRATION_FORM.get('Terms')}")
    agreeToTerms(page, REGISTRATION_FORM.get("Terms"))
    print("[PASS] Terms preference set")

    print("--- All form fields filled successfully ---")


def printAccessibilityTree(page):
    print("\n[ACTION] Waiting for registration form to load...")

    page.locator("#firstName").wait_for(state="visible")

    print("[PASS] Registration form is visible")

    print("\n[ACTION] Getting accessibility tree...")

    accessibility_tree = page.locator("body").aria_snapshot()

    print("\n========== ACCESSIBILITY TREE ==========")
    print(accessibility_tree)
    print("========================================\n")
    
def fillInFirstName(page, firstName):
    #By role, preferred method
    page.get_by_role("textbox", name="First name").fill(firstName)
    
    #By label, preferred method
    # page.get_by_label("First name").fill("Doe")

    # #By placeholder, good option if the placeholder is unique and descriptive
    # page.get_by_placeholder("e.g. Alex").fill("John")

    # #By locator, good option if the locator is unique and descriptive
    # page.locator("#firstName").fill("Doe")

    # #By locator, Usually unnecessary
    # page.locator('input[id="firstName"]').fill("John")
    # page.fill('input[name="firstName"]', "Doe")


def fillInLastName(page, lastName):
    page.get_by_role("textbox", name="last Name").fill(lastName)

def fillInEmail(page, email):
    page.get_by_placeholder("alex@example.com").fill(email)

def fillInEmailConfirmation(page, email):
    page.get_by_label("Confirm email").fill(email)

def fillInPassword(page, password):
    page.locator('input[type="password"]').fill(password)

def fillInPhoneNumber(page, phoneNumber):
    page.get_by_role("textbox", name="Phone number").fill(phoneNumber)

def selectCountry(page, country):
    countrySelect = page.get_by_role("combobox", name="Country")
    countrySelect.select_option(label=country)

def fillInCity(page, city):
    page.get_by_role("textbox", name="City").fill(city)

def selectGender(page, gender):
    genderSelect = page.locator(f'input[type="radio"][value="{gender}"]')
    genderSelect.check()   

def fillInDateOfBirth(page, dateOfBirth):
    #By label, preferred method
    datePicker = page.get_by_label("Date of birth")
    datePicker.fill(dateOfBirth)
    datePicker.scroll_into_view_if_needed()
    datePicker.highlight()  

def verifyRegistrationLink(page):
    print("\n[ACTION] Checking Registration link")

    registrationLink = page.get_by_role("link", name="Registration")

    registrationLink.scroll_into_view_if_needed()
    registrationLink.highlight()

    print("[CHECK] Verifying link is visible")
    expect(registrationLink).to_be_visible()
    print("[PASS] Registration link is visible")

    print("[CHECK] Verifying link destination")
    href = registrationLink.get_attribute("href")
    assert href.endswith("#registration"), f"Unexpected href: {href}"
    print("[PASS] Registration link has the correct destination")

    print("[ACTION] Clicking Registration link")
    registrationLink.click()

    print("[CHECK] Verifying URL after click")
    assert page.url.endswith("#registration"), f"Unexpected URL: {page.url}"
    print("[PASS] Registration navigation verified")
    
def verifyHelpLink(page):
    helpLink = page.get_by_role("link", name="Help")
    helpLink.scroll_into_view_if_needed()
    helpLink.highlight()
    helpLink.click()

    printAccessibilityTree(page)
    dialog = page.get_by_role("dialog", name=REGISTRATION_FORM["modalHeaderText"])
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role("heading", level=2, name=REGISTRATION_FORM.get("modalHeaderText"))).to_be_visible()

    dialogOkButton = dialog.get_by_role("button", name=REGISTRATION_FORM.get("modalButtonText"))
    expect(dialogOkButton).to_be_visible()
    expect(dialogOkButton).to_be_enabled()
    dialogOkButton.click()

def resetForm(page):
    print("[ACTION] Clicking Reset form button")

    page.get_by_role("button", name="Reset form").click()

    print("[PASS] Reset button clicked successfully")

def fillInPersonalWebsite(page, website):
    page.get_by_label("Personal website").fill(website)


def selectOccupation(page, occupation):
    page.get_by_label("Occupation").select_option(occupation)


def fillInIntroduction(page, introduction):
    page.get_by_label("Short introduction").fill(introduction)


def selectYearsOfExperience(page, experience):
    page.get_by_label("Years of experience").select_option(experience)


def selectFavoriteBrowser(page, browser):
    page.get_by_label("Favorite browser").select_option(browser)


def selectTopics(page, topics):
    for topic in topics:
        page.locator(
            f'input[type="checkbox"][name="topics"][value="{topic}"]'
        ).check()


def selectContactMethod(page, contact_method):
    page.locator(
        f'input[type="radio"][name="contactMethod"][value="{contact_method}"]'
    ).check()


def subscribeToNewsletter(page, subscribe):
    newsletter = page.locator("#newsletter")

    if subscribe:
        newsletter.check()
    else:
        newsletter.uncheck()


def agreeToTerms(page, agree):
    terms = page.locator("#terms")

    if agree:
        terms.check()
    else:
        terms.uncheck()

def validateResetForm(page: Page):

    print("\n--- Starting Reset Validation ---")

    resetForm(page)

    print("[CHECK] Verifying text fields are empty")

    expect(page.locator("#firstName")).to_have_value("")
    expect(page.locator("#lastName")).to_have_value("")
    expect(page.locator("#email")).to_have_value("")
    expect(page.locator("#confirmEmail")).to_have_value("")
    expect(page.locator("#password")).to_have_value("")
    expect(page.locator("#phone")).to_have_value("")
    expect(page.locator("#birthday")).to_have_value("")
    expect(page.locator("#city")).to_have_value("")
    expect(page.locator("#website")).to_have_value("")
    expect(page.locator("#bio")).to_have_value("")

    print("[PASS] All text fields are empty")

    print("[CHECK] Verifying dropdowns returned to default values")

    expect(page.locator("#country")).to_have_value("")
    expect(page.locator("#occupation")).to_have_value("")
    expect(page.locator("#experience")).to_have_value("")
    expect(page.locator("#favoriteBrowser")).to_have_value("")

    print("[PASS] All dropdowns returned to default values")

    print("[CHECK] Verifying Gender radio buttons are unchecked")

    expect(page.locator('input[name="gender"]:checked')).to_have_count(0)

    print("[PASS] Gender radio buttons are unchecked")

    print("[CHECK] Verifying Topics checkboxes are unchecked")

    expect(page.locator('input[name="topics"]:checked')).to_have_count(0)

    print("[PASS] Topics checkboxes are unchecked")

    print("[CHECK] Verifying default contact method")

    expect(
        page.locator('input[name="contactMethod"][value="email"]')
    ).to_be_checked()

    print("[PASS] Default contact method is Email")

    print("[CHECK] Verifying Newsletter and Terms are unchecked")

    expect(page.locator("#newsletter")).not_to_be_checked()
    expect(page.locator("#terms")).not_to_be_checked()

    print("[PASS] Newsletter and Terms are unchecked")

    print("--- Reset validation completed successfully ---")

def validateSubmitForm(page: Page):

    print("\n--- Starting Submit Validation ---")

    print("[ACTION] Clicking Submit registration button")

    page.get_by_role(
        "button",
        name="Submit registration"
    ).click()

    print("[PASS] Submit button clicked")

    confirmation_dialog = page.locator("#confirmationDialog")

    print("[CHECK] Verifying confirmation dialog is visible")
    expect(confirmation_dialog).to_be_visible()
    print("[PASS] Confirmation dialog is visible")

    print("[CHECK] Verifying confirmation heading")

    expect(
        confirmation_dialog.get_by_role(
            "heading",
            name="Registration submitted!"
        )
    ).to_be_visible()

    print("[PASS] Confirmation heading is visible")

    print("[CHECK] Verifying success message")

    expect(page.locator("#status")).to_have_text(
        "Form submitted successfully (demo)."
    )

    print("[PASS] Success message displayed")

    print("[ACTION] Closing confirmation dialog")
    page.locator("#closeDialog").click()

    print("[CHECK] Verifying confirmation dialog is closed")
    expect(confirmation_dialog).not_to_be_visible()

    print("[PASS] Confirmation dialog closed successfully")

    print("--- Submit validation completed successfully ---")

def verifyPlaywrightDocsLink(page):
    print("\n[ACTION] Checking Playwright documentation link")

    docsLink = page.get_by_role("link", name="Playwright documentation")

    docsLink.scroll_into_view_if_needed()
    docsLink.highlight()

    print("[CHECK] Verifying link is visible")
    expect(docsLink).to_be_visible()
    print("[PASS] Link is visible")

    print("[CHECK] Verifying link destination")
    expect(docsLink).to_have_attribute("href", "https://playwright.dev/")
    print("[PASS] Link points to Playwright documentation")

    print("[CHECK] Verifying link opens in a new tab")
    expect(docsLink).to_have_attribute("target", "_blank")
    print("[PASS] Link is configured to open in a new tab")

def verifyPreferencesLink(page):
    print("\n[ACTION] Checking Preferences link")

    preferencesLink = page.get_by_role("link", name="Preferences")

    preferencesLink.scroll_into_view_if_needed()
    preferencesLink.highlight()

    print("[CHECK] Verifying link is visible")
    expect(preferencesLink).to_be_visible()
    print("[PASS] Preferences link is visible")

    print("[CHECK] Verifying link destination")
    href = preferencesLink.get_attribute("href")
    assert href.endswith("#preferences"), f"Unexpected href: {href}"
    print("[PASS] Preferences link has the correct destination")

    print("[ACTION] Clicking Preferences link")
    preferencesLink.click()

    print("[CHECK] Verifying URL after click")
    assert page.url.endswith("#preferences"), f"Unexpected URL: {page.url}"
    print("[PASS] Preferences link navigation verified")