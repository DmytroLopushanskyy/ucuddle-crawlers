import matplotlib.pyplot as plt



x = [10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,10,20,30,40,50,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,20,40,60,80,100,
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,	
40,	
80,	
120,	
160,	
200,100,
125,
150,
175,
200,100,
125,
150,
175,
200,100,
125,
150,
175,
200,100,
125,
150,
175,
200,100,
125,
150,
175,
200,100,
125,
150,
175,
200,
100,125,150,175,200,100,100,125,125,125,150,125,150,150,150,175,175,175,175,200,200,200,200,100,125,125,125,125,125,150,150,150,150,150,175,175,175,175,175,200,200,200,200,200,100,125,125,125,125,125,150,150,150,150,150,175,175,175,175,175,200,200,200,200,200,100,125,125,125,125,100,150,150,150,150,125,175,175,175,175,150,200,200,200,175,200,200,100,125,125,125,125,125,150,150,150,150,150,175,175,175,175,175,200,200,200,200,200,100,125,125,125,125,125,150,150,150,150,150,175,175,175,175,175,200,200,200,200,200,100,125,125,125,125,150,150,175,175,125,150,150,200,200,150,175,175,175,200,200,200,100,125, 
125, 
125, 
125, 
125, 
150, 
150, 
150, 
150, 
150, 
175, 
175, 
175, 
175, 
175, 
200, 
200, 
200, 
200, 
200,50, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
80, 
80, 
80, 
80, 
80, 
80, 
80, 
80, 
60, 
60, 
60, 
60, 
90, 
70, 
100, 
60, 
60, 
60, 
60, 
60, 
70, 
90, 
90, 
90, 
90, 
90, 
90, 
90, 
70, 
70, 
70, 
80, 
110, 
70, 
70, 
70, 
70, 
80, 
80, 
100, 
80, 
100, 
100, 
100, 
100, 
100, 
100, 
80, 
80, 
80, 
80, 
80, 
90, 
90, 
90, 
90, 
110, 
110, 
110, 
110, 
90, 
110, 
110, 
110, 
90, 
90, 
100, 
90, 
90, 
100, 
100, 
100, 
100, 
100, 
100, 
110, 
100, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
50, 
60, 
60, 
60, 
60, 
70, 
70, 
60, 
60, 
60, 
60, 
60, 
70, 
70, 
80, 
80, 
70, 
70, 
70, 
70, 
70, 
80, 
80, 
90, 
90, 
80, 
80, 
80, 
80, 
80, 
90, 
90, 
90, 
90, 
100, 
90, 
100, 
90, 
90, 
100, 
100, 
100, 
110, 
100, 
110, 
110, 
110, 
110, 
100, 
100, 
110, 
110, 
110, 
100, 
50, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
70, 
60, 
60, 
70, 
70, 
80, 
70, 
70, 
70, 
70, 
70, 
70, 
80, 
80, 
80, 
80, 
80, 
90, 
80, 
80, 
80, 
90, 
90, 
90, 
90, 
90, 
100, 
90, 
90, 
90, 
100, 
100, 
100, 
100, 
100, 
110, 
100, 
100, 
100, 
110, 
110, 
110, 
110, 
110, 
110, 
110, 
110, 
50, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
60, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
70, 
80, 
80, 
80, 
80, 
80, 
80, 
80, 
80, 
80, 
90, 
90, 
90, 
90, 
90, 
90, 
90, 
90, 
90, 
100, 
100, 
100, 
100, 
100, 
100, 
100, 
100, 
100, 
110, 
110, 
110, 
110, 
110, 
110, 
110, 
110, 
110]


z_for_50 = [20783778511,12647673322,14924841890,11497462108,12892366484,
34791635769, 18634206434, 13140956642, 10392851969, 10046637555,
26870975219, 19714708386, 17990528092, 21712739129, 18138921713, 
18815226515, 10530036483, 10186495699, 10046471765, 10044256857, 
35144156611, 34625805423, 29441474526, 31587895870, 31101705522, 
23773087333, 21976141152, 22455639946, 22959968519, 24609182816,
24376002351, 19739919730, 17320127388, 17033954305, 18812741058,
63267217128, 47241506344, 48657493876, 54498555990, 47346029696,
16701953697, 10834480357, 10073070038, 10160117237, 10160117237]

