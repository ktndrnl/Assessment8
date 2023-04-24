def update_mailing_list(mailing_list):
    mailing_list_copy = mailing_list.copy()
    for key, value in mailing_list_copy.items():
        status = value[2]
        email = value[1]
        if "opt-out" in status.lower() or "unsubscribed" in status.lower():
            del mailing_list[key]
            continue
        if "@gmail" in email.lower():
            del mailing_list[key]

    ids = []

    for key, value in mailing_list.items():
        ids.append(key)
    return ids
