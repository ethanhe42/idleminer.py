# %% https://whattomine.com/coins?aq_4090=2&a_4090=true&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_4080=0&aq_47Ti=0&aq_47=0&aq_46Ti=0&aq_39Ti=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_37Ti=0&aq_3070=0&aq_3060Ti=0&aq_3060=0&aq_66=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_a5=0&aq_a45=0&aq_a4=0&aq_a2=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=254.0&factor%5Beth_p%5D=520.0&e4g=true&factor%5Be4g_hr%5D=254.0&factor%5Be4g_p%5D=520.0&zh=true&factor%5Bzh_hr%5D=360.0&factor%5Bzh_p%5D=520.0&cnh=true&factor%5Bcnh_hr%5D=0.0&factor%5Bcnh_p%5D=0.0&cng=true&factor%5Bcng_hr%5D=19600.0&factor%5Bcng_p%5D=640.0&s5r=true&factor%5Bs5r_hr%5D=6.3&factor%5Bs5r_p%5D=500.0&cx=true&factor%5Bcx_hr%5D=14.8&factor%5Bcx_p%5D=580.0&ds=true&factor%5Bds_hr%5D=18.6&factor%5Bds_p%5D=500.0&cc=true&factor%5Bcc_hr%5D=34.0&factor%5Bcc_p%5D=600.0&cr29=true&factor%5Bcr29_hr%5D=0.0&factor%5Bcr29_p%5D=0.0&hh=true&factor%5Bhh_hr%5D=4000.0&factor%5Bhh_p%5D=480.0&ct32=true&factor%5Bct32_hr%5D=2.7&factor%5Bct32_p%5D=500.0&eqb=true&factor%5Beqb_hr%5D=170.0&factor%5Beqb_p%5D=700.0&b3=true&factor%5Bb3_hr%5D=12.0&factor%5Bb3_p%5D=700.0&ns=true&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=520.0&factor%5Bal_p%5D=480.0&ops=true&factor%5Bops_hr%5D=240.0&factor%5Bops_p%5D=560.0&ir=true&factor%5Bir_hr%5D=107.0&factor%5Bir_p%5D=640.0&zlh=true&factor%5Bzlh_hr%5D=288.0&factor%5Bzlh_p%5D=700.0&kpw=true&factor%5Bkpw_hr%5D=134.0&factor%5Bkpw_p%5D=660.0&ppw=true&factor%5Bppw_hr%5D=120.0&factor%5Bppw_p%5D=800.0&nx=true&factor%5Bnx_hr%5D=550.0&factor%5Bnx_p%5D=760.0&fpw=true&factor%5Bfpw_hr%5D=128.0&factor%5Bfpw_p%5D=660.0&vh=true&factor%5Bvh_hr%5D=4.2&factor%5Bvh_p%5D=440.0&factor%5Bcost%5D=0.1&factor%5Bcost_currency%5D=USD&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&dataset=Main&commit=Calculate
import os
import signal
import subprocess
import gpustat
import time

configs = {
    'YOUR_WALLET_ADDRESS': '14ytoEgvzdtU7bXjGGodeprVCizchnH9iy',
}

cmd = '/home/yihuihe/Documents/mine/1.76a/lolMiner --algo NEXA --pool stratum+tcp://nexapow.auto.nicehash.com:9200 --user YOUR_WALLET_ADDRESS.RIG_ID'
cmd = './bzminer_v17.0.0_linux/bzminer -a nexa -w YOUR_WALLET_ADDRESS.RIG_ID -p stratum+tcp://nexapow.auto.nicehash.com:9200 --nc 1'

for k, v in configs.items():
    cmd = cmd.replace(k, v)

# Get a copy of the current environment variables
env = os.environ.copy()

# %%
while 1:
    gpus = gpustat.new_query()
    for g in gpus:
        if len(g.processes) == 0:
            print('starting miner')
            
            proc = subprocess.Popen(f"{cmd.replace('RIG_ID', str(g.index))} --devices {g.index}", shell=True) # , env=env
            time.sleep(10)
        elif len(g.processes) > 1:
            for p in g.processes:
                if 'miner' in p['command'].lower():
                    print('killing miner pid', p['pid'])
                    try:
                        os.kill(p['pid'], signal.SIGTERM)
                    except:
                        pass
    time.sleep(0.5)
