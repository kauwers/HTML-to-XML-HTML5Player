#replace.py

def findAndDeleteCaps(filePath):
    print("script ran", filePath)
    # toReplace specifies which items to replace and with what
    # e.g. Aname will be replaced with name, Btype is replaced with type
    toReplace = {"Aid":"id", "Btime":"time", "Csrc":"src", "Bname":"name", "Ctemplate":"template", "Btitle":"title", "Cthumbnail":"thumbnail", "Dcontent":"content"}

    # Read in file as a string and open it to be written to
    textToReplace = open(filePath).read()

    writeFile = open(filePath,"w")

    # run through the dictionary using the original key and the new text to use
    for original, new in toReplace.items():
        textToReplace = textToReplace.replace(original, new) # Replace the specified text
    #    print(textToReplace)



    writeFile.write(textToReplace)
    writeFile.close()


def module2replace(filePath):
    # toReplace specifies which items to replace and with what
    # e.g. Aname will be replaced with name, Btype is replaced with type
    toReplace = {"1_ea6hh6q1":"1_ml8uffn8","1_78u06p34":"1_zdvqo113","1_xzivkoxx":"1_l9kx0z80","1_flvlbz76":"1_kgjrjnjx","1_4zza413y":"1_k0byh2ey","1_pjrxy9ks":"1_dpwcq8c5","1_2zfvylqb":"1_vmo184ve","1_p75tmtcb":"1_e0fic9xv","1_kr6sis8j":"1_in3dq11q","1_edywxl4g":"1_hca1in5u","1_pcz86iuf":"1_znm3429h","1_0pen9sh9":"1_u82p5a06","1_2p40o3jw":"1_2ox4gf9c","1_axexc7sy":"1_rk3af2cp","1_y9kd108x":"1_28u6oqqb","1_m854dnw5":"1_iq1kdxj1","1_w8ygtwi8":"1_1q2wpb1k","1_eauepfxs":"1_jz171axq","1_f55gkixt":"1_qebdhwpq","1_3kom69f7":"1_9ch2bij6","1_qjjfanbh":"1_rmtsz48l","1_vdarvxv4":"1_6fj0t2as","1_rdvzbp3b":"1_3djri7dg","1_7saw60z5":"1_onbgbmp7","1_pvjoepza":"1_3am7rf4x","1_w9i9wd3a":"1_9i51m3q4","1_00b8c4nu":"1_680fef5t","1_nv9tnzm2":"1_814byxdr","1_baiszlqs":"1_b7t1atgv","1_eubr5qcv":"1_t414qpn4","1_5qg3eu11":"1_re4b83jg","1_qkzlropl":"1_5el08izg","1_au9ljklf":"1_sno9k2fe","1_abgtj3ah":"1_x8n7mswj","1_wofhry6x":"1_htof15of","1_rvivbmfu":"1_4gjq61v6","1_y1qkk67x":"1_2tw0vkot","1_ywkh7jj4":"1_aslcc5iz","1_qpc8ewtp":"1_ln0t94td","1_8epkca2r":"1_v0un14xz","1_h95dmj60":"1_h0ljvajm","1_plyufoca":"1_o2ecpla4","1_umppvhd2":"1_ptmqogkl","1_1g011s1c":"1_v9u1yxtp","1_bk6ea064":"1_y39jt79q","1_k04dnmag":"1_82tuomxb","1_8vsb5pe1":"1_4sdzu7zb","1_8unj7ad5":"1_yvgtrmid","1_wkhjjgdx":"1_0gd046wh","1_ipwmlf9v":"1_sscety0j","1_6qxx3pxw":"1_m6rhl849","1_8dau15ag":"1_4tlmrrsj","1_u47w0kzk":"1_njsq52ur","1_mio2f1uk":"1_2u3pd8fe","1_nfo1wkix":"1_57z7zn1z","1_321rmags":"1_a207by7o","1_8t82yf8b":"1_9vv79pjf","1_93ir7v4b":"1_gxwh4jjp","1_fpcgkr73":"1_1cjoiuqc","1_1v02u1uf":"1_xpeoagyt","1_tapf8uri":"1_r1gln2ar","1_wjke1nu5":"1_auprjeys","1_jdhqa1lo":"1_05m2m2sj","1_hymyfu8j":"1_ttpbqb7s","1_lau58mml":"1_pcmu60dl","1_kp5v3bzf":"1_u5aqe0i2","1_385aiekl":"0_c4cnz0zw","1_1fys1j8y":"0_xn1nuia9","1_6opfyzgz":"1_h7nhd1l7","1_ft7ymq6w":"1_ow1dc4nn","1_kd9yukpf":"1_35lbweeu","1_0lsvec4d":"1_av26shed","1_ssq3eap9":"1_z03u2xbd","1_x4vigr3v":"1_uw4xpqpi","1_bvmikyp3":"1_za2m4f9p","1_cfgsasxi":"1_ssje2okc","1_vtgc3mn2":"1_zs0n8jwk","1_9qbf3krr":"1_kf3ssm67","1_lkgodqke":"1_4gegcj3y","1_0j8neaa2":"1_60ey8ssv","1_fnsdc3mz":"1_7khi7lg3","1_bjdh6v3k":"1_hrz52qvh","1_01z7x65o":"1_6ys29nm1","1_cd17umev":"1_z335hswb","1_po9to03i":"1_u9wc4p7h","1_w8pto7gg":"1_vyffqo0r","1_3ey35k6l":"1_q5rly0yn","1_jo1fo6vc":"1_2ewttsnu","1_0dnkoeu0":"1_56nyjs1c","1_e92kvznr":"1_zymky3p2","1_u52hq8cg":"1_8d0utzs6","1_pomwiynt":"1_semdfiq1"}

    # Read in file as a string and open it to be written to
    textToReplace = open(filePath).read()

    writeFile = open(filePath,"w")

    # run through the dictionary using the original key and the new text to use
    for new, original in toReplace.items():
        textToReplace = textToReplace.replace(original, new) # Replace the specified text

    writeFile.write(textToReplace)
    writeFile.close()

