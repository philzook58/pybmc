import subprocess
import tempfile
import json


def hello() -> str:
    return "Hello from pybmc!"


def run_symtab2gb(infile: str, outfile: str) -> None:
    return subprocess.run(["symtab2gb", infile, "-o", outfile], capture_output=True)


def run_cbmc_file(infile: str, *args, **kwargs) -> None:
    return subprocess.run(
        ["cbmc", infile, *args, *[("--" + k, v) for k, v in kwargs.items()]],
        capture_output=True,
    )


def run_cbmc_string(c_string: bytes, *args, **kwargs) -> None:
    with tempfile.NamedTemporaryFile(suffix=".c") as tmp:
        tmp.write(c_string)
        tmp.flush()
        return run_cbmc_file(tmp.name, *args, **kwargs)


def symtab_of_C(c_string: bytes) -> object:
    res = run_cbmc_string(c_string, "--json-ui", "-show-symbol-table")
    res.check_returncode()
    msgs = json.loads(res.stdout)
    symtabs = [msg["symbolTable"] for msg in msgs if "symbolTable" in msg]
    assert len(symtabs) == 1
    return symtabs[0]


def json_of_symtab(symtab) -> None:
    pass
