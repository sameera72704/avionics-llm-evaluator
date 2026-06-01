from src.compilers.c_runner import *

c_code = """

float clamp_altitude(float altitude)
{
    return altitude;
}

"""

test_harness = """

#include <stdio.h>

int main()
{
    printf("HARNESS_OK\\n");
    return 0;
}

"""

result = compile_and_run_c(
    c_code,
    test_harness
)

print(result)