namespace Sortowanie
{
    internal static class Sort
    {
        internal static void BubbleSort(int[] tab)
        {
            int length = tab.Length;
            bool sorted;
            int temp;

            while (length > 1)
            {
                sorted = true;
                for (int i = 0; i < length - 1; i++)
                {
                    if (tab[i] > tab[i + 1])
                    {
                        temp = tab[i];
                        tab[i] = tab[i + 1];
                        tab[i + 1] = temp;
                        sorted = false;
                    }
                }

                if (sorted)
                {
                    break;
                }

                length--;
            }
        }

        internal static void QuickSort(int[] tab, int left = 0, int right = -1)
        {
            if(right == -1)
            {
                right = tab.Length - 1;
            }
            
            if (left > right)
            {
                return;
            }

            int indexLeft = left - 1, indexRight = right + 1;
            int pivot = tab[left];
            int temp;

            while (true)
            {
                while (pivot > tab[++indexLeft]);
                while (pivot < tab[--indexRight]);

                if (indexLeft <= indexRight)
                {
                    temp = tab[indexLeft];
                    tab[indexLeft] = tab[indexRight];
                    tab[indexRight] = temp;
                }
                
                else
                {
                    break;
                }
            }

            if (indexRight > left)
            {
                QuickSort(tab, left, indexRight);
            }
            
            if (indexLeft < right)
            {
                QuickSort(tab, indexLeft, right);
            }
        }
    }
}
