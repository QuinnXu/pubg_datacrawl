import requests
import json
import csv
import os


def deaths(_url):
    url = "https://pubg.op.gg/api/matches/Svg7Thpx__N3LAxphvieh"+_url+"/deaths"
    headers = {"user-agent":"Mozilla/5.0 (Macintosh;"
                            " Intel Mac OS X 10_13_3) "
                            "AppleWebKit/537.36 (KHTML, "
                            "like Gecko) Chrome/64.0.3282."
                            "167 Safari/537.36 "
        ,}


    response = requests.get(url, headers=headers)
    html_str = response.content.decode() #json文件

    dict_ret = json.loads(html_str)
    dict_death = dict_ret["deaths"]


    with open('death.csv', 'w', newline='') as csvfile:
        fieldnames = ['map_id','time_event', 'description','victim_name','victim_x','victim_y','victim_rank','killer_name','killer_x','killer_y','killer_rank']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for event in dict_death:
            if event["killer"] == None:
                writer.writerow({'map_id': dict_ret["map_id"],
                                 'time_event':event["time_event"],
                                 'description':event["description"],
                                 'victim_name':event["victim"]["user"]["nickname"],
                                 'victim_x':event["victim"]["position"]["x"],
                                 'victim_y':event["victim"]["position"]["y"],
                                 'victim_rank':event["victim"]["rank"],
                                 'killer_name':"null",
                                 'killer_x':"null",
                                 'killer_y':"null",
                                 'killer_rank':"null"})
            else:
                if event["killer"]["rank"] == None:
                    writer.writerow({'map_id': dict_ret["map_id"],
                                 'time_event': event["time_event"],
                                 'description': event["description"],
                                 'victim_name': event["victim"]["user"]["nickname"],
                                 'victim_x': event["victim"]["position"]["x"],
                                 'victim_y': event["victim"]["position"]["y"],
                                 'victim_rank': event["victim"]["rank"],
                                 'killer_name': event["killer"]["user"]["nickname"],
                                 'killer_x': event["killer"]["position"]["x"],
                                 'killer_y': event["killer"]["position"]["y"],
                                 'killer_rank': "1"})
                else:
                    writer.writerow({'map_id': dict_ret["map_id"],
                                 'time_event': event["time_event"],
                                 'description': event["description"],
                                 'victim_name': event["victim"]["user"]["nickname"],
                                 'victim_x': event["victim"]["position"]["x"],
                                 'victim_y': event["victim"]["position"]["y"],
                                 'victim_rank': event["victim"]["rank"],
                                 'killer_name': event["killer"]["user"]["nickname"],
                                 'killer_x': event["killer"]["position"]["x"],
                                 'killer_y': event["killer"]["position"]["y"],
                                 'killer_rank': event["killer"]["rank"]})



def stats(_url):
    url = "https://pubg.op.gg/api/matches/Svg7Thpx__N3LAxphvieh"+_url
    headers = {"user-agent":"Mozilla/5.0 (Macintosh;"
                            " Intel Mac OS X 10_13_3) "
                            "AppleWebKit/537.36 (KHTML, "
                            "like Gecko) Chrome/64.0.3282."
                            "167 Safari/537.36 "
        ,}

    response = requests.get(url, headers=headers)
    html_str = response.content.decode() #json文件

    dict_ret = json.loads(html_str)
    dict_stat = dict_ret["teams"]


    with open('stats.csv', 'w', newline='') as csvfile:
        fieldnames = ['total_rank','nickname', 'rank','kills','damage_dealt','walk_distance','ride_distance','time_survived']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for team in dict_stat:
          #  if event["killer"] == None:
          #      writer.writerow({'map_id': dict_ret["map_id"],
          #                       'time_event':event["time_event"],
          #                       'description':event["description"],
          #                       'victim_name':event["victim"]["user"]["nickname"],
          #                       'victim_x':event["victim"]["position"]["x"],
          #                       'victim_y':event["victim"]["position"]["y"],
          #                       'victim_rank':event["victim"]["rank"],
          #                       'killer_name':"null",
          #                       'killer_x':"null",
          #                       'killer_y':"null",
          #                       'killer_rank':"null"})
          #  else:
                writer.writerow({'total_rank': dict_ret["total_rank"],
                                 'rank':team["stats"]["rank"],
                                 'nickname':team["participants"][0]["user"]["nickname"],
                                 'kills':team["participants"][0]["stats"]["combat"]["kda"]["kills"],
                                 'damage_dealt':team["participants"][0]["stats"]["combat"]["damage"]["damage_dealt"],
                                 'walk_distance':team["participants"][0]["stats"]["combat"]["distance_traveled"]["walk_distance"],
                                 'ride_distance':team["participants"][0]["stats"]["combat"]["distance_traveled"]["ride_distance"],
                                 'time_survived':team["participants"][0]["stats"]["combat"]["time_survived"]
                                 })


