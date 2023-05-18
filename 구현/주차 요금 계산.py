import math
def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    visited = [0]*len(records)
    car_dict = dict()
    answer = []
    
    def cal_time(i, time, carnum,h,m):
        cnt = 0
        for j in range(i+1, len(records)):
            ti, car, inout = records[j].split()
            if inout == "OUT" and car == carnum:
                h_, m_ = ti.split(":")
                h_, m_ = int(h_), int(m_)
                hour = (h_-h)*60
                if m_-m < 0 :
                    minute = 60-abs(m_-m)
                    hour -= 60#minute가 음수면 1시간 빼주기
                    if hour < 0:
                        hour = 0
                else:
                    minute = m_-m
                total_time = hour + minute
                cnt += 1
                break
            else:
                continue
        if cnt == 1:
            return total_time
        
        else:#입차후 출차 내역이 없다면
            hour = (23-h)*60
            if 59-m < 0 :
                minute = 60-abs(59-m)
                hour -= 60#minute가 음수면 1시간 빼주기
                if hour < 0:
                    hour = 0
            else:
                minute = 59-m
            total_time = hour + minute
            return total_time
            
    for i in range(len(records)):
        time, carnum, inout = records[i].split()
        h, m = time.split(":")
        h, m = int(h), int(m)
        
        if carnum not in car_dict:
            car_dict[carnum] = 0 #{5961:0}

        if inout == "IN" and visited[i] == 0:
            visited[i] = 1
            car_dict[carnum] += cal_time(i, time,carnum,h,m)
    
    #요금 계산하기
    for key, values in car_dict.items():
        if values >= basic_time:
            price = basic_fee + math.ceil((values-basic_time)/unit_time)*unit_fee
        else:
            price = basic_fee
        answer.append([key,price])
    answer.sort(key = lambda x:x[0])
    
    #출력
    real_answer = []
    for i in answer:
        real_answer.append(i[1])
        
    return real_answer
