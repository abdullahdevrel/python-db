import maxminddb
import urllib.request
import os

DB_DOWNLOAD_URL = "https://ipinfo.io/data/free/country_asn.mmdb?token="
DEFAULT_DB_PATH = "./files/country_asn.mmdb"

class Client:

    def __init__(self, access_token=None, path=None, replace=False):
        self.access_token = access_token
        self.path = path
        self.replace = replace

        if self.access_token is None and self.path is None:
            raise SyntaxError("Token or Path is required")
            
        if self.path is None:
            self.path = DEFAULT_DB_PATH

        # Check if file already exists skip the download.
        if os.path.exists(self.path) and not self.replace:
            print("File already exists. Skipping download.")
        else:
            if self.access_token is None:
                raise SyntaxError("Token is required to download the file")
            
            # Create directory if doesn't exist and download file.
            directory = os.path.dirname(self.path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                print("Downloading mmdb file.")
                urllib.request.urlretrieve(DB_DOWNLOAD_URL+self.access_token, self.path)

        # Read the mmdb file.
        self.db = maxminddb.open_database(self.path)

    def getDetails(self, ip):
        return self.db.get(ip)

    def getCountry(self, ip):
        return self.db.get(ip)['country']
    
    def getCountryName(self, ip):
        return self.db.get(ip)['country_name']
    
    def getContinent(self, ip):
        return self.db.get(ip)['continent']
    
    def getContinentName(self, ip):
        return self.db.get(ip)['continent_name']
    
    def getASN(self, ip):
        return self.db.get(ip)['asn']
    
    def getASNName(self, ip):
        return self.db.get(ip)['as_name']
    
    def getASNDomain(self, ip):
        return self.db.get(ip)['as_domain']
                