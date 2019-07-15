In this program I have used linkedlist to maintain the block chain. for every new block we keep it appending to the tail of the list

TIme Complexity:
1. for appending it will be O(1), since we have just to change the tail pointer

Space Complexity:
Space coplexity will be O(nk), where n is the number of blocks and k is the space taken by each block. Since n will be dominant, we can say it is O(n)
