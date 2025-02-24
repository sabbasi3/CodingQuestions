using System;class Hole1{public static void Play(string[]b){for(int i=0;i<3;i++){if(b[i]=="XXX"||b[0][i]==b[1][i]&&b[1][i]==b[2][i]&&b[0][i]=='X'){Console.Write("X");return;}if(b[i]=="OOO"||b[0][i]==b[1][i]&&b[1][i]==b[2][i]&&b[0][i]=='O'){Console.Write("O");return;}}Console.Write((b[0][0]==b[1][1]&&b[1][1]==b[2][2]||b[0][2]==b[1][1]&&b[1][1]==b[2][0])&&b[1][1]!='.'?b[1][1]:"-");}}



// Non shortened below
using System;

namespace Course
{
    static class Hole1
    {
        public static void Play(string[] board)
        {
            for (int i = 0; i < 3; i++)
            {
                if (board[i] == "XXX" || (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == 'X')) 
                { 
                    Console.WriteLine("X"); 
                    return; 
                }
                if (board[i] == "OOO" || (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == 'O')) 
                { 
                    Console.WriteLine("O"); 
                    return; 
                }
            }
            if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] || 
                 board[0][2] == board[1][1] && board[1][1] == board[2][0]) && board[1][1] != '.')
            {
                Console.WriteLine(board[1][1]);
                return;
            }
            Console.WriteLine("-");
        }
    }
}