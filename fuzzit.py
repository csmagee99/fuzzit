import requests

target_url = input("Enter target url to fuzz: ")

with open("fuzzer_list.txt", "r") as fuzzer_list:
    try:
        for word in fuzzer_list:
            resp = requests.post(target_url + word)
            print(target_url + word)
            print(resp)
            if resp.ok:
                print('Fuzz yeah!!')
            else:
                print('Boo!')
    except:
        pass
