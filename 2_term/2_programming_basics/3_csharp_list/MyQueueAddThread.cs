namespace Kolejka
{
    internal class MyQueueAddThread
    {
        private Thread t;
        private MyQueue queueueue;
        private bool _continue = true;

        public MyQueueAddThread(MyQueue queueueue)
        {
            this.queueueue = queueueue;
            t = new Thread(new ThreadStart(QueueAdd));
        }

        public void Start() 
        {
            _continue = true;
            t.Start();
        }

        public void Stop()
        {
            _continue = false;
            t.Join();
        }

        private void QueueAdd()
        {
            Random random = new Random();

            while(_continue)
            {
                int r = random.Next(101);
                Console.WriteLine($"MyQueueAddThread: {r}");
                queueueue.AddValue(r);

                Thread.Sleep(8000);
            }
        }
    }
}