z_for_100 = [26037099224,
25622268053,26177183616,25618695290,25673255615,31700167189,19507373132,19121366886,18687385526,19070716059,
25864922421,16679046094,17071628127,18601362114,19349730972,22614837318,12313394259,16109644393,10056871301,
10054941665,18036171047,13808915049,13451127317,14278947184,13356775804,28603442962,22464463474,20476742401,
20170538855,19415308898,33792010863,20363914843,18953015910,19127427210,41396709562,55110721821,59320548574,
20140876170,40560225608,39042334680,36647332722,34021528875,54042111825,42288526837,44993801801,28900976293,
26101532862,25669318454,25656230345,26631544402]




	

z_for_200 = [35304915075,34018331531,26945543730,28266105563,29203765354,35066102389,34672126413,34934415356,35188855958,34759027849,
61344567215,49622575805,32525073356,41650912767,30800601898,49422662874,98772580610,19567895097,65131793178,67064042578,41388896306,
39746256233,46710411712,65733232179,40455326393,55488784782,
58760735502,51167768236,45912596852,46933314282,41534634949,26570547460,22517374988,25511294817,23401239388,70151445210,66292761718,66328933185,
66237535060,
66297054087,14469092239,
17022171915,
23594515539,
18316972876,
17322515362,13881834444,
11879911105,
12579210569,
15175860775,
35416712933,29719151610,
25446772256,
23747002281,
22525527997,
25897513004,17040823157,
23901492726,
15999166279,
19086374527,
65962117757,103845661554,
110143943600,
78505572819,
103011744540,
105257532380,20515983315,
20750837013,
20702179021,
19567205786,
19493994243,20446898403,
11413230917,
10944202544,
11866271300,
10437835747,
25240863055,
25781434686,
19575719552,
17088071388,
22100301962,
16573798286,
31100272564,
20471999241,
33624772806,
21635439617,
26659412791,
21247206347,
18997795679,
21908568241,
22250200400,
32767806305,
24017425815,
25184981834,43286914027,
35068467990,
39897214398,
40632526369,
39951276018,
40861803477,
38530771960,
38282346575,
38761825226,
40260399357,
39291601570,
37968052695,
36678998556,
36306969113,
39070628516,
41851779437,
36205274311,
40233130576,
40955200341,
39462814960,
38005456151,24191555961,
21020434526,
21308333902,
22264211006,
22948303999,
25977772148,
20847567391,
20283389517,
20665212978,
21160623587,
20407718510,
21210280271,
23091573364,
21454235251,
21568757889,
32204808576,
21207708826,
20469121354,
22272174220,
22106456394,
18146856894,50329577848,
36620097684,
35989844227,
36044166236,
37816645697,
106780501189,
36715074807,
38087191680,
36341538475,
36956015867,
39211385520,
41191111552,
42117103240,
42955785298,
43036130122,
43044299522,
42531683828,
43407984761,
40645291151,
40205650844,
102095202306,
41509448500,
30458692862,
30321161083,
36427341825,
38339631088,
37877074086,
38831022912,
30791875123,
30658405754,
29683169952,
32740842258,
28857179991,
31654489647,
33938837249,
34498039491,
36710884033,
37781853658,
33259196082,
26380097992,
25178478570,
29702314052,
26163125774,
43597662942,
41155852095,
38365688491,
38771902224,
39613553999,
40287394731,
35467754181,
35154638714,
37185238661,
37118501160,
36206396296,
38805135364,
38829876990,
42402824224,
44543316363,
43491452149,
37433164504,
37217242933,
36910879887,
36292047810,
36691550336,
93582444627,
17620173653,
17388697779,
23435993829,
18533735326,
18324770370,
18163315100,
17641613235,
25954710906,
98467268171,
91120908356,
91861879106,
72128817709,
79607988486,
63689807963,
59443957673,
59184299758,
67598089345,
68231718341,
66491416160,
62893055117,
40684240595,
29392021547,
31290248443,
31874146220,
31284088165,
34462034769,
30044864776,
31966531237,
28883450155,
27410388025,
41129328584,
28171495493,
31524632782,
29700954387,
30209204164,
32669962221,
28779275397,
34259328402,
26130043123,
41310416304,
43073078801,67123184799,
60675071581,
60796306308,
60820495438,
60794614330,
64954827090,
61134631235,
63786897793,
62246707810,
65086724497,
67004570587,
64964226056,
66130585836,
69128222042,
69969960099,
67070838329,
68068768187,
68024527819,
71730487571,
43148774536,
43584714508,
44303282570,
44357862778,
45470978807,
45426962378,
47464068208,
47860075302,
49520038254,
45421304138,
74034072200,
73019630019,
75310851505,
69966885418,
72001767369,
74902288075,
74806736067,
35312109101,
34931141117,
36896634807,
35683328997,
38823570550,
27949748019,
26131843071,
85704979568,
88286805999,
90694452009,
92659684930,
92347795768,
21002411729,
92917918720,
93565997899,
94648434539,
93699132952,
95806438158,
94851902178,
100124910920,
100680098105,
100070405896,
98654401144,
93129621763,
90843372885,
84698188880,
84840989565,
85867918784,
89295472401,
19265027094,
94145004050,
82098065918,
27885648204,
97938135468,
98192952580,
100374183763,
100033114468,
97280299429,
98806117100,
94674454889,
96837517189,
99979924943,
67685276190,
72616996633,
99775010398,
29444052537,
71638888573,
94137693326,
76000983583,
74813403287,
77797002722,
92083894742,
94166111238,
89817717068,
89903552113,
86191372161,
86115615842,
88312759034,
31551569191,
87774056772,
84728403717,
85654516479,
83551791406,
83067977553,
75933789230,
71892698731,
72746603151,
73299089021,
73653418039,
68355937051,
68673191555,
71187590738,
71248295685,
72897398060,
72940004677,
73526921962,
73806789402,
77241817827,
74240402092,
76568789147,
93535176550,
95494550441,
23029318096,
28077480961,
99518988883,
100517028090,
101286825566,
100583558905,
103889518773,
51894749098,
63449254788,
64307790517,
64895264257,
69307334917,
69188466632,
71278785471,
73399197384,
71414797405,
74298563649,
73770236389,
76461896068,
77759971092,
68147958925,
72979100127,
68401447496,
82064512205,
82711793067,
66379370538,
74021330072,
65734083026,
65481256051,
79392296248,
86024645117,
90072593415,
94192867292,
95395484128,
54724048254,
67163884681,
68407316042,
24313177633,
100697141322,
73730776196,
14862315926,
25963001380,
24152726352,
84547566190,
70598655357,
90742821673,
25249067482,
24327875646,
108483300878,
65607680309,
54786299577,
63809975613,
60208525239,
66603547020,
56978141360,
62994214979,
63245430767,
15760419192,
69332936630,
63635099227,
63969921718,
66876180301,
63061675597,
63887473550,
63838522009,
64146204615,
66478339525,
62786082696,
63067899607,
64000097607,
59887207015,
61233398030,
62943293270,
63118449736,
64112333627,
69796746003,
64098817207,
62927883723,
63074511173,
62201573999,
59912845681,
63382195596,
63022446324,
65422401915,
60032528342,
63760814312,
65300024117,
62946499766,
66932882557,
64389512296,
68067634469,
66024191142,
62796006869,
64836381903,
63691783094,
66123303778,
62213355264,
55904055174,
48740278771,
52976480186,
50722407001,
47929654607,
41292809909,
43232488174,
59934596562,
69102185785,
71061330885,
77879557151,
80515196336,
82664632227,
81269135586,
83698519061,
82987726090,
83903905085,
61046206804,
59941874044,
54154877730,
52135154814,
53501665565,
53605563242,
52162622743,
54770499494,
54667753543,
59963536704,
61975970595,
61884082069,
53213822218,
71913699487,
74633850913,
74463515760,
74757082633,
75516880818,
52121414437,
77166591481,
77052854724,
81059706703,
78022100114,
80804637022,
79769172999,
78194805738,
82001399637,
84973905126,
85877875556,
86974410337,
81871146939,
82925528714,
81116169669,
84249079968,
84061490352,
79918162135,
85764839253,
84024611248,
86121799766,
82796062581,
78017204595,
74254524862,
71909378014,
73306873212,
69913464105]


print(len)






y = [(10**9)*50/i for i in z_for_50] + [(10**9)*100/i for i in z_for_100] + [(10**9)*200/i for i in z_for_200]


import plotly.express as px
fig = px.scatter(x=x, y=y)
fig.show()

# plt.scatter(x, y)
# plt.show()

diict = dict()
for i in range(len(x)):
    # print(x[i])
    if str(x[i]) not in diict.keys():
        diict[str(x[i])] = [y[i]] 
    else:
        diict[str(x[i])].append(y[i])

d2 = dict()
for key, value in diict.items():
    # print (key)
    # print(value)
    s = sum([int(item) for item in value])
    l = len(value)
    d2[key] = s/l

# for item iin

x1 = d2.keys()
y1 = d2.values()

plt.scatter(x1, y1)
plt.show()

print(len(x1))
print(len(y1))

# fig = px.scatter(x=x1, y=y1)
# fig.show()