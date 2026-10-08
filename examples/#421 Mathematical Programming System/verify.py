import highspy
solver = highspy.Highs()
solver.setOptionValue("output_flag", False)
assert solver.readModel("hello.mps") == highspy.HighsStatus.kOk
assert solver.run() == highspy.HighsStatus.kOk
assert solver.getModelStatus() == highspy.HighsModelStatus.kOptimal
values = solver.getSolution().col_value
assert len(values) == 13 and all(v == round(v) for v in values)
text = bytes(int(v) for v in values).decode("ascii")
assert text == "Hello, World!"
print(text)
