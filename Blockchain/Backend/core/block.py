class Block:
    """ Block is a storage container that stores transactions """
    def __init__(self, Height, BlockSize, BlockHeader, TxCount, Txs):
        self.__next = None
        self.__Height = Height
        self.__BlockSize = BlockSize
        self.__BlockHeader = BlockHeader
        self.__txCount = TxCount
        self.__Txs = Txs

