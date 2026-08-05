class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adjacency_list=[[] for i in range(n)]
        for caller,callee in invocations:
            adjacency_list[caller].append(callee)
        suspicous=[False]*n

        def dfs(method):
            suspicous[method]=True
            for next_method in adjacency_list[method]:
                if not suspicous[next_method]:
                    dfs(next_method)
        dfs(k)
        ''' 
        if there is a normal method calling a suspicous method and also if it is not suspicous 
        meaning True and True then we need to can't remove the suspicous methods
        '''
        for caller,callee in invocations:
            if not suspicous[caller] and suspicous[callee]:
                return [i for i in range(n)]
        '''
        if there are suspicous methods and there are no outside methods connected to it
        we can remove the suspicous methods
        '''
        normal_methods=[]
        for method in range(n):
            if not suspicous[method]:
                normal_methods.append(method)
        return normal_methods                





        