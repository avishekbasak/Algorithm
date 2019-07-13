import hashlib
import datetime

class Block:
    '''
    This class represents the block in a blockchain that holds the data, timestamp when the block was created in GMT and previous block hash
    '''

    def __init__(self, data, previous_block):
        #get current timme in GMT format
        self.timestamp = self.__get_current_gmt()
        #set data
        self.data = data
        #set previous hash; set 0 for first block
        if previous_block is not None:
            self.previous_hash = previous_block.hash
        else:
            self.previous_hash = 0
        #calculate hash for the current block
        self.hash = self.__calc_hash()
        #capture the previous link
        self.__prev_link = previous_block

    def __calc_hash(self):
        '''
        calculate hash of data using SHA-256 hash
        '''
        if self.data is None:
            return 0
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Block(data={self.data},time={self.timestamp},previous_hash={self.previous_hash})"

    def __get_current_gmt(self):
        '''
        return current GMT time
        '''
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        #append new block to the tail, if head is set otherwise set both head and tail
        if self.head is None:
            block = Block(data,None)
            self.head = block
            self.tail = self.head
        else:
            block = Block(data,self.tail)
            self.tail = block



#Block class test
block0 = Block("Some Information", None)
block1 = Block("Another Information", block0)
block2 = Block("More Information", block1)

print(block0)
#Block(data=Some Information,time=2019-07-09T04:32:08.008120UTC,previous_hash=0)
print(block1)
#Block(data=Another Information,time=2019-07-09T04:32:08.008394UTC,previous_hash=6d8bf1eac14158e858b3a3a376c5dedeceb895ce5fc715324020eb0cfb2d4336)
print(block2)
#Block(data=More Information,time=2019-07-09T04:32:08.008414UTC,previous_hash=1c760e5bf2ac1e928e173797e96569888f11cd1a4602f587f4f990c65b2fd9c7)

blockchain = BlockChain()
blockchain.append("Some Information")
blockchain.append("Another Information")
blockchain.append("More Information")

print(blockchain.head)
#Block(data=Some Information,time=2019-07-09T04:33:16.102419UTC,previous_hash=0)
print(blockchain.head.previous_hash)
#0
print(blockchain.tail)
#Block(data=More Information,time=2019-07-09T04:33:16.102447UTC,previous_hash=1c760e5bf2ac1e928e173797e96569888f11cd1a4602f587f4f990c65b2fd9c7)
print(blockchain.tail.previous_hash)
#1c760e5bf2ac1e928e173797e96569888f11cd1a4602f587f4f990c65b2fd9c7
