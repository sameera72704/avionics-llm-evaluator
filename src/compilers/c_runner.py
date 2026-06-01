import subprocess
import tempfile
import os


COMMON_HEADERS = """

#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

"""


def compile_and_run_c(
        c_code,
        test_harness
):

    combined = (

        COMMON_HEADERS

        +

        "\n"

        +

        c_code

        +

        "\n\n"

        +

        test_harness

    )

    with tempfile.NamedTemporaryFile(
        suffix=".c",
        delete=False,
        mode="w"
    ) as src:

        src.write(combined)

        src_path = src.name

    binary_path = src_path.replace(
        ".c",
        ".out"
    )

    compile_result = subprocess.run(

        [
            "gcc",
            "-Wall",
            "-o",
            binary_path,
            src_path
        ],

        capture_output=True,
        text=True
    )

    result = {

        "compiled":
        compile_result.returncode == 0,

        "compile_errors":
        compile_result.stderr,

        "output": "",

        "run_errors": ""

    }

    if result["compiled"]:

        run_result = subprocess.run(

            [binary_path],

            capture_output=True,

            text=True
        )

        result["output"] = run_result.stdout

        result["run_errors"] = run_result.stderr

    os.unlink(src_path)

    if os.path.exists(binary_path):

        os.unlink(binary_path)

    return result