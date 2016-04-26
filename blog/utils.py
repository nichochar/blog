from articles import articles_data

months = {
    1: 'january',
    2: 'februrary',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}


def get_title_from_slug(slug):
    """
    From a slug, find the right article, return it's title
    """
    for article in articles_data:
        if article['slug'] == slug:
            return article['title']

    return False
