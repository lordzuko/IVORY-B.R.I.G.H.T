#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <assert.h>

using namespace std;

typedef unordered_map<string,string> stringmap;


//This function takes string and return its hash value
size_t create_hash(string password)
{
	stringmap mymap;
	stringmap::hasher fn = mymap.hash_function();
	return fn(password);
}




//this function will return true if user is already registered
int is_user_registered(string username,string password)
{
	string user_name,pass_word;
	ifstream file;
	file.open("login.txt",ios::in);
	
	while(!file.eof())
	{
		file >> user_name >> pass_word;
		if(user_name == username)
		{
			cout <<"\nUsername already exists\nEnter different username\n";
			return true;
		}
		else
			continue;
	}	
	return false;
}




// this function registers new user and add its details to file
void register_user(string username, string password){
	
	ofstream file;
	// opening file login.txt in append mode
        file.open("login.txt",ios::app);
	//assert(file != NULL);
        file << username << " "<< create_hash(password) << endl;
        
        file.close();
}




// this function checks for validity of username and password the player entered
bool check_if_valid(string username, string password)
{
	string user_name ;
	size_t pass_word;

	ifstream file;
	file.open("login.txt",ios::in);

	while(!file.eof())
	{
		file >> user_name >> pass_word;
		if(user_name == username && pass_word == create_hash(password))
		{
			cout << "\nusername and Password validated\nLogging U in the game\n";
			return true;
		}
		else 
			continue;
	}
		
	file.close();
	cout << "\nThe username or password u entered is not valid\n"; 
	
	return false;	
}




void login()
{
	string password,username;

	// User getline so that even spaces can be included while entering username and password
	// But there should not be any spaces in username
	
	char option ;
	cout << "New?? (y/n)\n";
	option = getchar();

	switch(option)
	{
		case 'y':	do{
					cout << "Username: ";
			 		cin >> username;
					cout << "Password: ";
					cin >> password;
				}while(is_user_registered(username, password));
				
				register_user(username,password);

				cout << "\nU r registered\n********** Enjoy the game :D **********\n"; 

				// enter here the function to start the game

	
				break;
	
		case 'n':       
				do{
					cout << "Username:";
					cin >> username;
					cout << "Password:";
					cin >> password;
				}while(!check_if_valid(username,password));	
				
				break;
		default:	cout << "Oops!!!  U pressed wrong key\n";				
				break;
	}
	
}




int main()
{
	login();
	return 0;
}
