 
#include <iostream>
#include<string>
#include<unordered_map>

using namespace std;

class User
{
   string user_id;
   string email_id;
   string mobile_no;
   string name;
   
   public:
        User(string uid, string n, string email, string mob)
        {
            
             user_id = uid;
             name = n;
             email_id = email;
             mobile_no = mob;
        }
        string get_user_id()
        {
             return user_id;
        }
       
};