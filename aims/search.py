def search_by_category(items, category):
    """Tìm các đĩa DVD theo thể loại."""
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Tìm các đĩa DVD có tiêu đề chứa keyword."""
    return [dvd for dvd in items if keyword in dvd.title]
