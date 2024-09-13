import pandas as pd
# CSV 파일 경로
csv_file = '1_data.csv'
# CSV 파일 읽기
df = pd.read_csv(csv_file, header=None, encoding='UTF-8')

# 헤더 추가
df.columns = [
    '호선', '역명', '상세위치', '소형(개수)', '중형(개수)', '대형(개수)', '특대형(개수)', '이용요금', '운영사'
]
# HTML 테이블로 변환
html_table = df.to_html(index=False)
# HTML 파일로 저장
with open('1_data.html', 'w', encoding='UTF-8') as file:
    file.write('<!DOCTYPE html>\n<html lang="ko">\n<head>\n')
    file.write('    <meta charset="UTF-8">\n')
    file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    file.write('    <title>CSV 데이터 테이블</title>\n')
    file.write('    <style>\n')
    file.write('        table {\n')
    file.write('            width: 100%;\n')
    file.write('            border-collapse: collapse;\n')
    file.write('        }\n')
    file.write('        th, td {\n')
    file.write('            border: 1px solid black;\n')
    file.write('            padding: 8px;\n')
    file.write('            text-align: left;\n')
    file.write('        }\n')
    file.write('        th {\n')
    file.write('            background-color: #F2F2F2;\n')
    file.write('        }\n')
    file.write('    </style>\n')
    file.write('</head>\n<body>\n')
    file.write(html_table)
    file.write('\n</body>\n</html>')







