#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

template<typename T>
using vector = std::vector<T>;

struct Pos3D
{
    int i, j, k;
public:
    Pos3D()
    : i(0), j(0), k(0)
    {

    }

    Pos3D(int i, int j, int k)
    : i(i), j(j), k(k)
    {

    }

};

int bfs(vector< vector<std::string> >& buildings, vector<vector<vector<bool>>>& visited, Pos3D sp,
        int L, int R, int C)
{
    std::deque<std::tuple<Pos3D, int>> dq; // 위치와 탐색횟수
    auto [i, j, k] = sp;
    visited[i][j][k] = true;
    dq.emplace_back(std::make_tuple(Pos3D(i, j, k), 0));
    
    int dx[] = {-1, 1}; 
    int dy[] = {0, 1, 0, -1}; 
    int dz[] = {1, 0, -1, 0};
     


    while(!dq.empty())
    {
        auto [pos, count] = dq.front();
        auto [x, y, z] = pos;
        dq.pop_front();


        // std::cout << x << " " << y << " " << z << " " << count << std::endl;
        
        
        for(int i=0; i<4; i++) // 북동서남
        {
            int ddy = y + dy[i];
            int ddz = z + dz[i];
            
            if(0 <= ddy && ddy < R && 0 <= ddz && ddz < C && !visited[x][ddy][ddz]) // 범위
            {
                if(buildings[x][ddy][ddz] == '#')
                {
                    continue;
                }
                else if(buildings[x][ddy][ddz] == '.')
                {
                    visited[x][ddy][ddz] = true;
                    dq.emplace_back(std::make_tuple(Pos3D(x,ddy,ddz), count+1));
                }
                else if(buildings[x][ddy][ddz] == 'S')
                {
                    return count+1;
                }
            }
        }

        for(int i=0; i<2; i++) // 상하
        {
            int ddx = x + dx[i];

            if(0 <= ddx && ddx < L && !visited[ddx][y][z])
            {
                if(buildings[ddx][y][z] == '#')
                {
                    continue;
                }
                else if(buildings[ddx][y][z] == '.')
                {
                    visited[ddx][y][z] = true;
                    dq.emplace_back(std::make_tuple(Pos3D(ddx,y,z), count+1));
                }
                else if(buildings[ddx][y][z] == 'S')
                {
                    return count+1;
                }
            }
        }

    }

    // 모두 비워졌는데도 S를 못찾았으면 못찾음
    return -1;
    
}
int main()
{
    while(true)
    {
        int L, R, C = 0;
        std::cin >> L >> R >> C;
        if(L == 0 && R == 0 && C == 0)
        {
            break;
        }
        Pos3D startPos;
        vector<vector<vector<bool>>> visited(L, vector<vector<bool>>(R, vector<bool>(C, false))); 
        // vector<vector<vector<bool>>> visited;
        
        vector< vector<std::string>> buildings(L); // buildings[0] : 1층

        for(int i=0; i<L; i++)
        {
            for(int j=0; j<R; j++)
            {
                std::string rowInput;
                std::cin >> rowInput;

                buildings[i].push_back(std::move(rowInput));
                
                const std::string b_str = buildings[i].back();
                for(int k=0; k<static_cast<int>(b_str.size()); k++)
                {
                    if(b_str[k] == 'E')
                        startPos = Pos3D(i, j, k);
                }
                
            }
        }

        auto result = bfs(buildings, visited, startPos, L, R, C);
        if(result == -1)
        {
            std::cout << "Trapped!" << std::endl;
        }
        else
        {
            std::cout << "Escaped in " << result << " minute(s)." << std::endl;
        }
    }

}