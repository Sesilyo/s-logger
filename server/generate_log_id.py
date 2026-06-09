def generate_id(prefix_name, date, time):
    # prefix_name is the tag name or the project name

    # uses the first three letters of the tag/project
    # converts to uppercase
    prefix = prefix_name[:3].upper()

    # partitions the timestamp into denominations
    # Y year, m month, d day
    # H hour, M minute, S seconds
    date_suffix = date.replace("-", "") + time.replace(":", "")

    return f"{prefix}{date_suffix}"