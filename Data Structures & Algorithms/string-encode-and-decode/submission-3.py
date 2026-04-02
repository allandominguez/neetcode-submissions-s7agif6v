class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        print(encoded_str)
        return encoded_str
    
    def _get_str_len(self, s: str, cur: int) -> int:
        this_cur = cur
        str_len = ""
        while this_cur < len(s):
            if s[this_cur] == "#":
                return int(str_len)
            elif not s[this_cur].isdigit():
                return 0
            str_len += str(s[this_cur])
            this_cur += 1
        return 0
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        cur = 0
        while cur < len(s):
            if s[cur].isdigit():
                str_len = self._get_str_len(s, cur)
                if str_len < 0:
                    cur += 1
                    continue
                cur += len(str(str_len)) + 1
                if str_len == 0:
                    decoded_list.append("")
                else:
                    decoded_list.append(s[cur:cur+str_len])
                cur += str_len
            else:
                cur += 1
        
        return decoded_list

