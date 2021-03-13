class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        l=[str(x) for x in range(10)]
        lSymbols=['+','-']
        lE=['.',' ']
        out=''
        isOneSymbolRecevied=False
        if len(s) == 0: return 0
        for i in range(len(s)):
            if i ==0 and s[i] not in l and s[i] not in lSymbols and s[i] in lE:
                return 0
            if (s[i] in l) and not isOneSymbolRecevied:
                out+=s[i]
                continue
            if s[i] in lSymbols:
                if not isOneSymbolRecevied and s[i] in lE:
                    out+=s[i]
                    
                    isOneSymbolRecevied=True
                    continue
                else:
                    break
        if len(out) == 1 and out in lSymbols:
            return 0
        if  int(out) < 0 and int(out) < -2147483648:
            return -2147483648
        elif int(out) > 2147483647:
            return 2147483647
        return int(out)

s=Solution()
print(s.myAtoi("  -42"))