class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        mod = int(1e9) + 7
        
        @lru_cache(maxsize=None)
        def dp(len_playlist , cnt_unique_songs) :

            if len_playlist == goal :
                return 1 if cnt_unique_songs == n else 0
            
            ans = 0 

            if cnt_unique_songs < n :
                ans += (n - cnt_unique_songs) * dp(len_playlist + 1 , cnt_unique_songs + 1)
            
            if cnt_unique_songs > k :
                ans += (cnt_unique_songs - k) * dp(len_playlist + 1 , cnt_unique_songs)
            

            return ans % mod
        
        return dp(0 , 0)




