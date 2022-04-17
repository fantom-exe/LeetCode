class Solution:
    def roman_to_int(self, s: str) -> int:
        if len(s) < 2:
            return self.numeral_to_int(s)

        curr_numeral = 0
        next_numeral = 0
        integer = 0
        for i in range(len(s)-1):
            curr_numeral = self.numeral_to_int(s[i])
            next_numeral = self.numeral_to_int(s[i + 1])
            print(curr_numeral, next_numeral)

            if curr_numeral == 1 and (next_numeral == 5 or next_numeral == 10):
                integer -= curr_numeral
                print(integer)
            elif curr_numeral == 10 and (next_numeral == 50 or next_numeral == 100):
                print(integer)
                integer -= curr_numeral
            elif curr_numeral == 100 and (next_numeral == 500 or next_numeral == 1000):
                print(integer)
                integer -= curr_numeral
            else:
                print(integer)
                integer += curr_numeral

        integer += next_numeral

        print('total:', integer)
        return integer

    @staticmethod
    def numeral_to_int(numeral):
        match numeral:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
            case _:
                return "Unknown numeral"


sol = Solution()
sol.roman_to_int('MCMXCIV')
