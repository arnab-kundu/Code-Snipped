import requests
import sys

###############################################################################################################################################
# How to run
#
# Open CMD and Run
# download_large_file_in_chunk_from_url.py your_url(space not allowed in between url)
# Sample
# download_large_file_in_chunk_from_url.py https://avatars.githubusercontent.com/u/18009010?s=400&u=625a1f8fe4d17f1890daa66671ee99351e7ed6df&v=4
#
################################################################################################################################################

# Get url
download_url = sys.argv[-1]
if download_url.endswith('.py'):
    download_url = 'https://avatars.githubusercontent.com/u/18009010?s=400&u=625a1f8fe4d17f1890daa66671ee99351e7ed6df&v=4'
else:
    pass

# Main Function
def download_file(url, filename = 'arnab.jpg'):
    try:
        if filename:
            pass
        else:
            filename = url[url.rfind('/')+1:]
            print('Downloading: ', filename)

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size = 8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

# Call Main function
download_file(download_url)