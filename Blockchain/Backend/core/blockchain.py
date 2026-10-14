import sys
import time

"""
ПРИМЕЧАНИЕ ПО ЗАПУСКУ:
Этот скрипт использует абсолютные импорты от корня проекта.
Чтобы избежать ошибок ModuleNotFoundError, запускайте его из корневой папки `learn_coin_chain` через терминал:

    python -m Blockchain.Backend.core.blockchain
"""
from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.utils.util import hash256

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock() 

    def GenesisBlock(self):
        self.addBlock(0, ZERO_HASH)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f'Codies Alert sent {BlockHeight} Bitcoins to Jeo'
        
        # Хэшируем транзакцию для корня Меркла
        merkleRoot = hash256(Transaction)
        bits = 'ffff001f'
        
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        
        new_block = Block(BlockHeight, 1, blockheader, 1, Transaction)
        self.chain.append(new_block)


if __name__ == "__main__":
    blockchain = Blockchain()
    print("Add second block...")
    last_block_hash = blockchain.chain[-1]._Block__BlockHeader.blockHash
    blockchain.addBlock(1, last_block_hash)
