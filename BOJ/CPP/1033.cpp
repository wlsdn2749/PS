#include <iostream>
#include <vector>
#include <utility>
#include <numeric> // std::gcd
using namespace std;

using ll = long long;
using Ratio = pair<ll,ll>; // (분자, 분모)

struct Edge {
    int to;
    ll p, q; // 현재 / 다음 = p / q
};

int N;
vector<vector<Edge>> adj;
vector<Ratio> ratio;
vector<bool> visited;

// DFS로 비율 전파
void dfs(int node, ll num, ll den) {
    visited[node] = true;
    ratio[node] = {num, den};

    for (auto &e : adj[node]) {
        if (!visited[e.to]) {
            // 다음 노드 비율 = 현재 노드 비율 × (q/p)
            ll n_num = num * e.q;
            ll n_den = den * e.p;

            ll g = gcd(n_num, n_den);
            n_num /= g;
            n_den /= g;

            dfs(e.to, n_num, n_den);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    adj.resize(N);
    ratio.resize(N);
    visited.resize(N, false);

    for (int i = 0; i < N - 1; i++) {
        int a, b;
        ll p, q;
        cin >> a >> b >> p >> q;
        adj[a].push_back({b, p, q});
        adj[b].push_back({a, q, p});
    }

    // 0번 노드를 기준으로 시작
    dfs(0, 1, 1);

    // 모든 분모의 LCM 계산
    ll lcm_all = 1;
    for (int i = 0; i < N; i++) {
        lcm_all = lcm(lcm_all, ratio[i].second);
    }

    // 정수로 변환
    vector<ll> result(N);
    for (int i = 0; i < N; i++) {
        result[i] = ratio[i].first * (lcm_all / ratio[i].second);
    }

    ll g_all = result[0];
    for (int i = 1; i < N; i++) {
        g_all = gcd(g_all, result[i]);
    }
    for (int i = 0; i < N; i++) {
        cout << result[i] / g_all << " ";
    }
    cout << "\n";

    return 0;
}