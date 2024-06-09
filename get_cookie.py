"""
Prompts the user to log in to the HoYoLAB website and saves the cookie to a file.
"""
import argparse
import enum
import pathlib
import typing

from playwright.sync_api import sync_playwright

class Browser(enum.Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"

    def __str__(self):
        return self.value

def main(browser: Browser = Browser.CHROMIUM, executable: typing.Optional[str] = None):
    with sync_playwright() as p:
        if browser is Browser.CHROMIUM:
            browse = p.chromium.launch(executable_path=executable, headless=False)
        elif browser is Browser.FIREFOX:
            browse = p.firefox.launch(executable_path=executable, headless=False)
        elif browser is Browser.WEBKIT:
            browse = p.webkit.launch(executable_path=executable, headless=False)
        else:
            raise ValueError(f"Unknown browser: {browser}")
        page = browse.new_page()
        page.goto("https://www.hoyolab.com/accountCenter/postList?id=71845688")
        page.wait_for_selector("div.mhy-game-record-card-list", timeout=None)
        cookies = page.context.cookies("https://www.hoyolab.com/accountCenter/postList")
        # Playwright returns a list of dictionaries, we need to convert it to a string
        cookie = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        (pathlib.Path(__file__).parent / "COOKIE").write_text(cookie)
        browse.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the cookie from the HoYoLAB website")
    parser.add_argument("--browser", default="chromium", choices=["chromium", "firefox", "webkit"], help="The browser to use (default: chromium)")
    parser.add_argument("--executable", default=None, help="The path to the browser executable (optional)")
    args = parser.parse_args()
    main(browser=Browser(args.browser), executable=args.executable)
