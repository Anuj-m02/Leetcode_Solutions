class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        
        n = len(skill)
        skill.sort()

        left , right = 0 , n-1
        req = skill[left] + skill[right]
        cnt = 0

        while left < right :
            a , b = skill[left] , skill[right]
            if a + b != req :
                return -1

            cnt += a*b
            left += 1
            right -= 1

        return cnt 

