namespace Kolejka
{
    internal class Program
    {
        static void Main()
        {
            int add_threads, get_threads;

            Console.WriteLine("Ile ma byc watkow MyQueueAddThread?");
            add_threads = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Ile ma byc watkow MyQueueGetThread?");
            get_threads = Convert.ToInt32(Console.ReadLine());

            MyQueue queueueue = new MyQueue(100);
            MyQueueAddThread[] addTab = new MyQueueAddThread[add_threads];
            MyQueueGetThread[] getTab = new MyQueueGetThread[get_threads];

            for(int i = 0; i < addTab.Length; i++)
            {
                addTab[i] = new MyQueueAddThread(queueueue);
                addTab[i].Start();
            }

            for(int i = 0; i < getTab.Length; i++)
            {
                getTab[i] = new MyQueueGetThread(queueueue);
                getTab[i].Start();
            }

            Console.ReadLine();
            
            for (int i = 0; i < addTab.Length; i++)
            {
                addTab[i].Stop();
            }

            for (int i = 0; i < getTab.Length; i++)
            {
                getTab[i].Stop();
            }
        }
    }
}