url_list = ["4hFKGQbRJFvN7uSq8lgnguAlWuJoPe_r6aq50SNjyctJ5sVDuh3QAsT0lgUpv1SkkcgF4sT6nVVAs67nKptBHM%3D",
"zc4e6w4NkIFMfTDMXuaEQbQ9vBtj4PmckJ07Pw9SILYwtF_U8zsEKC3yTX0ecLvohQO5avGml4ljaKtzTIAc2Y%3D",
"6vggU6NQvbExUfzBqNzLSie9NEXWBTA_RkVqNzZwAfWZKyMKLuTcwH4elDJ00VMvXgPK1r7VidCxdw28rgKQpY%3D",
"8t8Drk-iJ5c6M8O90v7bEQYTgLuTkI84HcNwQmlwK6NByCiuN1svcHbtYoQ305dmd5KGxJ0Fw_DUTzqLcSwuDo%3D",
"w7QIMryQ87LQiZE-IKWyvSYjiFdyshuUoaSV3XOoxqDlxkt1D80tPN1VAd-3w-0wI9z9TfMW_r0u_mtkRxmNkk%3D",
"9DP-X7c_eTRAfm5Ywzu6sPkDsGudv9oNQ4ngr4evknSmQDUq7wdqLc1-P2i97OhpkSYwHkrrhSlKmZTYgbjpyY%3D",
"7j16SCXWzx7Pvq9DrYocNWe-vbIUUroRZknMjGjTa-iZj2OjLezDBWuF5WclL77Lf85l8g5zIvF-11iRYEAq5o%3D",
"3uhA1SWl084eXtHlPx-PO3QEnzmWQ6laKHBVD8vei0_X6Wq3W_ax6iocRxsCSxoINqNgYmDwCJawq_PASByJN4%3D",
"7HZMEbIV1dZ8NH5nmdau3LQdC1GNPmHr-3oWXpObkdYlonxNsl8K1CtYYS0vvQ0WuUPl2DBUCBzZS1tfXrfJRo%3D",
"xHD-RheIIWtgn3j2j6Hn3i0icWEZg6w0G4fb0LUuALLcPY8-6wTTxqPUzOzy56_tg8dp6hLKAxUDVqmacpFWP4%3D",
"yx35vyR3KJ3KeuPLNB4qF2x1MVvcqpnljyCBjALON8UpCGiJsdMFLxwSssYXdXTcyRKWTgbyCdjdiD1KLQOrTc%3D",
"3pIG1XeQqP8IufPM_jCSDUo4_AteaZlSYz67_pPERQn1He-VpMmJl5SndN9iA4-ir19PhxEoPfmYyGJKem6BKs%3D",
"7pl8t0QhM1wzcQM641vegoIA3dCuGnWfl9N3zpHf2F4jqVkwnkyF56yokp_tXdxb_UyP6g1q45MTgbkZvFsQmU%3D",
"_9nKC584zBlxRhRtJg0j2MuhjoMIYHUmj_jDHy6jn74Ylby3NMEbf2t4b_aCNlang3vqCF2hJY-GViqOWmT3ZU%3D",
"xifkPvKa5-YUDZDNsJ546Zlf21BHngdjpHUmCjFV8bTwuGyXMHr4ZIFT0lP5OyINxKz64DPTBBBOOT-VY_lQC8%3D",
"-wxl4uMR-cMfv2R4QIwoSyQRHWJMdHgyTls26UpAYawWg3-EonpeyB3fuSFmpQgdmAaPT7yNj9WVR8OpagofkM%3D",
"_WSrr8Ss5ME9OWcOlsg_iSmyx2bgT54E__jViTiVE38e9rxDRrIRSLC0h58_lw0UjDtje4LNMySvzEmWP4x-qw%3D",
"13GAClCkQuat4MmCkpcwRUHOBHqfDBVmLSLAvS07t_MFZP31OpWmIqvvRUWvg-ITLXzNbMpyQCJavitypF74OA%3D",
"8W9izO4n1FD9fkqDW_9JX0bDCt4TahlHVgE0vZRvareiDRfNmlOF-cMynOBmL1pkXmEckrJ3BrG7UXOk4ckZyE%3D",
"3q6-uR-t5nziaZNDWwM11MbztGpt-QL6FULYXdAzJEB_VvMJ0JdiCDpj0p1LCbc-3C0Ie6jlGRF4X6oERLq3pQ%3D",
"2-VG4Sl3GUrrr-nSb0PBvpwdRuFYsNQFSaHsoqt_KEYxx_agGUtJClfiqp1BHeXgeflEptIW2V-NPobDh2on-U%3D",
"yMzqwMg8E_M49HSESH8nVWfyapAFUJle-XGbu8XZVy1oJ5P1t6GjeQ3tYdZkbRSCr3tric369A1atLJxkepH_I%3D",
"6e_-15SMNDpXqyYSy9ME8VILqLl40Krl3wypkJfXQbzPxO-hFf3rbCdyWuwSFgEDLB6AoHg-_WTkB0XpF9jNwU%3D",
"0x0i4EDftM8jOVsSGU45XG1gEbulKoCks2sMURAmNSLY5mp49s9Icrzh1f3o3x9mFI9aU6-oCluliKXvU39qzw%3D",
"6BpmfQPQZMKzy6qL7rvcmpFvjTuNAmvDzBK0L8hptFRCkxe3ERtCaSFwH8WcEoEfPpYXfZNwNOwxqXtmoTTawc%3D",
"wziklEyrsaAJrrX4mFTs1KlsPOHDGtwTvvlcLtIOUY8JbeOjC37NZOsfXwbTT8RIUgRXNnF6TYIb2Trq82P6i8%3D",
"5bWvgwAZTfvpfPbX0dYaAgPG45jIkZCzoCmRPfcyEO9NdTqU68ds9KLtuCejygmJqulskdtbyRQB77CTG671iQ%3D",
"yFyMwxqcE0S4GeMAbBBQrlV-N11yZQNksYhBicje2Np3uCdk0u9mScgAoBXT3KBqVu6Xp7qZR9uQo-1Ndqg35E%3D",
"6xnZY4LtEB89-1TLIAeBkLz3dv-eQdG1Eg7jOZMdPpbuJUffZyDPhG5mWTIDV6mXmtY-1qxpods_QP3caJNHoE%3D",
"w16Glhvfm_W9jW-VwoL9-7jqwmblZ5PfMmA7BYU8e1XYZVDvbAbTKuVLGJ5o5ShZw-1t97wICuxTxcOUggSCyE%3D",
"1OHheE9pUo4TXxzkSC1quuK1p5bGUzuFRFTVZlA4gAyus63e7MkPMCYpxJjIxGJCmSQJnShlA23ud6iJY-Yalc%3D",]

num = 1
for x in url_list:
    deaths(x)
    stats(x)
    os.renames('death.csv', "{}_deaths_XiaoJue.csv".format(num))
    os.renames('stats.csv', "{}_stats_XiaoJue.csv".format(num))
    num += 1


