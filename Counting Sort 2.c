
#include<stdio.h>

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}


int partition (int arr[], int low, int high)
{
	int pivot = arr[high];
	int i = (low - 1); 

	for (int j = low; j <= high- 1; j++)
	{
		
		if (arr[j] <= pivot)
		{
			i++; 
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}


void Sort(int arr[], int low, int high)
{
	if (low < high)
	{
	
		int pi = partition(arr, low, high);
		Sort(arr, low, pi - 1);
		Sort(arr, pi + 1, high);
	}
}

void printArray(int arr[], int size)
{
	int i;
	for (i=0; i < size; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
	Sort(arr, 0, n-1);
	printArray(arr, n);
	return 0;
}
