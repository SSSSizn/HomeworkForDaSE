def count_hours_in_txt(txt_filename):
    hours_count = {str(hour).zfill(2): 0 for hour in range(24)}

    with open(txt_filename, 'r') as file:
        for i, line in enumerate(file):
            if i == 0 or '?' in line:
                continue

            clean_line = line.strip()

            try:
                hour_str = clean_line[:2]
                hours_count[hour_str] += 1
            except KeyError:
                print(f"Ignoring line {i+1} due to unexpected format.")

    return hours_count


txt_filename = 'newtime.txt'
result = count_hours_in_txt(txt_filename)

for hour, count in result.items():
    print(f"{hour}时出现的次数：{count}次")
