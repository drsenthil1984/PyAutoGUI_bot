from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Step 1: Open Cricbuzz")

    page.goto(
        "https://www.cricbuzz.com/",
        wait_until="domcontentloaded"
    )

    page.screenshot(path="cricbuzz_home.png")

    print("Step 2: Open Live Scores directly")

    page.goto(
        "https://www.cricbuzz.com/cricket-match/live-scores",
        wait_until="domcontentloaded"
    )

    page.screenshot(
        path="live_scores.png",
        full_page=True
    )

    print("Step 3: Wait for India vs West Indies")

    page.get_by_text(
        "India vs West Indies",
        exact=False
    ).first.wait_for(timeout=15000)

    print("India vs West Indies found")

    page.screenshot(
        path="india_vs_west_indies.png",
        full_page=True
    )

    print("Step 4: Extract page title")

    title = page.title()
    print("Page title:", title)

    print("Step 5: Extract visible page data")

    page_text = page.locator("body").inner_text()

    print("--------------------------------")
    print(page_text[:5000])
    print("--------------------------------")

    input("Press Enter to close browser...")

    browser.close()