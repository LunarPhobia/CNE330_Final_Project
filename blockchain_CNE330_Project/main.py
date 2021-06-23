# PyCoin (PYC)

#import library

import hashlib

#define class

class PyCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#list of transactions

t1 = "Nikita sends 1 PYC to Justin"
t2 = "Jack sends 4.8 PYC to Zak"
t3 = "Zak sends 11 PYC to Justin"
t4 = "Justin sends 3 PYC to Fiseha"
t5 = "Nikita sends .02 PYC to Zak"
t6 = "Fiseha sends 1.1 PYC to Jack"

#blockchain

initial_block = PyCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = PyCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = PyCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)
