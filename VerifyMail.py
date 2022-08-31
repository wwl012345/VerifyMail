import random
import smtplib
import logging
import sys
import dns.resolver

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger()


def fetch_mx(host):
    # 查看邮箱服务
    logger.info('正在查找邮箱服务器')
    answers = dns.resolver.resolve(host, 'MX')
    res = [str(rdata.exchange)[:-1] for rdata in answers]
    logger.info('查找结果为：%s' % res)
    return res

def verify_istrue():
    # 验证邮箱是否存在
    email_list = []
    exist = []
    email_obj = {}
    final_res = {}
    f = open('exist.txt', 'a+')

    # 从文件中读取用户名
    for line in open(sys.argv[1]):
        res = line.strip('\n')
        email_list.append(res)

    # 获取邮箱后缀
    for em in email_list:
        name, host = em.split('@')
        if email_obj.get(host):
            email_obj[host].append(em)
        else:
            email_obj[host] = [em]

    # 查看邮箱是否存在
    for key in email_obj.keys():
        host = random.choice(fetch_mx(key))
        logger.info('正在连接服务器...：%s' % host)
        s = smtplib.SMTP(host, timeout=10)
        for need_verify in email_obj[key]:
            helo = s.docmd('HELO chacuo.net')

            send_from = s.docmd('MAIL FROM:<3121113@chacuo.net>')
            send_from = s.docmd('RCPT TO:<%s>' % need_verify)
            if send_from[0] == 250 or send_from[0] == 451:
                final_res[need_verify] = True  # 存在
                # 将存在的邮箱放在exist列表中
                exist.append(need_verify)
            elif send_from[0] == 550:
                final_res[need_verify] = False  # 不存在
            else:
                final_res[need_verify] = None  # 未知
        s.close()
    for i in range(len(exist)):
        f.writelines(exist[i] + '\n')
    print(final_res)

if __name__ == '__main__':
    result = verify_istrue()
