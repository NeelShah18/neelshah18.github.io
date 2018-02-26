import json

def main():
    result_json = []
    outfile = open('canada_1.json','w')
    with open('*.json', 'r') as f:
        for line in f:
            one_dic = json.loads(line)
            try:
                data = one_dic["place"]["country_code"]
                if data.lower() == 'ca':
                    result_json.append(one_dic)
            except:
                pass

    f.close()
    json.dump(result_json, outfile)
    outfile.close()
    print("Done!")
    return None

if __name__=="__main__":
    main()
