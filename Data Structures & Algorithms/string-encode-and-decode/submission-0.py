class Solution:
    # ["Hello","World"]
    # 5#Hello5#Wrold
    # so len(str) + "#" + str....
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # take int values up to first #. then take index from # + 1 till # + 1 + int value

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            string = s[j + 1 : j + length + 1]
            res.append(string)
            i = j + length + 1
        
        return res
        
            

