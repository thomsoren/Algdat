#!/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

def f(x, y):
    n = x + y -2
    k = x-1 
    n_fac = fac(n)
    k_fac = fac(k)
    result = n_fac//(k_fac*fac(n-k))
    return result


# Hardkodete tester på format (x, y, svar)
tests = [
    (1, 1, 1),
    (1, 2, 1),
    (3, 3, 6),
    (3, 5, 15),
    (9, 13, 125970),
    (13, 7, 18564),
    (15, 15, 40116600),
    (25, 39, 96977332473382725),
    (34, 27, 39602161018878633),
    (16, 23, 9364199760),
    (24, 43, 227068876035237600),
    (49, 47, 1591832366587979203662186030),
    (46, 44, 25665205262091854495873760),
    (31, 13, 11058116888),
    (10, 28, 94143280),
    (25, 43, 624439409096903400),
    (39, 25, 96977332473382725),
    (47, 43, 23991387527607603115708080),
    (35, 26, 30284005485024837),
    (31, 16, 344867425584),
    (12, 15, 4457400),
    (12, 12, 705432),
    (13, 21, 225792840),
    (19, 14, 206253075),
    (34, 15, 341643774795),
    (30, 29, 15033633249770520),
    (33, 47, 7821124592080019009790),
    (25, 13, 1251677700),
    (24, 49, 2650087220696342700),
    (38, 34, 100226479430802391940),
    (35, 18, 14771069086725),
    (12, 29, 1676056044),
    (22, 22, 538257874440),
    (46, 11, 29248649430),
    (48, 32, 5325020998862991666240),
    (50, 41, 33261615914984857055174310),
    (42, 36, 5454610487089714145160),
    (31, 37, 5516694892996182896),
    (20, 47, 12321566916640800),
    (19, 30, 4568648125690),
    (23, 22, 1052049481860),
    (21, 23, 513791607420),
    (48, 11, 43183019880),
    (14, 26, 5414950296),
    (30, 19, 4568648125690),
    (26, 44, 2646461346833015712),
    (16, 16, 155117520),
    (26, 34, 17451799771031262),
    (42, 23, 52728013040874885),
    (37, 13, 69668534468),
    (43, 35, 4545508739241428454300),
    (18, 15, 265182525),
    (28, 14, 12033222880),
    (19, 38, 144079707346575),
    (13, 35, 38910617655),
    (50, 38, 2893740668169934025792700),
    (17, 32, 1503232609098),
    (45, 38, 158444263771748044763400),
    (50, 26, 35059031427432595752),
    (26, 33, 9929472283517787),
    (27, 49, 66072789997853738148),
    (42, 23, 52728013040874885),
    (44, 39, 183461779104129314989200),
    (34, 23, 1300853625660225),
    (41, 20, 1397281501935165),
    (22, 39, 5189902721473470),
    (36, 37, 221256270138418389602),
    (48, 24, 1791608261879217600),
    (49, 42, 39751687313030682822037590),
    (31, 26, 3085851035479212),
    (22, 41, 12176310231149295),
    (26, 12, 600805296),
    (34, 29, 191724747789809255),
    (47, 28, 74604711829408425056),
    (38, 33, 47249626017378270486),
    (29, 23, 88749815264600),
    (29, 45, 75553695443676829680),
    (39, 25, 96977332473382725),
    (10, 12, 167960),
    (31, 41, 55347740058143507128),
    (45, 26, 4150132566624501912),
    (41, 37, 6212195276963285554210),
    (26, 20, 1408831480056),
    (50, 47, 3086205608690980088732809650),
    (38, 26, 147405545359541742),
    (50, 27, 101131821425286333900),
    (10, 17, 2042975),
    (46, 20, 8719878125622720),
    (18, 13, 51895935),
    (14, 39, 476260169700),
    (11, 25, 131128140),
    (31, 49, 3439076061765682117780),
    (36, 48, 177879702602584113899040),
    (36, 41, 2942618815403661578310),
    (16, 45, 39895566894540),
    (44, 21, 13488561475572645),
    (19, 46, 2588713818544245),
    (11, 31, 847660528),
    (42, 43, 839455243105945545123660),
    (34, 15, 341643774795),
    (14, 22, 927983760),
    (28, 26, 477551179875952),
    (29, 45, 75553695443676829680),
    (42, 37, 11666805764052999699370),
    (22, 46, 89067326568860640),
    (37, 47, 232231833953373704257080),
    (20, 45, 6131164307078475),
    (167, 228, 7082948864820803663628029102949107253729842794685500864385654321252211182445232679443872409880388264167897889553440),
    (161, 217, 97351320617125875045943603498211498745866990807172399684951867856783694402790573241161968530706898414665850450),
    (146, 143, 11519764939701603127186792452768768546043596005921447416013422741709554415172269883870),
    (90, 128, 201485183204675225062643536217728983039369012505310854715752320),
    (92, 182, 99890245309490236368784933413354036663124164729477068892668298791246818560),
    (157, 161, 5838095508286721532709528409803854511151305741589635304616614480944962706310570443881408600762),
    (130, 134, 354016051143468696783791498144533680750000783164208892238596879097681307496740),
    (76, 197, 143250280820906973932384771061083405926090165663608785443625478496620),
    (148, 247, 2813627725212492284717801351207741440005843923153774007934272792529127995152490929700113184796735644314049716800),
    (238, 114, 18588935499484192000747372928879901597695150253028825446653946891150878014216210501459722798000),
    (72, 232, 18252336489378675295971119455745556786408665545771672785345667026429600),
    (221, 52, 50964382545662522941989122021076271942393594399764034320),
    (132, 202, 231097173768302369876058390766944352497240055740395711196150316500455553802573193397349130913144),
    (164, 108, 270989600564215473118975985784621728414644954078098860624157051606486222271200),
    (184, 213, 1118508058520535263397418351782460968983188297865276794008945622799494524696485952331682541651596103980085490149199200),
    (92, 54, 9603168101309337510028755136667596179840),
    (84, 136, 44654935817877654281806121981324728689151319491732120283088248),
    (127, 136, 156634164975183729445295486647560036404299461621945823899533583522788104889472),
    (144, 116, 5044923741309991425956300613654555590602273421286914703853750276064801683200),
    (182, 245, 31236531484283078726073126855642913698920809820407111398441397892842706283837461503643608452513882859466512944843415610468000),
    (114, 208, 81817477405979320176910973180245066594691882814020211422369449220847793904032284913094400),
    (154, 114, 286356799879620472717499174596315555346599485052957834718513899135578993189600),
    (82, 115, 175777546240337791220407905870306072547121822575302764600),
    (224, 186, 4454766670172757061968429730996480464235005498473403457022813141737269461858388648915474531320193149619650541004395782400),
    (64, 224, 17575454605987412496945437866826907301319897880406344171927072000),
    (100, 74, 51166316916679980896946967744186187090095763343000),
    (95, 91, 1379363400956405299111471844050556271685325865981272800),
    (83, 112, 81755037386388245155846437548978316529605040412656629440),
    (155, 68, 4479058407907448199412857020923505953871050953909838486530),
    (139, 113, 23667947451598266764699846368322431581688740373653216490743399972916028625),
    (169, 197, 535959245989678789058732394043269532100244104143609301077723533809980982744295934037409282433879251650844810),
    (150, 167, 1897579500866667775571040008810135807959345276447797665546589470849181777096049320215353700100),
    (78, 77, 732932566345585498433243089884414262536751560),
    (62, 211, 33611977046258764171291482823454895470652401973261098086524720),
    (64, 174, 17172941137061647684922869302138418428664175859195442683200),
    (183, 152, 181007375394903101232625600692002345149154230801967031228349787506573931931581518522165280865991968),
    (171, 224, 22720483043431631870008721445764620449165265400119358137900429853136945341730378034654435517028269312784618564950400),
    (127, 232, 2024918258727738205205907583576270441171405961430510055207171627126455978435158124974381016370568064),
    (226, 127, 145206059498117577079260558136168064686744605300494778140099603154967143943378592272583045913674952),
    (171, 106, 1287149840438411534568664242454390622345654700324627441139041345566085515806800),
    (239, 89, 1843671044211324309367475279686223039524175540093217862399978825053427771388076000),
    (180, 206, 665953410781608816176154383496794672747464850023129086299789933383679095662118690839127694500755717140082572540160),
    (236, 69, 638026840426950440439557271769125326725766327833913740679724218156100),
    (248, 120, 787078913887533231867537715350585418028832565704346786341735994482357327032944048531037940224592000),
    (173, 146, 3794709749780075177400947846865512082816262455845007019607410073138619113597565957559724427630),
    (118, 104, 58092957207794570973266857329406940681324396162425115282150128800),
    (68, 76, 297890552164888191053744358705214108985160),
    (111, 203, 413318168973513042281749722256957938167248864101020116574447215757650234586888410593120),
    (97, 136, 6717309986917260933465021643501125363469212099406095609329543066435),
    (171, 60, 33515771556525020169820845297740784002726043549421682160),
    (193, 87, 24963417110248912928996565252598924011806874554398996009405558278977513100),
    (236, 123, 163639154000028522385680411298128346821111974429807967477064513262333746758870674436945682164446400),
    (134, 154, 2917882121434812460350240835141546273704878848951936462506973589463933911370102143580),
    (157, 159, 1492075042503658788347703463385674691216488025578062308111780916166765634403665984451909130032),
    (53, 99, 75140928735424634130082322915233871005500),
    (166, 199, 175805641940599379862106178075177995916403003739887792936904994548534459830290865114066003190420415962807140),
    (241, 131, 6440303722942338282622502840174092331973125752126565530070420638955596115672892693441697162695786587898),
    (179, 250, 36045845433818943334824673452682825481278221801066082205548005529762109093268525506776680229699752236307339404710539312054000),
    (93, 240, 443387276310883342749950597279696841756009880837259994958462842640776715984536744000),
    (235, 121, 12582117068280556796440514521852376743534902234185326227815453882647374240348357839679078161992800),
    (192, 82, 45815699233512758227744787599394063308813688020363993635133249958242560),
    (137, 108, 128459190907885658897744362835878574492642580378541466955113885214629574),
    (199, 55, 44703041038630878726808775968278838455280928552704555500),
    (86, 131, 25464591508030334378354311951377953870507147587421120353609883),
    (174, 199, 85898167160967255176894527885647831032648115568688329674070846389582825518178637040935938801381573445817837400),
    (84, 54, 216939458239435813017226269867659294400),
    (87, 221, 432258029126036542093526467407480114117540078019374620748278889480757885495200),
    (133, 100, 17173254009932400257666968574461639953868604235929762439436018858425),
    (249, 155, 6432969108807862971422029793811804074668783551030898699522263502046048040501260500062980903451794681855568983004000),
    (231, 90, 516310507835793830995767232747645879296031665610411607193233406136179503073884460),
    (198, 96, 4957576388269716583639209682488869713755724814238964396149194223245883450134400),
    (70, 84, 194223718380246317610201163674690968638342000),
    (95, 242, 10847202075391540054417267834511831117594380030863424744975343905591546336179799182000),
    (161, 154, 695538106055928311819757032993643662767979208053612118180156736113010822034313170945907826794),
    (72, 154, 328018932012030153632894747311093204671881639928783655474272),
    (172, 174, 1531602518609948683065344072456960288377392051090296687437458754169537196599026750263856759776476842560),
    (213, 207, 25291391158022591006197866602516071753661705094354927322379175819893967316329408240380875782960096605419941235047356157970080),
    (101, 136, 212172948364535765199820556668735693005125611163282517741510398771606),
    (205, 143, 23441872970155147495526371944784458177224570139794895097748333000351147067233688175521208046418649320),
    (140, 152, 72707809031142300599183094920427352212329179135513558980257067941727996533592208342080),
    (189, 81, 4754379791477354868602019675408078633418341667081178640965001831897360),
    (53, 87, 354011533558339838590148903133757134480),
    (164, 104, 6458070869622371196025121837082850499618919434844202801601805479981427825600),
    (125, 186, 112546931305265166549810552863330649396574272442105135526300106145297372248516132942650400),
    (248, 227, 561529607046847943092005544832697277726905433295774807166457634674667945715342347880440013008569548716026615161342721111516787144445350257760),
    (106, 208, 16768701969996156520543299473751330888591022296328371147534050921357563906229153202240),
    (212, 139, 22859880136423111792212159958114577536613027021368823168274288931785194144176128068876458132404848148),
    (50, 109, 145572290970018562646095770713217749931500),
    (73, 75, 5800834723650648582408201347161496628568500),
    (230, 239, 12896494248945124778967977467028962369570769773647039748081422183117653410766538166451430764139864920156156532002669969661366964704625341600),
    (50, 157, 598175843710730668556161002729317692014711555900),
    (206, 118, 2026739876826734498322315642922468539848610606162557542424058713917871414145340077291377280),
    (215, 127, 996559133369035076128097708882702330604469681483569988473267981562953668030388914398474869118080),
    (199, 132, 50979285742576604096542498322248108917610044625412322468312230022544016751152509862027444506920),
    (249, 75, 127321069450083886013285042125317854866007929007100601426473101183281548000),
    (180, 250, 86187831540081048867625476188537705620039547099755771977511432216414428446474463222907369487773709257762800364335814667928000),
    (95, 141, 15487046208485094584684100250004710393724801425075837831185914725080),
    (131, 242, 9914326478056462667439620554790822635527094000161642372017120568682681157322170909821035881162393461038),
    (241, 86, 64916794705564431428481809203624307398293287171647378952538721008439738019175600),
    (145, 244, 36315709773437500343029549654092759731684547745634220516749031164510118302935779763830790059512890796493802000),
    (15, 15, 40116600),
    (13, 7, 18564),
    (9, 13, 125970),
    (3, 5, 15),
    (3, 3, 6),
    (1, 2, 1),
    (1, 1, 1),
]


failed = False
for x, y, answer in tests:
    student = f(x, y)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
x: {x}
y: {y}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
