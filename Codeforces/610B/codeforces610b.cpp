#include <iostream>
#include <deque>
#include <string>

int paint(int length, int jars[])
{
	int jarsFull = length;
	int squaresPainted = 0;
	int smallest = 10000;
	int smallestPlace = 0;
	for (int i = 0; i < length; ++i)
	{
		if (jars[i] < smallest)
		{
			smallest = jars[i];
			smallestPlace = i;
		}
	}
	std::cout << smallestPlace << std::endl;
	while (jarsFull > 0)
	{
		for (int i = smallestPlace + 1; i < length; ++i)
		{
			if (jars[i] == 0)
			{
				return squaresPainted;
			}
			else if (jars[i] > 0)
			{
				jars[i] -= 1;
				squaresPainted += 1;
			}
		}
		for (int i = 0; i < length; ++i)
		{
			if (jars[i] == 0)
			{
				return squaresPainted;
			}
			else if (jars[i] > 0)
			{
				jars[i] -= 1;
				squaresPainted += 1;
			}
		}
	}
	return squaresPainted;
}

int main()
{
	int* list;
	int n;
	std::cin >> n;
	list = new int[n];
	for (int i = 0; i < n; ++i)
	{
		std::cin >> list[i];
	}
	std::cout << paint(n, list) << std::endl;
}