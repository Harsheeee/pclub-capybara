#include <bits/stdc++.h>
using namespace std;
const int INF = 2e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    vector<int> best(n, INF);
    deque<int> maxQ, minQ;

    int L = 0;
    for (int R = 0; R < n; ++R) {
        while (!maxQ.empty() && a[maxQ.back()] <= a[R]) maxQ.pop_back();
        maxQ.push_back(R);
        while (!minQ.empty() && a[minQ.back()] >= a[R]) minQ.pop_back();
        minQ.push_back(R);

        // shrink
        while (a[maxQ.front()] - a[minQ.front()] > R - L) {
            if (maxQ.front() == L) maxQ.pop_front();
            if (minQ.front() == L) minQ.pop_front();
            ++L;
        }

        // harmonic check
        if (a[maxQ.front()] - a[minQ.front()] == R - L) {
            int len = R - L + 1;
            for (int i = L; i <= R; ++i)
                if (best[i] > len) best[i] = len;
        }
    }

    while (q--) {
        int k; cin >> k; --k;          // 0-indexed
        int ans = best[k];
        cout << (ans == INF ? -1 : ans) << '\n';
    }
    return 0;
}
