#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>
#include <queue>

using boardType = std::vector<std::vector<int>>;
using pairVectorType = std::vector<std::pair<int, int>>;
int bfs(boardType& board, pairVectorType& viruses, pairVectorType& wall_candidates,
        pairVectorType wallSelects)
{
    // 시작
    for(auto&& i : wallSelects)
    {
        auto [y, x] = i;
        board[y][x] = 1;
    }

    int N = static_cast<int>(board.size());
    int M = static_cast<int>(board[0].size());

    // std::cout << N << M << std::endl;

    bool visited[N][M];
    int unSafeCount = 0;
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    
    memset(visited, false, sizeof(visited));
    std::queue<std::pair<int, int>> q;

    for(auto&& item : viruses)
    {
        auto [y,x] = item;
        if(visited[y][x]) continue;

        q.push({y, x});
        visited[y][x] = true;
        ++unSafeCount;

        while(!q.empty())
        {
            auto [y, x] = q.front();
            q.pop();
            
            for(int i=0; i<4; i++)
            {
                int ddy = y + dy[i];
                int ddx = x + dx[i];
                if(0 <= ddx && ddx < M && 0 <= ddy && ddy < N)
                {
                    if(board[ddy][ddx] != 1 && !visited[ddy][ddx])
                    {
                        visited[ddy][ddx] = true;
                        ++unSafeCount;
                        q.push({ddy, ddx});
                    }
                }
            }
        }
    }

    // 원복
    for(auto&& i : wallSelects)
    {
        auto [y, x] = i;
        board[y][x] = 0;
    }
    // std::cout << wall_candidates.size() + viruses.size() - unSafeCount << std::endl;
    return wall_candidates.size() - 3 + viruses.size() - unSafeCount;
}
int main()
{
    int N, M;
    std::cin >> N >> M;
    boardType board(std::vector(N, std::vector<int>(M, 0)));
    pairVectorType viruses;
    pairVectorType wall_candidates;
    
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            int temp;
            std::cin >> temp;
            board[i][j] = temp;

            if(temp == 0) wall_candidates.push_back({i, j});
            if(temp == 2) viruses.push_back({i, j});
            
        }
    }

    auto wc_size = static_cast<int>(wall_candidates.size());
    int answer = 0;
    // 3중 포문
    for(int i=0; i<wc_size; i++)
    {
        for(int j=i+1; j<wc_size; j++)
        {
            for(int k=j+1; k<wc_size; k++)
            {
                pairVectorType wallSelects = 
                {
                    wall_candidates[i],
                    wall_candidates[j],
                    wall_candidates[k]
                };
                int result = bfs(board, viruses, wall_candidates, wallSelects);
                answer = std::max(result, answer);
            }
        }
    }

    std::cout << answer << std::endl;
}