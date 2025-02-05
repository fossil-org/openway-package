from openway import Package, INIT

def main():
    package = Package(
        name="package",
        version=INIT
    )

    exec(package.get_fc("main.py"))
    # note: executes code in package/init/main.py
    # note: fc means file contents

if __name__ == "__main__":
    main()