def module1replace(filePath):
    toReplace = {"1_hvbaigg3":"1_g613xf3r","1_d43g100u":"1_ie59e5ke","1_5dm1puuh":"1_6dpubnbb","1_a2r5ca0m":"1_ky95x92s","1_rs6dsa9w":"1_l762phrl","1_zzdeweca":"1_vxce4pfu","1_3lfagkbs":"1_brxdxaz8","1_3hn7u7zb":"1_r1kuyy77","1_bq0c8p22":"1_hqhuc053","1_akgbodur":"1_disvggf0","1_zgzka0ay":"1_ayw2io8j","1_jgbgktyl":"1_u183x86j","1_yt0m3jhn":"1_3zdkdfs5","1_7why5a8y":"1_stuthodb","1_hzu4yxr1":"1_sn34q9q1","1_ipx21lc3":"1_1hjorkj6","1_6veq8sol":"1_kkw718p4","1_0y3b8qvb":"1_0q8begzi","1_en4whnpj":"1_08edijw9","1_p3j48blv":"1_xqlyey92","1_hzd31x57":"1_eswojgc9","1_plxzhbs3":"1_fb34w024","1_k6mqco86":"1_bic73828","1_5zjel2pl":"1_hx925had","1_u9y2ryu0":"1_bahgmz7d","1_51hztfv6":"1_zwdy2qds","1_t8rzy4d2":"1_9hvn5m6z","1_nn14ohkq":"1_qx6vx12g","1_m1ypxyeo":"1_1sg9yeme","1_9n90q5nc":"1_dklgtafa","1_29r5p3dk":"1_pfsc1yx4","1_pmk6z6g7":"1_rzztz80n","1_gih6inpq":"1_2zpvj8mr","1_qa6q0dff":"1_ln1iolq7","1_stb76vmd":"1_aj65c7k0","1_o7n6d6ye":"1_gn6y2hb1","1_dk6hsn0w":"1_cgipxu1l","1_69aiglf8":"1_ng9y59vw","1_fasmcd65":"1_tfq3zzup","1_ou7jou90":"1_i9hhysy1","1_t162ruf1":"1_bgtmqthi","1_o586jr2i":"1_tduumyf1","1_f5vlxqnv":"1_0qo8bpma","1_j6q24420":"1_5b5lxh9j","1_p5hg9qnr":"1_kyjapdhx","1_z1v9pxn8":"1_6w0j2cac","1_4ofxvsph":"1_asm424r0","1_j861xy03":"1_awodp0s5","1_n5bhlw0s":"1_7cmv1wrr","1_m7xzb3l7":"1_z6drph0v","1_wqpmrdvg":"1_dr4t2wro","1_z1dj1z6u":"1_kuqwzkf4","1_x2ra0fjf":"1_4g8fxirj","1_jsq1096m":"1_j55qd8au","1_7f6v8rig":"1_qudy7w9v","1_21m1lj8s":"1_5vrji6ed","1_27t6dt9q":"1_28saai48","1_9ngto6xt":"1_229042xs","1_xzzq05uc":"1_wqp2fegp","1_9icr10ue":"1_tjlp3s08","1_owy91ikf":"1_93bgdsd8","1_bg87efv8":"1_ihsnklpq","1_hq6gndjc":"1_32cmstz3","1_uz70pmvp":"1_p0ilrtjt","1_cpn5swhw":"1_zg6675y8","1_a7rwi4b8":"1_9o8qpc9b","1_2wylbrg8":"1_y50nf0on","1_7i3w654a":"1_8o57uvix","1_jw9bgr61":"1_x4qazly5","1_dc55kt3k":"1_bi32eih1","1_1dnk5gsb":"1_ubjgtb4i","1_di0kds8z":"1_7e49se6r","1_kiuwlrzb":"1_xl0pmh0u","1_84w54ok4":"1_kby39d3a","1_ozw0owby":"1_ifotel9q","1_2ldp8yns":"1_dlks421p","1_orb5gwmz":"1_4581d1aj","1_5zs7vgef":"1_okckrlqp","1_lgb43tq1":"1_fgao1nyx","1_vf6n47wj":"1_x5f21boc","1_96wolxnj":"1_8vf7eif6","1_lzz8w107":"1_2egp6eta","1_sroa5viy":"1_ew0fx8r6","1_981cakla":"1_udcdwsw7","1_v7c991i9":"1_u1q8i7lx","1_9j6tp4my":"1_q5tu7q67","1_it2ha2re":"1_89frvvl6","1_3j8n7k02":"1_pmz6g9lk","1_x2zggw4f":"1_9i8x4eho","1_jn8hxakd":"1_ijju3stk","1_vkc1wg1a":"1_k4bgzu5j","1_83usbm6t":"1_7h0k5bae","1_gmgh78oi":"1_d97h4lwb","1_ahbdjqip":"1_edp962vj","1_cdydmk2f":"1_tloldbd5","1_1k1xapvr":"1_0f96pfzy","1_mzd8ff1o":"1_1c4uafye","1_bnzs9ilr":"1_rjemvky7","1_p33hja9b":"1_ztltliwc","1_evs11umj":"1_ea5yy5pa","1_ttessaiv":"1_cuc8qsd5","1_o96kqp93":"1_xpvslq35","1_gcyn66xs":"1_ba1njf8t","1_q2g6aqxk":"1_ekt1hzxt","1_fpbi8r0z":"1_w8m90hyt","1_v2283edb":"1_j5dn6yx7","1_py6xwfu9":"1_l159g9k1","1_9y1n1lkz":"1_e4uzahn0","1_6xsvm9oa":"1_a8nwark1","1_ues7q3jb":"1_mnjh4ycn","1_vpn13214":"1_62xw4377","1_vnwj6opc":"1_jrde6br1","1_wzq6s2ul":"1_n6hjipqq","1_s11f95gb":"1_g1jv3t6p","1_rqpr922z":"1_6gy1ojyh","1_ghb2tl7f":"1_0clo8t9g","1_d3tbk5ic":"1_d5ujrl3h","1_3pge2tb7":"1_6ukn1nmz","1_os5kh7ul":"1_fzc9juvb","1_oarfcfbx":"1_onsg8pyz","1_j1n0rwp4":"1_2zylr5b7","1_d1yc1x90":"1_dnrgia4m","1_zsoicyfp":"1_2de17d9a","1_6qadrqy4":"1_kz595xk1","1_x1z911t3":"1_byfb6sf2","1_sl7jv8hb":"1_fwjtx3ck","1_zkybzxqk":"1_y2d4g588","1_zv92ckmx":"1_koe8k2sm","1_i4pz3z02":"1_dv1eko48","1_73znr4or":"1_qx54nks1","1_mxwlsij0":"1_b75lv3nd","1_a07fv8u0":"1_mrmn7rmz","1_gotfx37t":"1_i0vzynr2","1_r0rncs9d":"1_nvwmtc8b","1_bml7c4l0":"1_ofyd95n0","1_jvhj7nuy":"1_9agb5iz1","1_qp0eysts":"1_2a1v7soc","1_htc7b0o4":"1_mcewr115","1_gl4f9lhn":"1_4slme6so","1_5ngrmky3":"1_vpm6g05u","1_2hr33mnk":"1_n3auj41d","1_nw7cddt5":"1_iibisgv1","1_y9zzkkwa":"1_snxxfwi6","1_yrcj0tvg":"1_v5jfo7sm","1_rc75bkw4":"1_6frgoh0m","1_krshd305":"1_a3gjcsp7","1_u29q6u12":"1_zyx6pf8o","1_9id7f60j":"1_6g5msyu5","1_2t49ecty":"1_c6d1jmj6","1_ec2nk8l9":"1_sy1dapwp","1_n0czie02":"1_zh1z3loe","1_n7v55yub":"1_4fx3ilft","1_h3fwjrh1":"1_arqo3ler"}

    # Read in file as a string and open it to be written to
    textToReplace = open(filePath).read()

    writeFile = open(filePath,"w")

    # run through the dictionary using the original key and the new text to use
    for new, original in toReplace.items():
        textToReplace = textToReplace.replace(original, new) # Replace the specified text

    writeFile.write(textToReplace)
    writeFile.close()
