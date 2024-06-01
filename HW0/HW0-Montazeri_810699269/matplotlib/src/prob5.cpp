#include <iostream>
#include <vector>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include "matplotlibcpp.h"

using namespace std;
namespace plt = matplotlibcpp;

int prob5()
{
    srand(time(0));
    vector<float> t;
    vector<float> wave_1, wave_2;
    for (int i = 0; i < 1000; i++)
    {
        t.push_back(i / 100.0);
        wave_1.push_back(sin(t[i]) + float(rand()) / float(RAND_MAX) * 0.1);
        wave_2.push_back(2 * sin(1.5 * t[i]) + float(rand()) / float(RAND_MAX) * 0.35);
    }

    plt::figure_size(1300, 400);
    plt::plot(t, wave_1, "r", {{"label", "y_1 = sin(t)"}});
    plt::plot(t, wave_2, "b", {{"label", "y_2 = 2*sin(1.5t)"}});

    plt::title("Different Sinusoidal Waves Subject to Noise");
    plt::xlabel("time (s)");
    plt::ylabel("Amplitude");
    plt::grid(true);
    plt::legend();
    plt::show();
    return 0;
}

int main()
{
    prob5();
    return 0;
}