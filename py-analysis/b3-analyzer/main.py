from data.data_spec import B3Asset, TesouroAsset, AssetsData
from data.providers.dadosmercado import TreasuryAPI

if __name__ == "__main__":
    treasury = TreasuryAPI()
    print(treasury.listOfAssets())
    
