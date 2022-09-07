#authentication details for accessing td amertirade api
#'api_key' -> personal use api key given by td developer account
#'redirect_url' -> always stays as local host when run on personal machine
#'driver_path' -> path to chromedriver in users C driver
#'token_path' -> when td amertirade api is first accessed a 30-day
#                token is created to be used for faster access

api_key = '5W348KLER7G2MNO77MMYDBULKDGPFOTQ@AMER.OAUTHAP'
redirect_url = 'https://localhost'
driver_path = "C:\Program Files\Webdrivers\chromedriver.exe"
token_path = 'data_feeds/td_ameritrade/authentication/token'

