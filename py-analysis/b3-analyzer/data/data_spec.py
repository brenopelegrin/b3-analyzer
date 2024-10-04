import uuid
import json
import os

class AssetsData:
    def __init__(self, path='data/assets.json'):
        self._path = path
        self._dict = {}
        self._loaded = False
        self.load()
        
    @property
    def loaded(self):
        return self._loaded
    
    @property
    def exchanges(self):
        return list(self._dict["exchanges"].keys())
    
    def assets(self, exchange):
        """
        Get all assets from exchange.
        
        Args:
            exchange (str): Exchange name.
        
        Returns:
            dict: dict of assets.
            
        Raises:
            Exception: If exchange not found.
        """
        if exchange in self.exchanges:
            return self._dict["exchanges"][exchange]
        else:
            raise Exception(f"Exchange `{exchange}` not found.")
                
    def load(self):
        try:
            with open(self._path, 'r') as f:
                self._dict = json.load(f)
                self._loaded = True
        except Exception as exc:
            self._loaded = False
            raise Exception(f"Error when loading AssetsData from file `{self.path}`.")
    
    def save(self):
        with open(self._path, 'w') as f:
            json.dump(self._dict, f, indent=True)
            
    def addAsset(self, asset):
        if isinstance(asset, B3Asset):
            if asset.symbol not in self.assets(asset.exchange):
                self._dict["exchanges"][asset.exchange][asset.symbol] = asset.toDict()
                self.save()
                
        elif isinstance(asset, TesouroAsset):
            if asset.isin not in self.assets(asset.exchange):
                self._dict["exchanges"][asset.exchange][asset.isin] = asset.toDict()
                self.save()   
        else:
            raise Exception(f"Invalid asset type `{type(asset)}`.")

class TesouroAsset:
    def __init__(self, isin, name, due_date, index, min_investment, unit_price, annual_interest, reference_date):
        self._exchange = "tesourodireto"
        self._isin = isin
        self._name = name
        self._due_date = name
        self._index = index
        self._min_investment = min_investment
        self._unit_price = unit_price
        self._annual_interest = annual_interest
        self._reference_date = reference_date
    
    @property
    def name(self):
        return self._name
        
    @property
    def exchange(self):
        return self._exchange
    
    @property
    def isin(self):
        return self._isin
    
    @property
    def dueDate(self):
        return self._due_date  

    @property
    def index(self):
        return self._index
    
    @property
    def minInvestment(self):
        return self._min_investment
    
    @property
    def unitPrice(self):
        return self._unit_price
    
    @property
    def annualInterest(self):
        return self._annual_interest
    
    @property
    def referenceDate(self):
        return self._reference_date
    
    def toDict(self):
        return {
            "isin": self.isin,
            "name": self.name,
            "due_date": self.dueDate,
            "index": self.index,
            "min_investment": self.minInvestment,
            "unit_price": self.unitPrice,
            "annual_interest": self.annualInterest,
            "reference_date": self.referenceDate
        }
        
class B3Asset:
    def __init__(self, symbol, name):
        self._id = uuid.uuid4()
        self._symbol = symbol
        self._name = name
        self._exchange = "b3"
        
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def name(self):
        return self._name
        
    @property
    def exchange(self):
        return self._exchange
    
    def toDict(self):
        return {
            "id": self._id,
            "symbol": self.symbol,
            "name": self.name
        }
