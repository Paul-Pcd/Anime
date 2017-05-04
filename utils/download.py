# -*- coding: utf-8 -*-

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import pymongo
import urllib
import socket

client = pymongo.MongoClient('localhost', 27017)
Bilibili = client['Bilibili']
Bangumi = Bilibili['Bangumi']
Episode = Bilibili['Episode']

socket.setdefaulttimeout(10.0)


def get_cover_from(pic):
    try:
        pic_url = pic['cover']
        pic_name = 'E:/Projects/Bilibili/media/{}_.{}'.format(pic['_id'], 'jpg')
        urllib.urlretrieve(pic_url, pic_name)
    except Exception as e:
        print('{}\t{}'.format(pic['_id'], e))

if __name__ == '__main__':
    pool = ThreadPool()
    pool.map(get_cover_from, (i for i in Episode.find()))
    pool.close()
    pool.join()

'''
    5916    timed out
    1890    timed out
    2331    timed out
    2144    timed out
    5320    timed out
    2597    timed out
    3557    timed out
    2005    timed out
    1449    timed out
    827     timed out
    4027    timed out
    2181    timed out
    3853    timed out
    1577    timed out
    1324    timed out
    524     timed out
    4319    timed out
    5798    timed out
    109     timed out
    3530    timed out
    1309    timed out
    5788    timed out
    1569    timed out
    5777    timed out
    3072    timed out
    193     timed out
'''

