import math

sect = [[0,0.025450843829724068, 0.04183526032200968, 0.05529194927240022, 0.06712409476794967, 0.07878391764107351, 0.09061292881618233, 0.0986169017114994, 0.10991947509140532, 0.11795593923019454, 0.12557308548646096, 0.13326944291428755, 0.13869011664951403, 0.14430700191438528, 0.15033903333314924, 0.15730239175883198, 0.16324173331553882, 0.1681959390292893, 0.1748443912189871, 0.18031567144921845, 0.18475101141796735, 0.19067225812474897, 0.19495231305863825, 0.19982459399766928, 0.2042576043098383, 0.2079003944193787, 0.21267281020697004, 0.21570602658246485, 0.22000447453533223, 0.22442500035562074, 0.22753750832619413, 0.23097765492989897, 0.23456042835005608, 0.23810498210319875, 0.24153176908035656, 0.24508509792999122, 0.24758751239479204, 0.25128066805447324, 0.254633982740213, 0.2577251769278446, 0.2606448087594124, 0.2636220729370692, 0.2671708271386092, 0.2693465548190095, 0.2722225489011312, 0.27550922804917755, 0.2774992372358096, 0.28032946706014505, 0.28277711026967167, 0.28590805741547054, 0.2886635532895312, 0.2908864978821162, 0.29356575804230367, 0.29690422233628166, 0.29958652178161294, 0.3019106548979048, 0.30358839008049743, 0.3064674358011348, 0.30904644526041936, 0.3118306458758784, 0.31405612722715803, 0.3170885499998751, 0.3195255572557859, 0.3212786073562848, 0.3237300356759103, 0.32582890225715166, 0.32760602462241717, 0.3293078141437832, 0.3316347461272988, 0.3337270824241162, 0.33543718156419433, 0.3378747112300766, 0.33986391523022375, 0.3417264668567679, 0.34310729725924016, 0.3452901740940899, 0.34730400246323545, 0.34916208183415853, 0.35137414970462666, 0.35276955814082733, 0.3553253821444794, 0.35734538349811396, 0.359010408305905, 0.36069218309910644, 0.36298268571020464, 0.36516783310199685, 0.36682109739006075, 0.3685200348897777, 0.3708514091165338, 0.3722641066580974, 0.3734203503124718, 0.37429695289234943, 0.3760005327581426, 0.37747663431318323, 0.379062448400453, 0.38027359430244745, 0.3814805264867447, 0.38279040284409116, 0.3849475966051362, 0.38606973687946256, 0.38763736783537683]
,[0,0.009367157999091824, 0.019807181162168286, 0.02817288716111699, 0.03573182909292405, 0.04336877534355177, 0.04965512742742206, 0.05492915910509788, 0.06178186264700103, 0.0666436142306992, 0.07085124676408117, 0.07472151869332988, 0.07889924986477881, 0.0834170361668799, 0.08688053765702886, 0.09017910045027244, 0.0930576509412705, 0.09685335161330322, 0.10121013332160878, 0.10531667328428307, 0.10854297777100586, 0.1123835403829, 0.11559195449063409, 0.119042736215633, 0.12191020354291837, 0.12506291009924242, 0.1277090997561906, 0.13056294512495725, 0.13242213538868552, 0.13646955768669755, 0.13992375676959545, 0.1430735018022531, 0.14532992548788626, 0.14839034620014757, 0.15119886911118408, 0.15331585738092035, 0.15634858217782366, 0.158108271956366, 0.15988904789995728, 0.16206278298720145, 0.16424394753436278, 0.16627326571736967, 0.1682390729571387, 0.17033615734695517, 0.17249360501000943, 0.17474850776062745, 0.17668023877602013, 0.17828590053697557, 0.18134674760942215, 0.18307788113721868, 0.18514029357604134, 0.18710237327530777, 0.1887763594034655, 0.19047162935347473, 0.1921104097638906, 0.19359966249848637, 0.1952035428334591, 0.19652669603152706, 0.19810074986338178, 0.19951042074991387, 0.20177001438379416, 0.20344771052618693, 0.20507320447675292, 0.2067422791442486, 0.20845277855538336, 0.2102354828300742, 0.21109662197015122, 0.21295255439741578, 0.21450798579117236, 0.2158691157123892, 0.2177743826841687, 0.2186816956563027, 0.2200582039554495, 0.22215633903603582, 0.22366336750188598, 0.22484770261344478, 0.22621422351411347, 0.22729117530266352, 0.2301696368171342, 0.2318820534210566, 0.2334656103025856, 0.23555216127727951, 0.2372051369967333, 0.2386901822769354, 0.24021210262941461, 0.2416901592007461, 0.24360266099466754, 0.2451654751408905, 0.24704076447478573, 0.248492688169901, 0.24923495839130616, 0.25090170065356254, 0.2524131291511098, 0.25413600608550335, 0.2552776227691106, 0.2565548460876774, 0.2581456143431442, 0.2593038891428795, 0.2605725029210795, 0.2622725953933076, 0.2637961582826486]
,[0,0.04048737720580653, 0.0628275984602793, 0.08157823757944305, 0.10013420202070122, 0.11446690626484146, 0.12971009279701118, 0.1418431125557874, 0.1506990038652336, 0.1589875942029415, 0.16802815812308192, 0.17632406794351518, 0.18421820620113938, 0.19103329102711564, 0.19847913472307166, 0.20596847590802003, 0.2135293760166711, 0.22044533720884119, 0.22633227802598943, 0.23259318562940445, 0.23853636553598234, 0.24509736269717086, 0.2520791399782403, 0.25717023390715343, 0.2626279775825906, 0.26716435370216585, 0.2716962881060754, 0.27652825411115045, 0.28241345400449525, 0.2863440246225297, 0.29054142821268436, 0.29475338504745996, 0.29962649628863014, 0.30464490639715014, 0.30903887469335456, 0.3138590840436445, 0.31812033434635223, 0.3230858568424757, 0.3267698892101115, 0.33049063408676815, 0.3343028017948305, 0.3380954022864284, 0.34211641515997193, 0.3456861625997243, 0.34861791254790675, 0.3525399402484709, 0.3565248229835527, 0.3600122500361229, 0.3631637916523047, 0.3667659655538611, 0.3706374808761771, 0.37376439088163393, 0.376614906986076, 0.3795684475116988, 0.3829263075359436, 0.38649839821277376, 0.3908143089522925, 0.39362307242740546, 0.396519809539401, 0.4000585659401932, 0.4028478280222214, 0.40566307357494247, 0.4087969769444728, 0.4111238503417586, 0.41389419613720824, 0.41647604382105496, 0.4198934363013308, 0.42266754155283526, 0.4249152794178638, 0.4280356137788145, 0.430940404085401, 0.4342678001752486, 0.4370883276148475, 0.4393119508021749, 0.4412445105706292, 0.4440852977137777, 0.4466926229757868, 0.44905063610168894, 0.45123694242282, 0.45347201689334415, 0.45569733515307975, 0.4575871063113669, 0.4600070821113553, 0.4622780294086275, 0.4645687048784587, 0.4667884233077453, 0.46908389972679854, 0.47080525377292537, 0.4728147267824152, 0.475271550822956, 0.47701803322963887, 0.47923126502144064, 0.48113029367209303, 0.48309950776829413, 0.4848962006845752, 0.48698322912929937, 0.4890631180056978, 0.49110772872220587, 0.49290244716489096, 0.49523957740207525, 0.49692285521199364]]

wordValues = []

# for i in sect:
# 	wordValue = []
# 	wordValue.append(math.log(i[0]))
# 	for j in range(1,len(i)):
# 		wordValue.append(math.log(i[j]-i[j-1]))
# 	wordValues.append(wordValue)


# print wordValues


#Transform
for i in range(len(sect)):
	for j in range(len(sect[i])):
		score = sect[i][j]
		score = 1 - score
		#Base 
		score = math.log10(score)
		sect[i][j] = score

#print window2

wordProb = []
for i in sect:
	row = []
	row.append(i[0])
	for j in range(1,len(i)):
		row.append(i[j]-i[j-1])
	wordProb.append(row)

print wordProb


#full = wordProb[0] + wordProb[1] + wordProb[2] + wordProb[3] + wordProb[4]
#full.sort()
#print full[0:100]
#print sum(full[0:100])

#print wordProb[4]
count = [0,0,0]
total = 0
for i in range(100):
	minScores = [wordProb[0][1],wordProb[1][1],wordProb[2][1]]
	index = minScores.index(min(minScores))
	#print minScores[index]
	#print index
	total += minScores[index]
	del wordProb[index][0]
	count[index] = count[index]+1

print total 
print count 
print 1-(10**total)