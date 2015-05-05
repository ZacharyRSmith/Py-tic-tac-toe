from subprocess import Popen, PIPE, STDOUT

f_in = open('in', 'r')        # If you have multiple test-cases, store each
                              # input/expected-output file in a list and iterate
                              # over this snippet.
f_expected = open('out_expected', 'r')  # Correct outputs
expected   = f_expected.read().splitlines()
p = Popen(["python", "../__init__.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate(input=f_in.read())[0].splitlines()

# Validate by comparing the two lists' elements.
assert len(out) == len(expected)
for i in range(len(out)):
    print "out: ", out[i]
    print "expected: ", expected[i]
    assert out[i] == expected[i]