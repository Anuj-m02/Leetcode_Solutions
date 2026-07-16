from collections import defaultdict , deque

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        # id , start , between time

        res = [0]*(n)

        stack = []

        for log in logs :
            curr_fn , curr_state , time = log.split(":")
            curr_fn = int(curr_fn)
            time = int(time)

            if curr_state == "start" :
                stack.append([curr_fn , time , 0])
            
            else :
                fn , start_time ,bw = stack.pop()

                total = time-start_time+1
                temp = total - bw

                res[fn] += temp

                if stack :
                    stack[-1][2] += total
            


        return res

