import requests

class TreasuryAPI:
    def __init__(self):
        self._baseURL = "https://api.dadosdemercado.com.br/v1"
        self._treasuryURL = self._baseURL+'/treasury'
        self._authToken = "8cb7a3a5529cec195ed3adc5cd994e66"
        
    def _get(self, url):
        return requests.get(url, headers={
            "Authorization": f"Bearer {self._authToken}"
        })
        
    def listOfAssets(self):
        response = self._get(self._treasuryURL)
        return response.json()
    
    def assetData(self, isin):
        response = self._get(self._treasuryURL + f'/{isin}')
        return response.json()