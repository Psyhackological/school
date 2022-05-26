namespace DrzewoBinarne
{
    internal class BinaryNode
    {
        public int Value { get; set; }
        public BinaryNode? Left { get; set; }
        public BinaryNode? Right { get; set; }

        public BinaryNode(int value)
        {
            this.Value = value;
        }
    }
}