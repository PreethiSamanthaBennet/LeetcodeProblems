class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            temp = ''
            
            if i % 3 != 0 and i % 5 != 0:
                temp += f'{i}'
                
            if i % 3 == 0:
                temp += "Fizz"
                
            if i % 5 == 0:
                temp += "Buzz" 
                
            res.append(temp)

        return res
