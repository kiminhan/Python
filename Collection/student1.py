import json

dic = [
    {
        '학생ID':'ITT001',
        '이름':'김인한',
        '나이':'29',
        '주소':'대전',
        '수강정보':{
            '과거수강횟수':'1',
            '현재수강과목':[
                {
                    '강의코드':'IT171106',
                    '강의명':'IOT 빅데이터 실무반',
                    '강사':'이현구',
                    '개강일':'2017-11-06',
                    '종료일':'2018-09-05'
                }
            ]
        }
    },
    {
        '학생ID':'ITT002',
        '이름':'윤성우',
        '나이':'29',
        '주소':'대전',
        '수강정보':{
            '과거수강횟수':'1',
            '현재수강과목':[
                {
                    '강의코드':'IT171106',
                    '강의명':'IOT 빅데이터 실무반',
                    '강사':'이현구',
                    '개강일':'2017-11-06',
                    '종료일':'2018-09-05'
                },
                {
                    '강의코드':'OB171106',
                    '강의명':'오픈소스 빅데이터 실무반',
                    '강사':'이현구',
                    '개강일':'2017-11-06',
                    '종료일':'2018-09-05'
                }
            ]
        }
    }
]
dic.append({
        '학생ID':'ITT002',
        '이름':'윤성우',
        '나이':'29',
        '주소':'대전',
        '수강정보':{
            '과거수강횟수':'1',
            '현재수강과목':[
                {
                    '강의코드':'IT171106',
                    '강의명':'IOT 빅데이터 실무반',
                    '강사':'이현구',
                    '개강일':'2017-11-06',
                    '종료일':'2018-09-05'
                },
                {
                    '강의코드':'OB171106',
                    '강의명':'오픈소스 빅데이터 실무반',
                    '강사':'이현구',
                    '개강일':'2017-11-06',
                    '종료일':'2018-09-05'
                }
            ]
        }
    })
