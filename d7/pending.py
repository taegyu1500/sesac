def print_장바구니(owner_id, owner_name, *args):
    print(f"{owner_id} {owner_name}의 장바구니: ", end = "")
    for i in args:
        print(f"{i} ")
    print("")    
print_장바구니(1, "김철수")

def personal_info(name, age, *args, **kwargs):
    print(f"이름:{name}, 나이:{age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for i in args:
        print(f"추가: {i}")

personal_info("김철수", 120, "a", "b", **{'abc': 'def', 'tags': 'tagrr'})