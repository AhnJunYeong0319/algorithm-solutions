record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    id_hash = {}
    result = []

    for order in record:
        line = order.split(' ')
        if line[0] == 'Enter':
            id_hash[line[1]] = line[2]
            result.append(f"{line[1]} 님이 들어왔습니다.")

        elif line[0] == 'Leave':
            result.append(f"{line[1]} 님이 나갔습니다.")

        else: # change
            id_hash[line[1]] = line[2]

    return list(map( lambda x: x.replace(x.split(' ')[0]+' ',id_hash[x.split(' ')[0]]),result))

print(solution(record))


### Another solution in discussion ###


def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]