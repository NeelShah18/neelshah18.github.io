import json
import apiloc as ap

def main():
    temp_dic = {}
    result = []
    with open("locCode.json","r") as t:
        temp_json = json.load(t)
        temp_dic = temp_json[0]
        #print(temp_dic)
    with open("data.json","r") as country_data:
        code = json.load(country_data)
        count = 0
        for data in code:
            one_dic = {}
            country = data['country_code'].lower()
            freq = data['Count']
            try:
                one_dic = {

                        "location" : {
                            "lat" : temp_dic[country][0],
                            "lon" : temp_dic[country][1]
                        },
                        "country" : country,
                        "freq" : int(freq.replace(",",""))

                }
                result.append(one_dic)
            except:
                pass
    t.close()
    country_data.close()
    with open("ansUpdate.json","w") as f:
        json.dump(result, f, sort_keys=True, indent=4)
    print(result)
    return None

if __name__=="__main__":
    main()
