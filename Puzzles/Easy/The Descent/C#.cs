using System;

class Player
{
    static void Main(string[] args)
    {
        // game loop
        while (true)
        {
            // Define required variables.
            int maxVal = 0;
            int maxIndex = 0;
            
            // Find the index of the max height and store in max_index.
            for (int i = 0; i < 8; i++)
            {
                int mountainH = int.Parse(Console.ReadLine());
                if (mountainH > maxVal){
                    maxVal = mountainH;
                    maxIndex = i;
                }
            }
            // Output the index of the mountain to fire on.
            Console.WriteLine(maxIndex); 
        }
    }
}