'''
    98594	timed out
    81278	timed out
    60298	timed out
    10455	timed out
    97107	timed out
    92626	timed out
    64048	timed out
    81269	timed out
    50953	timed out
    81268	timed out
    70872	timed out
    35075	timed out
    72691	timed out
    30235	timed out
    66475	timed out
    76513	timed out
    13897	timed out
    13358	timed out
    32242	timed out
    13359	timed out
    14073	timed out
    63796	timed out
    88702	timed out
    98615	timed out
    95189	timed out
    104259	timed out
    1971	timed out
    100438	[Errno socket error] timed out
    100371	timed out
    104045	timed out
    101309	timed out
    77682	timed out
    79329	timed out
    101302	timed out
    100575	timed out
    65791	timed out
    30053	timed out
    77668	timed out
    82143	timed out
    103431	timed out
    88489	timed out
    28499	timed out
    75278	timed out
    91123	timed out
    8761	timed out
    62693	timed out
    89036	timed out
    85194	timed out
    85502	timed out
    89481	timed out
    13805	timed out
    97329	timed out
    89475	timed out
    84995	timed out
    81494	timed out
    13673	timed out
    91535	timed out
    672	[Errno socket error] timed out
    30347	[Errno socket error] timed out
    89332	timed out
    88510	[Errno socket error] timed out
    89352	timed out
    95810	timed out
    88626	timed out
    4982	timed out
    27911	timed out
    101517	timed out
    89342	timed out
    90280	timed out
    76674	timed out
    94736	timed out
    11671	timed out
    90552	timed out
    29973	timed out
    97040	timed out
    29987	timed out
    12353	timed out
    65535	timed out
    62855	timed out
    5059	timed out
    30337	timed out
    63468	timed out
    5060	timed out
    80881	timed out
    32176	timed out
    30790	timed out
    89571	timed out
    16101	timed out
    8908	timed out
    63578	timed out
    14886	timed out
    89566	timed out
    89429	timed out
    33853	timed out
    28175	timed out
    18940	timed out
    5048	timed out
    86936	timed out
    5160	timed out
    18931	timed out
    90222	timed out
    28158	timed out
    12039	timed out
    95841	timed out
    43885	timed out
    54242	timed out
    65426	timed out
    18841	timed out
    1838	timed out
    86890	timed out
    10233	timed out
    82454	timed out
    18709	timed out
    1826	timed out
    16637	[Errno socket error] timed out
    45101	timed out
    3814	timed out
    33163	[Errno socket error] timed out
    19673	timed out
    16708	timed out
    33392	timed out
    18423	timed out
    16717	timed out
    33740	timed out
    33150	timed out
    89640	timed out
    26732	timed out
    15368	timed out
    21736	[Errno socket error] timed out
    16292	timed out
    16299	timed out
    26387	timed out
    36302	[Errno socket error] timed out
    81376	timed out
    17980	timed out
    16314	timed out
    17360	timed out
    26359	timed out
    22608	[Errno socket error] timed out
    15583	timed out
    22686	timed out
    22685	timed out
    84462	[Errno socket error] timed out
    84456	timed out
    86421	timed out
    86420	timed out
    86419	timed out
    93997	timed out
    92115	timed out
    22668	timed out
    23185	timed out
    92109	timed out
    21885	timed out
    92091	timed out
    24126	timed out
    22268	timed out
    24112	[Errno socket error] timed out
    25018	[Errno socket error] timed out
    24180	[Errno socket error] timed out
    90341	timed out
    66956	timed out
    92796	[Errno socket error] timed out
    90336	timed out
    39909	timed out
    41023	timed out
    66813	timed out
    26009	[Errno socket error] timed out
    90319	timed out
    39908	timed out
    101864	timed out
    26981	[Errno socket error] timed out
    27090	timed out
    36865	timed out
    82485	[Errno 2] : ''
    26972	[Errno socket error] timed out
    41219	[Errno socket error] timed out
    45878	timed out
    39279	timed out
    27274	timed out
    39141	timed out
    49943	timed out
    43821	timed out
    39036	timed out
    27420	timed out
    91196	[Errno socket error] timed out
    50515	[Errno socket error] timed out
    87773	timed out
    93189	timed out
    27828	timed out
    45837	timed out
    12610	timed out
    91931	timed out
    93271	timed out
    65241	[Errno socket error] timed out
    14142	timed out
    35011	timed out
    43301	[Errno socket error] timed out
    86379	timed out
    39830	[Errno socket error] timed out
    91318	timed out
    41464	timed out
    41590	[Errno socket error] timed out
    65206	timed out
    35049	[Errno socket error] timed out
    39641	[Errno socket error] timed out
    87375	timed out
    86362	[Errno socket error] timed out
    40400	timed out
    92314	timed out
    39634	[Errno socket error] timed out
    39200	timed out
    19443	[Errno socket error] timed out
    41572	timed out
    67537	timed out
    91654	timed out
    67565	timed out
    91704	timed out
    91702	timed out
    43680	[Errno socket error] timed out
    46921	timed out
    43672	timed out
    38922	timed out
    91645	timed out
    43559	timed out
    48663	timed out
    43636	timed out
    44623	[Errno socket error] timed out
    40857	[Errno socket error] timed out
    43617	timed out
    92352	timed out
    40744	timed out
    50862	[Errno socket error] timed out
    96547	timed out
    41560	timed out
    82298	timed out
    4633	timed out
    53307	timed out
    50197	timed out
    23882	timed out
    97730	timed out
    15723	timed out
    50282	timed out
    40433	timed out
    94496	timed out
    79643	timed out
    58339	timed out
    48296	[Errno socket error] timed out
    58319	timed out
    48627	timed out
    58312	timed out
    70549	timed out
    54898	timed out
    51380	[Errno socket error] timed out
    94209	timed out
    58609	[Errno socket error] timed out
    51369	[Errno socket error] timed out
    98014	timed out
    58601	timed out
    48327	timed out
    54838	[Errno socket error] timed out
    48376	[Errno socket error] timed out
    56469	timed out
    94444	timed out
    58868	timed out
    56614	[Errno socket error] timed out
    54842	timed out
    59481	timed out
    42045	timed out
    79479	timed out
    29643	timed out
    59325	timed out
    79470	timed out
    76434	timed out
    29520	timed out
    88376	timed out
    94885	timed out
    97547	timed out
    50624	timed out
    19843	timed out
    52746	timed out
    88289	timed out
    94408	timed out
    76407	timed out
    50609	timed out
    94394	timed out
    59885	timed out
    97353	timed out
    58053	[Errno socket error] timed out
    88351	timed out
    58051	timed out
    53212	timed out
    88345	timed out
    52799	timed out
    50568	timed out
    77948	timed out
    50562	timed out
    57318	timed out
    76381	timed out
    97513	timed out
    57957	timed out
    50435	timed out
    57310	timed out
    97753	timed out
    58379	timed out
    58377	timed out
    57296	timed out
    58032	timed out
    58372	timed out
    20221	[Errno socket error] timed out
    58216	timed out
    58214	timed out
    58404	timed out
    57665	timed out
    58204	timed out
    57653	[Errno socket error] timed out
'''