#include <iostream>
#include <cmath>
#include <windows.h>
#include <vector>
#include <stdlib.h>
#include <time.h>
// #include "matplotlibcpp.h"

using namespace std;
// namespace plt = matplotlibcpp;

int prob1()
{
    int x = 10;
    float y = 4.12;

    float Addition = x + y;
    float Subtraction = x - y;
    float Multiplication = x * y;
    float Division = x / y;
    float Exponentiation = exp(x);

    cout << "Addition=" << Addition;
    cout << "\nSubtraction=" << Subtraction;
    cout << "\nMultiplication=" << Multiplication;
    cout << "\nDivision=" << Division;
    cout << "\nExponentiation=" << Exponentiation;
    cout << endl;
    return 0;
}

int prob2()
{
    int age;
    cout << "Please enter your age:\t";
    cin >> age;
    if (age < 18)
    {
        cout << "you're a Minor";
    }
    else if ((18 <= age) && (age <= 65))
    {
        cout << "you're an Adult";
    }
    else if (65 < age)
    {
        cout << "you're a Senior";
    }
    else
    {
        cout << "invalid input";
    }
    cout << endl;
    return 0;
}

int prob3()
{
    int n = 12;
    int fib[n];
    int first = 0, second = 1;
    for (int i = 0; i < n; i++)
    {
        fib[i] = first;
        fib[i + 1] = second;
        int New = first + second;
        first = second;
        second = New;
    }

    for (int i = 0; i < n; i++)
    {
        cout << fib[i];
        if (i != n - 1)
        {
            cout << ", ";
        }
    }
    cout << endl;
    return 0;
}

int prob4(int n, float d, string word)
{
    for (int i = 0; i < n; i++)
    {
        cout << word;
        if (i != n - 1)
        {
            cout << " - ";
            Sleep(1000*d);
        }
    }
    cout << endl;
    return 0;
}

// int prob5()
// {
//     srand(time(0));
//     vector<float> t;
//     vector<float> wave_1, wave_2;
//     for (int i = 0; i < 1000; i++)
//     {
//         t.push_back(i / 100.0);
//         wave_1.push_back(sin(t[i]) + float(rand()) / float(RAND_MAX) * 0.1);
//         wave_2.push_back(2 * sin(1.5 * t[i]) + float(rand()) / float(RAND_MAX) * 0.35);
//     }

//     plt::figure_size(1300, 400);
//     plt::plot(t, wave_1, "r", {{"label", "y_1 = sin(t)"}});
//     plt::plot(t, wave_2, "b", {{"label", "y_2 = 2*sin(1.5t)"}});

//     plt::title("Different Sinusoidal Waves Subject to Noise");
//     plt::xlabel("time (s)");
//     plt::ylabel("Amplitude");
//     plt::grid(true);
//     plt::legend();
//     plt::show();
//     return 0;
// }


int main()
{
    cout << "\nprob1 - Arithmetic Operations\n";
    prob1();
    cout << "\nprob2 - Conditionals\n";
    prob2();
    cout << "\nprob3 - Loops\n";
    prob3();
    cout << "\nprob4 - Functions\n";
    prob4(5, 1, "Test");
    cout << "\nprob5 - Visualization";
    // prob5();
    return 0;
}
