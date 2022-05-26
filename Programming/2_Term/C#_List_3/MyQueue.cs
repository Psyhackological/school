namespace Kolejka
{
    internal class MyQueue
    {
        private int[] _tablicaIntow;
        private volatile int _count;

        public MyQueue(int size)
        {
            _tablicaIntow = new int[size];
            _count = 0;
        }

        public void AddValue(int a)
        {
            if(_count < _tablicaIntow.Length)
            {
                Console.WriteLine($"AddValue: {a}");
                _tablicaIntow[_count++] = a;
            }
        }

        public int? GetValue()
        {
            if(_count <= 0)
            {
                return null;
            }

            _count--;
            int first = _tablicaIntow[0];

            _tablicaIntow = _tablicaIntow.Skip(1).ToArray();

            Console.WriteLine($"GetValue: {first}");
            return first;
        }
    }
}
