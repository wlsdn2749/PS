#include <iostream>
#include <queue>
#include <algorithm>
#include <fstream>




void insertNum(std::priority_queue<int, std::vector<int>, std::less<int>>& max_heap,
               std::priority_queue<int, std::vector<int>, std::greater<int>>& min_heap,
               int x)
{
    if(max_heap.empty())
    {
        max_heap.push(x);
        return;
    }

    // 1) 값 분배: max의 top과 비교해 좌/우 힙 결정
    if (x <= max_heap.top()) max_heap.push(x);
    else                     min_heap.push(x);

    // 2) 리밸런싱: max가 항상 min과 같거나 1개 더 많게
    if (max_heap.size() < min_heap.size()) {
        max_heap.push(min_heap.top());
        min_heap.pop();
    } else if (max_heap.size() > min_heap.size() + 1) {
        min_heap.push(max_heap.top());
        max_heap.pop();
    }
    
}

int getMedium(std::priority_queue<int, std::vector<int>, std::less<int>>& max_heap)
{
    return max_heap.top();
}
int main()
{
    // std::ifstream ifs;
    // ifs.open("2696.in");
    std::cin.tie(0);
    std::cout.tie(0);
    std::ios_base::sync_with_stdio(false);

    int T;
    std::cin >> T;

    for(int i=0; i<T; i++)
    {
        int M;
        int count = 0;
        std::priority_queue<int, std::vector<int>, std::less<int>> max_heap; // max heap
        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap; // min heap


        std::cin >> M;
        if(M%2 == 0) std::cout << M/2 << std::endl;
        else std::cout << M/2 + 1 << std::endl;

        for(int j=0; j<M; j++)
        {
            int temp;
            std::cin >> temp;
            insertNum(max_heap, min_heap, temp);
            
            if((++count) % 2 == 1) 
                std::cout << getMedium(max_heap) << " ";
            if(count % 20 == 0 || j == M-1)
                std::cout << "\n";
    
        }
    }
}