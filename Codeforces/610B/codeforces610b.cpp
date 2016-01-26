#include <iostream>

int paint(int length, long jars[])
{
	int jarsFull = length;
	long squaresPainted = 0;
	long smallest = jars[0];
	int smallestPlace = 0;
	for (int i = 0; i < length; ++i)
	{
		if (jars[i] < smallest)
		{
			smallest = jars[i];
			smallestPlace = i;
		}
		else if (jars[i] == smallest)
		{
			smallestPlace = i;
		}
	}
	squaresPainted += smallest * jarsFull;
	for (int i = 0; i < length; ++i)
	{
		jars[i] -= smallest;
	}
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
	return squaresPainted;
}

int main()
{
	long* list;
	int n;
	std::cin >> n;
	list = new long[n];
	for (int i = 0; i < n; ++i)
	{
		std::cin >> list[i];
	}
	std::cout << paint(n, list) << std::endl;
}