class Solution:
    def roman_to_int(self, s: str) -> int:
        if len(s) < 2:
            return self.numeral_to_int(s)

        integer = 0
        for i in range(len(s)-1):
            prev_numeral = self.numeral_to_int(s[i])
            curr_numeral = self.numeral_to_int(s[i+1])
            i += 1

            print(prev_numeral, curr_numeral)
            if prev_numeral >= curr_numeral:
                integer += prev_numeral + curr_numeral
                print('+')
                print('int:', integer)
            else:
                integer -= curr_numeral - prev_numeral
                print('-')
                print('int:', integer)


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
sol.roman_to_int('CIX')
