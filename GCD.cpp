#include <iostream>
using namespace std;
 

int main()
{


 int r1 = 2740;
 int r2 = 1760;
 int s1 = 1;
 int s2 = 0;
 int t1 = 0;
 int t2 = 1; 
 cout << "enter your firt number   : "; 
 cin >> r1 ;
 cout << "enter your second number : "; 
 cin >> r2;


while (r2 > 0)
{   
	int q = r1 / r2;
    int r = r1 % r2; 
	r1 = r2;
    r2 = r;
    cout << "Q = "<< q << endl;
    cout << "r =" << r << endl; 
    cout << "r1 = "<< r1 << endl;
    cout << "r2 = "<< r2 << endl;
    cout << "---------------------------------" << endl;
    int s = s1 - q * s2 ;
    s1 = s2; 
    s2 = s;
    int t = t1 - q * t2;
    t1 = t2 ;
    t2 = t ;
    cout << "S1 = " << s1 << endl;
    cout << "S2 = "<< s2 << endl;
    cout << "S = " << s << endl;
    cout << "----------------------" << endl;
    cout << "T1 = "<< t1 << endl;
    cout << "T2 = "<< t2 << endl;
    cout << "T = " << t << endl;
    cout << "----------------------" << endl;
} 
cout <<"this is your S :" << s1 << endl ;
 cout << "this is yout T : "<< t1 << endl;
cout << "this is your GCD :  "<< r1 << endl;
return 0;
}
