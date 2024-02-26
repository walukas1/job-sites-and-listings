from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/jobs/search/?currentJobId=3775074715&f_E=1&geoId=90000020&keywords=data%20&location=Albuquerque-Santa%20Fe%20Metropolitan%20Area&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
    page.get_by_role("link", name="LinkedIn").click()
    page.get_by_label("Primary").get_by_role("link", name="Jobs").click()
    page.get_by_placeholder("Search job titles or companies").click()
    page.get_by_placeholder("Search job titles or companies").fill("Data Scientist")
    page.get_by_role("option", name="Data Scientist", exact=True).click()
    page.get_by_placeholder("Location").click()
    page.get_by_placeholder("Location").press("Meta+a")
    page.get_by_placeholder("Location").fill("albuqu")
    page.get_by_placeholder("Location").press("ArrowDown")
    page.get_by_placeholder("Location").press("Enter")
    page.locator("#main-content").get_by_role("link", name="Junior Machine Learning").click()
    page.get_by_label("Show more, visually expands").click()
    page.get_by_role("link", name="LinkedIn").click()
    page.get_by_label("Primary").get_by_role("link", name="Jobs").click()
    page.goto("https://www.linkedin.com/jobs/robots.txt")
    page.goto("https://www.linkedin.com/jobs/robots.txt?_l=en_US")
    page.goto("https://www.linkedin.com/robots.txt")
    page.get_by_text("# Notice: The use of robots").click()
    page.get_by_text("# Notice: The use of robots").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
