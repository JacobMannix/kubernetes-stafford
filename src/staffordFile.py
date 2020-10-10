# Jacob Mannix [09-09-2020]

# stafford_file function to initially find the postTitle value and it it doesnt exist it will create one with a default value.

# Import Dependencies
import os

# Function
def staffordFile(file_path):
    postTitle = []
    # Check if file exists
    if os.path.isfile(file_path):
        # if file exists open it
        with open(file_path, 'r') as file:
            for line in file:
                postTitle.append(str(line))
        postTitle = postTitle[0]
        return postTitle
    else:
        # if file doesn't exist create it with a default value
        # yesterday_date = date.today() - timedelta(days = 1)
        # end_title = ' SK Modified® Feature Results'
        # default_title = yesterday_date + end_title
        post_title = 'no previous race title'
        with open(file_path, "w") as output:
            output.write(str(post_title))
        return post_title