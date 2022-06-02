import subprocess


def test_happy_case_example():
    cwd = "positive_cases/happy_case_example"
    # Build
    subprocess.check_call(["poetry", "blixbuild"], cwd=cwd)

    # Validate wheel
    subprocess.check_call(["poetry", "blixvalidatewheel", "dist/blixexample-0.1.0-py3-none-any.whl"], cwd=cwd)


def test_negative_missing_from_project():
    cwd = "negative_cases/missing_from_project"
    # Validate wheel fails
    proc = subprocess.Popen(
        ["poetry", "blixvalidatewheel", "dist/blixexample-missing_from_project.whl"], cwd=cwd, stderr=subprocess.PIPE
    )
    stdout, stderr = proc.communicate()
    assert stdout is None
    stderr = stderr.decode()
    assert "RuntimeError" in stderr, "Expected error to be RuntimeError"
    assert (
        "Packages in Wheel file are not present in pyproject.toml/poetry.lock: {'nemoize'}" in stderr
    ), "Did not get expected error message!"