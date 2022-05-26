namespace Kolejka
{
    internal class MyQueueGetThread
    {
        private Thread t;
        private MyQueue queueueue;
        private bool _continue = true;

        public MyQueueGetThread(MyQueue queueueue)
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
            while (_continue)
            {
                Console.WriteLine($"MyQueueGetThread: {queueueue.GetValue()}");
                Thread.Sleep(3000);
            }
        }
    }
}
