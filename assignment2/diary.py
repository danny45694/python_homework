import traceback

try:
    with open("diary.txt", "a") as file:
        prompt = "What did you do today? "
        while True:
            txt_data = input(prompt)
            file.write(txt_data + "\n")

            if txt_data.strip().lower() == "done for now":
                break

            prompt = "What else? "
except Exception as e:
    import traceback
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
