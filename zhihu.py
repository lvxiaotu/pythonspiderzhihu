#coding:utf-8
import urllib2
import json
import re

def save_img(url):
    filename = url[-38:]
    
    headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            }
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    with open(filename.decode(),"wb") as f:
        f.write(response.read())
        print "finished "+filename


def get_img_urls():
    url = 'https://www.zhihu.com/api/v4/questions/29134042/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=40&sort_by=default'
    cookies = '_zap=b1513e85-fcd4-4c68-91e9-a06b25fea549; d_c0="AADCAeoEqwyPTlF6ZTPdisor08jC6nj2FdY=|1510415334"; Hm_lvt_0bd5902d44e80b78cb1cd01ca0e85f4a=1516678237,1516757937,1516776650,1516777528; __DAYU_PP=zm6UUeRQjb6eUeNq7eJvffffffff8756225235e6; _xsrf=b4d9f0bc-5dd8-4fd2-a0df-16a2f68d5a7c; q_c1=a303237371844da6a25931136be0ea2b|1527130570000|1509456224000; capsion_ticket="2|1:0|10:1527131409|14:capsion_ticket|44:NmZhZmYxNmJmMWZiNDU5MDhhMWRhMzZlNjEyYzlmNjk=|1b5f544f6bc42ac492c7f7f0019616cbb4ee49f75bf0d1e72a17d1f96deef8b2"; z_c0="2|1:0|10:1527131423|4:z_c0|92:Mi4xZ3lyNkF3QUFBQUFBQU1JQjZnU3JEQ1lBQUFCZ0FsVk5IM3Z6V3dEdTJLQlVveVQ3Zk9uTzBXSW10dERqa2tNNzNB|1466ebed0269b6ae32db644bde7d503c545c90dd5d55075d98f7365081d26748"; __utma=155987696.942400495.1527138103.1527138103.1527138103.1; __utmc=155987696; __utmz=155987696.1527138103.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=156dfd931a77f9586c0da07030f2df36'
    headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Cookie": cookies,
            }
    request = urllib2.Request(url,headers=headers)
    resopnse = urllib2.urlopen(request)
    jsonstr = resopnse.read()
    json_dict = json.loads(jsonstr)
    pattern = re.compile(r'https://.+?.jpg')
    for i in range(20):
        html = json_dict["data"][i]["content"]
        urls = pattern.findall(html)
        if urls != []:
            for url in urls:
                if url.startswith("https://"):
                     save_img(url)
def main():
    get_img_urls()
    
if __name__ == '__main__':
    main()
