from multiprocessing import Value
import multiprocessing
from bit import Key
from time import sleep, time
import random
#============================================================
p_addr_list = {
    66:'13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
    ,67:'1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9'
    ,68:'1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ'
    ,69:'19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG'
    ,70:'19YZECXj3SxEZMoUeJ1yiPsw8xANe7M7QR'
    ,71:'1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU'
    ,72:'1JTK7s9YVYywfm5XUH7RNhHJH1LshCaRFR'
    ,73:'12VVRNPi4SJqUTsp6FmqDqY5sGosDtysn4'
    ,74:'1FWGcVDK3JGzCC3WtkYetULPszMaK2Jksv'
    ,75:'1J36UjUByGroXcCvmj13U6uwaVv9caEeAt'
    ,76:'1DJh2eHFYQfACPmrvpyWc8MSTYKh7w9eRF'
    ,77:'1Bxk4CQdqL9p22JEtDfdXMsng1XacifUtE'
    ,78:'15qF6X51huDjqTmF9BJgxXdt1xcj46Jmhb'
    ,79:'1ARk8HWJMn8js8tQmGUJeQHjSE7KRkn2t8'
    ,80:'1BCf6rHUW6m3iH2ptsvnjgLruAiPQQepLe'
    ,81:'15qsCm78whspNQFydGJQk5rexzxTQopnHZ'
    ,82:'13zYrYhhJxp6Ui1VV7pqa5WDhNWM45ARAC'
    ,83:'14MdEb4eFcT3MVG5sPFG4jGLuHJSnt1Dk2'
    ,84:'1CMq3SvFcVEcpLMuuH8PUcNiqsK1oicG2D'
    ,85:'1Kh22PvXERd2xpTQk3ur6pPEqFeckCJfAr'
    ,86:'1K3x5L6G57Y494fDqBfrojD28UJv4s5JcK'
    ,87:'1PxH3K1Shdjb7gSEoTX7UPDZ6SH4qGPrvq'
    ,88:'16AbnZjZZipwHMkYKBSfswGWKDmXHjEpSf'
    ,89:'19QciEHbGVNY4hrhfKXmcBBCrJSBZ6TaVt'
    ,90:'1L12FHH2FHjvTviyanuiFVfmzCy46RRATU'
    ,91:'1EzVHtmbN4fs4MiNk3ppEnKKhsmXYJ4s74'
    ,92:'1AE8NzzgKE7Yhz7BWtAcAAxiFMbPo82NB5'
    ,93:'17Q7tuG2JwFFU9rXVj3uZqRtioH3mx2Jad'
    ,94:'1K6xGMUbs6ZTXBnhw1pippqwK6wjBWtNpL'
    ,95:'19eVSDuizydXxhohGh8Ki9WY9KsHdSwoQC'
    ,96:'15ANYzzCp5BFHcCnVFzXqyibpzgPLWaD8b'
    ,97:'18ywPwj39nGjqBrQJSzZVq2izR12MDpDr8'
    ,98:'1CaBVPrwUxbQYYswu32w7Mj4HR4maNoJSX'
    ,99:'1JWnE6p6UN7ZJBN7TtcbNDoRcjFtuDWoNL'
    ,100:'1KCgMv8fo2TPBpddVi9jqmMmcne9uSNJ5F'
    ,101:'1CKCVdbDJasYmhswB6HKZHEAnNaDpK7W4n'
    ,102:'1PXv28YxmYMaB8zxrKeZBW8dt2HK7RkRPX'
    ,103:'1AcAmB6jmtU6AiEcXkmiNE9TNVPsj9DULf'
    ,104:'1EQJvpsmhazYCcKX5Au6AZmZKRnzarMVZu'
    ,105:'1CMjscKB3QW7SDyQ4c3C3DEUHiHRhiZVib'
    ,106:'18KsfuHuzQaBTNLASyj15hy4LuqPUo1FNB'
    ,107:'15EJFC5ZTs9nhsdvSUeBXjLAuYq3SWaxTc'
    ,108:'1HB1iKUqeffnVsvQsbpC6dNi1XKbyNuqao'
    ,109:'1GvgAXVCbA8FBjXfWiAms4ytFeJcKsoyhL'
    ,110:'12JzYkkN76xkwvcPT6AWKZtGX6w2LAgsJg'
    ,111:'1824ZJQ7nKJ9QFTRBqn7z7dHV5EGpzUpH3'
    ,112:'18A7NA9FTsnJxWgkoFfPAFbQzuQxpRtCos'
    ,113:'1NeGn21dUDDeqFQ63xb2SpgUuXuBLA4WT4'
    ,114:'174SNxfqpdMGYy5YQcfLbSTK3MRNZEePoy'
    ,115:'1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv'
    ,116:'1MnJ6hdhvK37VLmqcdEwqC3iFxyWH2PHUV'
    ,117:'1KNRfGWw7Q9Rmwsc6NT5zsdvEb9M2Wkj5Z'
    ,118:'1PJZPzvGX19a7twf5HyD2VvNiPdHLzm9F6'
    ,119:'1GuBBhf61rnvRe4K8zu8vdQB3kHzwFqSy7'
    ,120:'17s2b9ksz5y7abUm92cHwG8jEPCzK3dLnT'
    ,121:'1GDSuiThEV64c166LUFC9uDcVdGjqkxKyh'
    ,122:'1Me3ASYt5JCTAK2XaC32RMeH34PdprrfDx'
    ,123:'1CdufMQL892A69KXgv6UNBD17ywWqYpKut'
    ,124:'1BkkGsX9ZM6iwL3zbqs7HWBV7SvosR6m8N'
    ,125:'1PXAyUB8ZoH3WD8n5zoAthYjN15yN5CVq5'
    ,126:'1AWCLZAjKbV1P7AHvaPNCKiB7ZWVDMxFiz'
    ,127:'1G6EFyBRU86sThN3SSt3GrHu1sA7w7nzi4'
    ,128:'1MZ2L1gFrCtkkn6DnTT2e4PFUTHw9gNwaj'
    ,129:'1Hz3uv3nNZzBVMXLGadCucgjiCs5W9vaGz'
    ,130:'1Fo65aKq8s8iquMt6weF1rku1moWVEd5Ua'
    ,131:'16zRPnT8znwq42q7XeMkZUhb1bKqgRogyy'
    ,132:'1KrU4dHE5WrW8rhWDsTRjR21r8t3dsrS3R'
    ,133:'17uDfp5r4n441xkgLFmhNoSW1KWp6xVLD'
    ,134:'13A3JrvXmvg5w9XGvyyR4JEJqiLz8ZySY3'
    ,135:'16RGFo6hjq9ym6Pj7N5H7L1NR1rVPJyw2v'
    ,136:'1UDHPdovvR985NrWSkdWQDEQ1xuRiTALq'
    ,137:'15nf31J46iLuK1ZkTnqHo7WgN5cARFK3RA'
    ,138:'1Ab4vzG6wEQBDNQM1B2bvUz4fqXXdFk2WT'
    ,139:'1Fz63c775VV9fNyj25d9Xfw3YHE6sKCxbt'
    ,140:'1QKBaU6WAeycb3DbKbLBkX7vJiaS8r42Xo'
    ,141:'1CD91Vm97mLQvXhrnoMChhJx4TP9MaQkJo'
    ,142:'15MnK2jXPqTMURX4xC3h4mAZxyCcaWWEDD'
    ,143:'13N66gCzWWHEZBxhVxG18P8wyjEWF9Yoi1'
    ,144:'1NevxKDYuDcCh1ZMMi6ftmWwGrZKC6j7Ux'
    ,145:'19GpszRNUej5yYqxXoLnbZWKew3KdVLkXg'
    ,146:'1M7ipcdYHey2Y5RZM34MBbpugghmjaV89P'
    ,147:'18aNhurEAJsw6BAgtANpexk5ob1aGTwSeL'
    ,148:'1FwZXt6EpRT7Fkndzv6K4b4DFoT4trbMrV'
    ,149:'1CXvTzR6qv8wJ7eprzUKeWxyGcHwDYP1i2'
    ,150:'1MUJSJYtGPVGkBCTqGspnxyHahpt5Te8jy'
    ,151:'13Q84TNNvgcL3HJiqQPvyBb9m4hxjS3jkV'
    ,152:'1LuUHyrQr8PKSvbcY1v1PiuGuqFjWpDumN'
    ,153:'18192XpzzdDi2K11QVHR7td2HcPS6Qs5vg'
    ,154:'1NgVmsCCJaKLzGyKLFJfVequnFW9ZvnMLN'
    ,155:'1AoeP37TmHdFh8uN72fu9AqgtLrUwcv2wJ'
    ,156:'1FTpAbQa4h8trvhQXjXnmNhqdiGBd1oraE'
    ,157:'14JHoRAdmJg3XR4RjMDh6Wed6ft6hzbQe9'
    ,158:'19z6waranEf8CcP8FqNgdwUe1QRxvUNKBG'
    ,159:'14u4nA5sugaswb6SZgn5av2vuChdMnD9E5'
    ,160:'1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv'
}

