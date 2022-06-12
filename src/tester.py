import os
import PAss

# Get Test source files
path = os.path.join(os.path.dirname(__file__), "../tests/in/")
test_files = os.listdir(path)

# Run Tests
for test_file in test_files:
    print(f"Running Test: {test_file}")
    path_in = os.path.join(os.path.dirname(__file__),
                           "../tests/in/") + test_file
    test = PAss.read_input_file(path_in)

    path_out = os.path.join(os.path.dirname(__file__),
                            "../tests/out/") + test_file.replace('.pass', '.ass')

    try:
        PAss.compile(test, test_file.replace(".pass", ""), path_out)
        print(f"Success! \n")
    except Exception as e:
        print(f"Test didn't finish. An error occured: \n {e}")
