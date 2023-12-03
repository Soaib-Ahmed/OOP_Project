//Bismillahir Rahmanir Rahim
//Soaib Ahmed...

#include <bits/stdc++.h>

using namespace std;

#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define faster  ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define  ll       long long int
#define  ld       long long double
#define  int_out(x) printf("%d",x)
#define  sp       " "
#define  pb       push_back
#define  cinv     for(auto &i:v) cin >> i;
#define  vi       vector<int>
#define  vii      vector<ll>
#define  cout(v)  for(auto e:v) cout << e << sp;
#define  ma_x     100000008
#define  yes      cout << "YES" << endl
#define  no       cout << "NO" << endl
#define  case     "Case " << test++ << ": "
#define  all(v)   v.begin(), v.end()
#define  tst      int tst; int test=1; cin >> tst; while(tst--)
#define  Faster   ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define  nl       "\n"




//Driver code


int main() 
{
    int t;      cin >> t;

    while (t--) 
    {
        cout << fixed << setprecision(10);
        int p, q;       in >> p >> q;
        int a, b;       cin >> a >> b;
        int c, d;       cin >> c >> d;
        double ans = 1e3;
        double r = sqrt((a - c) * (a - c) * 1.000 + (b - d) * (b - d) * 1.000) / 2;
        double xx = sqrt((p - c) * (p - c) * 1.000 + (q - d) * (q - d) * 1.000);
        double yy = sqrt((p - a) * (p - a) * 1.000 + (q - b) * (q - b) * 1.000);

        if (xx <= r || yy <= r) ans = min(ans, r);
        if (r * 2 <= 2 * xx) ans = min(ans, xx);
        if (r * 2 <= 2 * yy) ans = min(ans, yy);

        cout << ans << endl;
    }

    return 0;
}

