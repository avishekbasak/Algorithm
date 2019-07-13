In this program I have used recursion to find if the user has access or not. For every step, we first check if the user is same as group or if the user is present amongst the users in the group. Otherwise, we iteratively look for the user in each group.

TIme Complexity:
1. in worst case I can find the user in the last group in the last user. Hence, in worst scenario i have to traverse all the groups and for every group check every user.
Hence O(G*U), where G is the total number of groups and U is total number of Users.

Space Complexity:
Space coplexity will be O(G*U), where G is the total number of groups and U is total number of Users.
