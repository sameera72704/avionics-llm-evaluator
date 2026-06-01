from src.evaluators.static_checker import *

sample_code = """

float clamp_altitude(float altitude)
{
    if (altitude > 50000)
        return 50000;

    return altitude;
}

"""

forbidden = [
    "malloc",
    "free",
    "printf"
]

keywords = [
    "float",
    "return",
    "if"
]

print(
    check_forbidden_patterns(
        sample_code,
        forbidden
    )
)

print(
    check_safety_keywords(
        sample_code,
        keywords
    )
)