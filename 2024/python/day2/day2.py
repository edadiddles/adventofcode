from copy import copy


with open("input1.txt") as f:
    contents = f.read()

reports = contents.split("\n")

safe_rpt_cnt = 0
for report in reports:
    splt_report = report.strip().split(" ")
    try:
        report_data = [int(d) for d in splt_report]
        print(report_data)
    except Exception as e:
        print(e)
        continue
    
    s1_report_data = copy(report_data)
    s1_report_data.sort(reverse=False)
    s2_report_data = copy(report_data)
    s2_report_data.sort(reverse=True)
    if report_data != s1_report_data and report_data != s2_report_data:
        continue

    diff_arr = []
    for i in range(1, len(report_data)):
        diff_arr.append(abs(report_data[i-1] - report_data[i]))

    diff_arr.sort()
    if diff_arr[0] >= 1 and diff_arr[-1] <= 3:
        safe_rpt_cnt += 1

print(f"num of safe reports: {safe_rpt_cnt}")