r_keyDec_list = {
    66:36893488147419103231
    ,67:73786976294838206463
    ,68:147573952589676412927
    ,69:295147905179352825855
    ,70:590295810358705651711
    ,71:1180591620717411303423
    ,72:2361183241434822606847
    ,73:4722366482869645213695
    ,74:9444732965739290427391
    ,75:18889465931478580854783
    ,76:37778931862957161709567
    ,77:75557863725914323419135
    ,78:151115727451828646838271
    ,79:302231454903657293676543
    ,80:604462909807314587353087
    ,81:1208925819614629174706175
    ,82:2417851639229258349412351
    ,83:4835703278458516698824703
    ,84:9671406556917033397649407
    ,85:19342813113834066795298815
    ,86:38685626227668133590597631
    ,87:77371252455336267181195263
    ,88:154742504910672534362390527
    ,89:309485009821345068724781055
    ,90:618970019642690137449562111
    ,91:1237940039285380274899124223
    ,92:2475880078570760549798248447
    ,93:4951760157141521099596496895
    ,94:9903520314283042199192993791
    ,95:19807040628566084398385987583
    ,96:39614081257132168796771975167
    ,97:79228162514264337593543950335
    ,98:158456325028528675187087900671
    ,99:316912650057057350374175801343
    ,100:633825300114114700748351602687
    ,101:1267650600228229401496703205375
    ,102:2535301200456458802993406410751
    ,103:5070602400912917605986812821503
    ,104:10141204801825835211973625643007
    ,105:20282409603651670423947251286015
    ,106:40564819207303340847894502572031
    ,107:81129638414606681695789005144063
    ,108:162259276829213363391578010288127
    ,109:324518553658426726783156020576255
    ,110:649037107316853453566312041152511
    ,111:1298074214633706907132624082305023
    ,112:2596148429267413814265248164610047
    ,113:5192296858534827628530496329220095
    ,114:10384593717069655257060992658440191
    ,115:20769187434139310514121985316880383
    ,116:41538374868278621028243970633760767
    ,117:83076749736557242056487941267521535
    ,118:166153499473114484112975882535043071
    ,119:332306998946228968225951765070086143
    ,120:664613997892457936451903530140172287
    ,121:1329227995784915872903807060280344575
    ,122:2658455991569831745807614120560689151
    ,123:5316911983139663491615228241121378303
    ,124:10633823966279326983230456482242756607
    ,125:21267647932558653966460912964485513215
    ,126:42535295865117307932921825928971026431
    ,127:85070591730234615865843651857942052863
    ,128:170141183460469231731687303715884105727
    ,129:340282366920938463463374607431768211455
    ,130:680564733841876926926749214863536422911
    ,131:1361129467683753853853498429727072845823
    ,132:2722258935367507707706996859454145691647
    ,133:5444517870735015415413993718908291383295
    ,134:10889035741470030830827987437816582766591
    ,135:21778071482940061661655974875633165533183
    ,136:43556142965880123323311949751266331066367
    ,137:87112285931760246646623899502532662132735
    ,138:174224571863520493293247799005065324265471
    ,139:348449143727040986586495598010130648530943
    ,140:696898287454081973172991196020261297061887
    ,141:1393796574908163946345982392040522594123775
    ,142:2787593149816327892691964784081045188247551
    ,143:5575186299632655785383929568162090376495103
    ,144:11150372599265311570767859136324180752990207
    ,145:22300745198530623141535718272648361505980415
    ,146:44601490397061246283071436545296723011960831
    ,147:89202980794122492566142873090593446023921663
    ,148:178405961588244985132285746181186892047843327
    ,149:356811923176489970264571492362373784095686655
    ,150:713623846352979940529142984724747568191373311
    ,151:1427247692705959881058285969449495136382746623
    ,152:2854495385411919762116571938898990272765493247
    ,153:5708990770823839524233143877797980545530986494
    ,154:11417981541647679048466287755595961091061972988
    ,155:22835963083295358096932575511191922182123945976
    ,156:45671926166590716193865151022383844364247891952
    ,157:91343852333181432387730302044767688728495783904
    ,158:182687704666362864775460604089535377456991567808
    ,159:365375409332725729550921208179070754913983135616
    ,160:730750818665451459101842416358141509827966271232
    ,161:1461501637330902918203684832716283019655932542464
}
#============================================================
class BTC():
    def __init__(self):
        self.mode = 0
        self.r_start = 0
        self.r_end = 0
        print()
