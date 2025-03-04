import hashlib
from time import time 


def hash_256(string):
    return hashlib.sha256(string.encode()).hexdigest()

class TransactionGenerator:
    def __init__(self):
        self.random_seed=0
    
    def generate_transaction(self):
        transaction_payload=f"There is transaction between A and B with random seed {self.random_seed}"
        transaction_hash=hash_256(transaction_payload)
        self.random_seed+=1
        return transaction_hash
    

class Block:
    def __init__(self,hash_prev_block,target):
        self.transactions=[]
        self.hash_prev_block=hash_prev_block
        self.target=target
        self.nonce=0
        self.timestamp=time()
        self.hash=None
        self.size=1000

    def add_transaction(self,transaction):
        if len(self.transactions)<self.size:
            self.transactions.append(transaction)
    
    def __str__(self):
        return '-'.join([self.hash,str(self.timestamp),str(self.nonce)])
    
    def apply_mining(self):
        current_block_hash=hash_256(str(self))
        print(f"Current block hash: {current_block_hash} with target {self.target}")
        if int(current_block_hash,16)<int(self.target):
            print("Block mined")
            print(f"it took {self.nonce} tries to mine the block!!")
            return True
        else:
            self.nonce+=1
        
        return False
    
    def is_block_full(self):
       
        return len(self.transactions) >= self.size
    
class BlockChain:
    def __init__(self):
        self.block_chain=[]
    def push_block(self,block):
        self.block_chain.append(block)
    
    def notify_everybody(self):
        print('-' * 80)
        print('TO ALL THE NODES OF THE NETWORK, THIS BLOCK HAS BEEN ADDED:')
        print('[block #{}] : {}'.format(len(self.block_chain), self.get_last_block()))
        print('-' * 80)
    def get_last_block(self):
        return self.block_chain[-1]
    

def main_miner():
    last_block_header = '0e0fb2e3ae9bd2a0fa8b6999bfe6ab7df197a494d4a02885783a697ac74940d9'
    last_block_target = '000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    block_chain=BlockChain()
    transaction_generator=TransactionGenerator()
    block=Block(last_block_header,last_block_target)

    for i in range(1100):
        transaction=transaction_generator.generate_transaction()
        block.add_transaction(transaction)
        if block.is_block_full():
            break
        
    while not block.apply_mining():
        pass
    block_chain.push_block(block)
    block_chain.notify_everybody()

    last_block_header = hash_256(str(block_chain.get_last_block()))
    last_block_target = '0000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddffff'
    block_2=Block(last_block_header,last_block_target)

    for i in range(1320):
        transaction=transaction_generator.generate_transaction()
        block_2.add_transaction(transaction)
        if block_2.is_block_full():
            break

    while not block_2.apply_mining():
        pass
    block_chain.push_block(block_2)
    block_chain.notify_everybody()

    last_block_header = hash_256(str(block_chain.get_last_block()))
    last_block_target = '00000dddddddddddddddddddddddddddddddddddddddddddddddddddddddffff'

    block_3=Block(last_block_header,last_block_target)

    for i in range(1500):
        transaction=transaction_generator.generate_transaction()
        block_3.add_transaction(transaction)
        if block_3.is_block_full():
            break

    while not block_3.apply_mining():
        pass
    block_chain.push_block(block_3)    
    block_chain.notify_everybody()


   
if __name__ == '__main__':
    main_miner()

            


    