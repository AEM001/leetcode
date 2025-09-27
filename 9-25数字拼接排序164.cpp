#include<vector>
#include<string>
        
class Solution {
    public:
        string crackPassword(vector<int>& password) {
            for (int i=0;i<password.size();i++)
            {
                for(int j=0;j<password.size()-1;j++)
                {
                    if not(compare(password[j],password[j+1]))
                    {swap(password[j],password[j+1]);}
                }
            }
            string res="";
            for(int i=0;i<password.size();++i)
            {
                res+=to_string(password[i]);
            }
            return res;
            
        }
        bool compare(int a,int b)
        {
            if (to_string(a)+to_string(b)<to_string(b)+to_string(a))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    };