# ============================================================
    def input_mode(self):
        
        p_start = 66
        p_end = 66

        print("__PUZZLE : ",p_start,'=>',p_end)
        self.r_start = r_keyDec_list[p_start]
        self.r_end = r_keyDec_list[p_end+1]
        print('__RANGE   : ', self.r_start ,'=>', self.r_end)

        for i in range(p_start,p_end+1):
            print('__',i,': __',p_addr_list[i])

        self.mode = 'random'
        print()
# ============================================================
    def speed(self,cur_n):
        while True :
            print('__',cur_n.value, end= '\r')
            sleep(1)
# ============================================================
    def run_random(self, cur_n):
        print('__Random__')
        r = 5000000000 # range 
        for i in range(r):
            priv_int = random.randint(self.r_start, self.r_end)
            key = Key().from_int(priv_int)
            address_p2pkh_c = key.address_p2pkh_c
            # address_p2pkh_c = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so' # test 

            if  address_p2pkh_c in p_addr_list.values():
                print('==== Congrats to you ! Find key success ====')
                print('==== SUCCESS = GOOD JOB BRO ! ====')
                print(key.to_hex() ,'\n')
                print(key.address_p2pkh_c  ,'\n')

                f = open("$_Foundkey.txt", "a") # the found privatekey and address saved to "$_Foundkey.txt"
                f.write(key.to_hex()+'\n')
                f.write(key.to_wif()+'\n')
                f.write(key.address_p2pkh_c+'\n')
                f.close()
                exit()
            cur_n.value += 1
# ============================================================
if __name__ =="__main__":
        print('======================= PUZZLE ========================')
        obj = BTC()
        obj.input_mode()

        cur_n = Value('i',0)
        t1 = multiprocessing.Process(target=obj.run_random, args=(cur_n,))
        t2 = multiprocessing.Process(target=obj.run_random, args=(cur_n,))
        t3 = multiprocessing.Process(target=obj.run_random, args=(cur_n,))
        t4 = multiprocessing.Process(target=obj.run_random, args=(cur_n,))
        tspeed = multiprocessing.Process(target=obj.speed, args=(cur_n,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        tspeed.start()
        
