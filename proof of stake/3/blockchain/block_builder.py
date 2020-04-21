# -*- coding: utf-8 -*-
from .block import Block
from .block import GenesisBlock

class BlockBuilder:

    def __init__(self):
    	print('Initializing BlockBuilder...')
    	pass

    def generate_genesis_block(self, server_id):
    	genesis_block = GenesisBlock(server_id)
    	return genesis_block

    def generate_new_block(self, transaction, previous_block_hash, server_id):
        new_block = Block(transaction, previous_block_hash, server_id)
        return new_block


