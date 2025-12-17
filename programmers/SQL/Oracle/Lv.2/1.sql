-- 최솟값 구하기

-- Oracle 환경
SELECT MIN(DATETIME) AS "시간" -- 큰따옴표 or 별칭 생략 권장
FROM ANIMAL_INS;

SELECT MIN(DATETIME)
FROM ANIMAL_INS;