class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        '''
        adjacency list is initialized to reduce the search methods in invocations
        here each array represent indexes or method number and whom they call 
        if 0->1,0->2 then in adjancency list it is represented as method:0 [1,2]
        rather than showing [0,1][0,2] in invocations
        '''
        adjacency_list=[[] for i in range(n)]
        for caller,callee in invocations:
            adjacency_list[caller].append(callee)
        suspicous=[False]*n
        '''
        initially dfs(k) is called and then we'll check every method , the k is changed to True 
        and for the non-visited method well change to True until every method from k to rest is reached
        '''
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





        