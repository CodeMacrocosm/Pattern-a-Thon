#include<iostream>
using namespace std;

int main()
{
  int e=9;

  cout<<"\"Upside Down Triangle\":\n\n";

  for(int a=1;a<=5;a++)
 {
    for(int b=0;b<e;b++)
   {
    cout<<"*";  // printing asterisk character
   }
    cout<<endl;
    e=e-2;

      for(int c=0;c<a;c++)
     {
      cout<<" ";  // printing space here
     }

 }
 return 0;
}
