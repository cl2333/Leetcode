def intToRoman(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        
        temp = num // 1000
        if temp > 0:
            result += temp * 'M'
        
        num = num % 1000
        temp = num // 900
        if temp > 0:
            result += 'CM'
        
        num = num % 900
        temp = num // 500
        if temp > 0:
            result += 'D'
        
        num = num % 500
        temp = num // 400
        if temp > 0:
            result += 'CD'
        
        num = num % 400
        temp = num // 100
        if temp > 0:
            result += temp*'C'
        
        num = num % 100
        temp = num // 90
        if temp > 0:
            result += 'XC'
        
        num = num % 90
        temp = num // 50
        if temp > 0:
            result += 'L'
        
        num = num % 50
        temp = num // 40
        if temp > 0:
            result += 'XL'
        
        num = num % 40
        temp = num // 10
        if temp > 0:
            result += temp*'X'
        
        num = num % 10
        temp = num // 9
        if temp > 0:
            result += 'IX'
        
        num = num % 9
        temp = num // 5
        if temp > 0:
            result += 'V'
        
        num = num % 5
        temp = num // 4
        if temp > 0:
            result += 'IV'
        
        num = num % 4
        temp = num // 1
        if temp > 0:
            result += temp*'I'
        
        return result
        
            