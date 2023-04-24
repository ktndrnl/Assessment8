from modules_package_file import mailinglist_validation_util


def mailing_list_utils():
    return mailinglist_validation_util("mailing_list.csv", "active_users.csv", 'r+')


if __name__ == '__main__':
    # Calling the function from your package
    print('The output file has length {}.'.format(mailing_list_utils()))
