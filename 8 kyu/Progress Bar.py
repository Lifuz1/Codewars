# Given a character and a value between 0 to 100 with a multiple of 10, return a string that represents a simple progress bar.
#
# The value represents a percentage.
# The bar should begin and end with "|"
# Repeat the character to fill the bar, with each character equivalent to 10%
# Use spaces to pad the bar to a length of 10 characters.
# A single space comes after the bar, then a message with the % of completion (e.g. "Progress: 60%")
# If the value is 100, the message should be "Completed!".
# Examples
# ("#", 0)    ➞ "|          | Progress: 0%"
#
# ("=", 40)   ➞ "|====      | Progress: 40%"
#
# ("#", 60)   ➞ "|######    | Progress: 60%"
#
# (">", 100)  ➞ "|>>>>>>>>>>| Completed!"


def progress_bar(bar, progress):

    bar = progress // 10 * bar
    spaces = 10 - len(bar)
    bar = bar.ljust(len(bar) + spaces, ' ')
    if progress == 100:
        return f'|{bar}| Completed!'
    else:
        return f'|{bar}| Progress: {progress}%'