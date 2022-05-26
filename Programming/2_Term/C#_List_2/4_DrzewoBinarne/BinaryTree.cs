namespace DrzewoBinarne
{
    internal class BinaryTree
    {
        private BinaryNode? root;

        public void AddNode(int value)
        {
            Queue<BinaryNode?> queue = new Queue<BinaryNode?>();
            BinaryNode? node;

            if(this.root == null)
            {
                this.root = new BinaryNode(value);
                return;
            }

            queue.Enqueue(root);

            while (true)
            {
                node = queue.Dequeue();
                if (node.Left == null)
                {
                    node.Left = new BinaryNode(value);
                    return;
                }
                if (node.Right == null)
                {
                    node.Right = new BinaryNode(value);
                    return;
                }
                queue.Enqueue(node.Left);
                queue.Enqueue(node.Right);
            }
        }

        public List<int> PreOrder(BinaryNode? node = null)
        {
            List<int> result = new List<int>();

            if (node == null)
            {
                if(this.root == null)
                {
                    return result;
                }
                node = this.root;
            }

            result.Add(node.Value);

            if(node.Left != null)
            {
                result.AddRange(PreOrder(node.Left));
            }

            if(node.Right != null)
            {
                result.AddRange(PreOrder(node.Right));
            }

            return result;
        }

        public int CountNodes()
        {
            return this.PreOrder().Count;
        }

        public int CountLevels()
        {
            if(this.root == null)
            {
                return 0;
            }
            return (int)(1 + Math.Floor(Math.Log(CountNodes(), 2)));
        }

        public int Sum()
        {
            List<int> numbers = this.PreOrder();
            if(numbers.Count == 0)
            {
                return 0;
            }
            int sum = 0;

            foreach (int number in numbers)
            {
                sum += number;
            }

            return sum;
        }

        public int Min()
        {
            List<int> numbers = this.PreOrder();
            if (numbers.Count == 0)
            {
                return 0;
            }
            int min = numbers[0];

            foreach (int number in numbers)
            {
                if (number < min)
                {
                    min = number;
                }
            }

            return min;
        }

        public int Max()
        {
            List<int> numbers = this.PreOrder();
            if (numbers.Count == 0)
            {
                return 0;
            }
            int max = numbers[0];

            foreach (int number in numbers)
            {
                if (number > max)
                {
                    max = number;
                }
            }

            return max;
        }
    }
}
