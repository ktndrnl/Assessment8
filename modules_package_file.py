import csv
from update_mailing_list import update_mailing_list

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def read_mailing_list_file(filename, io_mode):
    """
        Input:
       - filename: the filename of the original dataset we are going to read the data from.
       - io_mode: the `input/output` mode we will use to handle the file operation.

        Output: the list of ids of the active users.
    """
    mailing_list = []
    with open(filename, io_mode) as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')
        next(file_reader)  # Skipping the header row

        for row in file_reader:
            mailing_list.append(row)

    mailing_list_buffer = []

    for item in mailing_list:
        mailing_list_buffer.append((item[0], [item[1], item[2], item[3]]))

    mailing_dict = dict(mailing_list_buffer)

    updated_mailing_list_ids = update_mailing_list(mailing_dict)

    return updated_mailing_list_ids


def save_output_file(updated_mailing_list, output_filename, io_mode):
    """
    Input:
   - updated_mailing_list: the list of ids of the active users in our CRM system database after filtered out the "unsubscribed" users.
   - output_filename: the name of the output file that will persist the users ids.
   - io_mode: the `input/output` mode we will use to handle the file operation.

    Output: This function does not return anything. Instead, write the results into an output csv file.
    """

    # Write each user id as a new row to the file
    with open(output_filename, io_mode) as active_users_file:
        csv_writer = csv.writer(active_users_file, delimiter=',')
        for user_id in updated_mailing_list:
            csv_writer.writerow([user_id])

    return None


def mailinglist_validation_util(filename, output_filename, io_mode):
    """
   Input:
   - filename: the name of the input file with the raw mailing list
   - output_filename: the name of the final, output csv file
   - io_mode: the io operation that this function needs, passed as an array

   Output: Returns the output file length
    """
    user_ids = read_mailing_list_file(filename, io_mode[0])
    save_output_file(user_ids, output_filename, io_mode[0])

    with open(output_filename, io_mode[0]) as output_file:
        output_file_length = len(output_file.readlines())

    return output_file_length
