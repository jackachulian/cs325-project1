import os
import pytest
import scraper

# Fixture to provide sample HTML and a scraper instance
@pytest.fixture
def sample_html():
    return """
    <div class="apphub_CardTextContent">
        <div class="date_posted">Posted: July 12, 2023</div>
        <br>The developers clearly made this game.</div>
    <div class="apphub_CardTextContent">
        <div class="date_posted">Posted: April 16</div>
        <br>Absolutely amazing!</div>
    """

@pytest.fixture
def new_scraper():
    return scraper.SteamReviewScraper("https://example.com")

def test_parse_reviews(scraper, sample_html):
    """
    Test the parsing logic to ensure reviews are cleaned correctly.
    """
    reviews = scraper.parse_reviews(sample_html)
    assert reviews == [
        "The developers clearly made this game.",
        "Absolutely amazing!"
    ]

def test_save_reviews(scraper):
    """
    Test the saving logic to ensure files are created correctly.
    """
    reviews = ["Review 1", "Review 2"]
    output_dir = "test_reviews"
    scraper.output_dir = output_dir

    # Save reviews
    scraper.save_reviews(reviews)

    # Check if files are created
    for idx, review in enumerate(reviews):
        filename = os.path.join(output_dir, f"review_{idx + 1}.txt")
        assert os.path.exists(filename)

    # Clean up
    for idx, review in enumerate(reviews):
        filename = os.path.join(output_dir, f"review_{idx + 1}.txt")
        os.remove(filename)
    os.rmdir(output_dir)

# test 1
new_scraper()

# test 2
test_parse_reviews(new_scraper())

# test 3
test_save_reviews(new_scraper())

# test 4
new_scraper().get_steam_reviews()