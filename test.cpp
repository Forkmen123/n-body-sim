#include <iostream>

namespace First
{
	int var = 10;
}


namespace First
{
	int var = 20;
}

int main()
{
std::cout << "value in First namespace: " << First::var << std::endl;
std::cout << "Value in Second namespace: " << Second::var << std::endl;




}
