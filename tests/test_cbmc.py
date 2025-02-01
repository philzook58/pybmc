import pybmc
import pytest
import subprocess

example1 = """
int main(int argc, char *argv[]) {
  int arr[] = {0, 1, 2, 3};
  __CPROVER_assert(arr[3] != 3, "expected failure: arr[3] == 3");
}
"""


def test_run_cbmc():
    res = pybmc.run_cbmc_string(example1.encode())
    with pytest.raises(subprocess.CalledProcessError):
        res.check_returncode()
    js = pybmc.symtab_of_C(example1.encode())
