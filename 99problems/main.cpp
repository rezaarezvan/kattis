#include <iostream>
#include <set>

using namespace std;

int main() {
  int N, Q;
  cin >> N >> Q;

  multiset<int> diff;
  for (int i = 0, d; i < N; i++) {
    cin >> d;
    diff.insert(d);
  }

  for (int i = 0; i < Q; i++) {
    int T, di;
    cin >> T >> di;

    if (T == 1) {
      auto it = diff.upper_bound(di);
      if (it == diff.end()) {
        cout << "-1\n";
        continue;
      }
      cout << *it << "\n";
      diff.erase(it);
    } else {
      auto it = diff.upper_bound(di);
      if (it == diff.begin()) {
        cout << "-1\n";
        continue;
      }
      cout << *prev(it) << "\n";
      diff.erase(prev(it));
    }
  }

  return 0;
}
