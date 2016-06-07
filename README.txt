To run the program, just go to the directory of IRLab

then enter command: 

python3 query.py

and you will on the way to go

mention that you need use PYTHON3

For EXTRA, I try to do evaluation by your submitted files in moodle,
you can see it in evalution.py file



YOU can see how I generate tf-idf in Utils class def generate_tf_rtfs method!

HERE is my process to do my program:
  1. extract the document contents, save documents individually into directory step1
1.5. split words in all the documents, save result into directory step1.5
  2. filter stop words and sort all the words in documents, save result into directory step2
  3. stem words and save result into directory step3
  4. generate words frequency in it's own document, save result into directory step4_words
  5. calculate words count appear in all documents, save result into file words_count_appear_in_document.txt
  6. calculate words largest frequency in all documents, save result into file words_largest_time_in_document.txt
  7. generate tf_idf_infos.txt by using file generated before

EACH time I run this program to query, it will only read files which was generated before.
THEREFORE, the speed will be very very fast!
IT only cost 0.2s for initialize and 0s - 0.5s for query in my computer!

SAMPLE RUN:
python3 main.py
init success! Cost time: 0.18 seconds
Ready to query (enter nothing to exit):presence of the edge shearing forces is found to diminish the
top 	1:	index: 1398	value: 0.3163882400671663
top 	2:	index: 180	value: 0.24636271557249323
top 	3:	index: 1251	value: 0.2125048466313413
top 	4:	index: 393	value: 0.17523415251416374
top 	5:	index: 902	value: 0.1675118123317311
top 	6:	index: 659	value: 0.15813350685850522
top 	7:	index: 418	value: 0.15422659723725576
top 	8:	index: 484	value: 0.1505999141104824
top 	9:	index: 412	value: 0.14852445572990655
top 	10:	index: 1387	value: 0.14449611034139545
top 	11:	index: 392	value: 0.1438114152458597
top 	12:	index: 298	value: 0.14007986266733058
top 	13:	index: 211	value: 0.1383993280203818
top 	14:	index: 943	value: 0.12948980858893883
top 	15:	index: 3	value: 0.1291515686865229
top 	16:	index: 655	value: 0.1260178644154235
top 	17:	index: 4	value: 0.12568181489865266
top 	18:	index: 664	value: 0.12244617921949817
top 	19:	index: 398	value: 0.12186609356726529
top 	20:	index: 389	value: 0.11704235554125338
top 	21:	index: 854	value: 0.11689002636044349
top 	22:	index: 514	value: 0.11683381564780387
top 	23:	index: 388	value: 0.11671928022828106
top 	24:	index: 683	value: 0.1163126873728579
top 	25:	index: 894	value: 0.11370032325336274
top 	26:	index: 420	value: 0.1133735841841835
top 	27:	index: 1244	value: 0.11286714511214108
top 	28:	index: 465	value: 0.1111292672643832
top 	29:	index: 65	value: 0.11035002451560702
top 	30:	index: 481	value: 0.10804393497522198
top 	31:	index: 1276	value: 0.10576307219509348
top 	32:	index: 826	value: 0.09923890482403291
top 	33:	index: 109	value: 0.0987269006491559
top 	34:	index: 434	value: 0.09808271237984326
top 	35:	index: 11	value: 0.09720087755423734
top 	36:	index: 1397	value: 0.09690697972540267
top 	37:	index: 1396	value: 0.09658198978692756
top 	38:	index: 222	value: 0.09543897446728235
top 	39:	index: 601	value: 0.09377016869785114
top 	40:	index: 324	value: 0.0937130176366279
top 	41:	index: 625	value: 0.09171679274346829
top 	42:	index: 1037	value: 0.09123419533285587
top 	43:	index: 788	value: 0.08945276758460528
top 	44:	index: 966	value: 0.08803937805238261
top 	45:	index: 255	value: 0.08800456401737565
top 	46:	index: 1392	value: 0.08783065059188733
top 	47:	index: 1106	value: 0.08778381035356439
top 	48:	index: 940	value: 0.0875175460314258
top 	49:	index: 453	value: 0.08605780166307417
top 	50:	index: 900	value: 0.08594961344019389
top 	51:	index: 1322	value: 0.08581588742181252
top 	52:	index: 736	value: 0.08572655480088323
top 	53:	index: 1255	value: 0.08489178261069688
top 	54:	index: 121	value: 0.08301039585817559
top 	55:	index: 400	value: 0.08248206391769881
top 	56:	index: 1349	value: 0.08072673780846142
top 	57:	index: 889	value: 0.08037352808140806
top 	58:	index: 116	value: 0.07983323426447135
top 	59:	index: 660	value: 0.0797560992823598
top 	60:	index: 1289	value: 0.07923138945669868
top 	61:	index: 452	value: 0.07916468181725687
top 	62:	index: 599	value: 0.07878536840712436
top 	63:	index: 252	value: 0.0786110462349943
top 	64:	index: 569	value: 0.07856084544875558
top 	65:	index: 929	value: 0.07844119846364059
top 	66:	index: 973	value: 0.07825387180721281
top 	67:	index: 102	value: 0.07776786567756777
top 	68:	index: 191	value: 0.07766702885866171
top 	69:	index: 903	value: 0.07709820703265695
top 	70:	index: 786	value: 0.07678963874167416
top 	71:	index: 644	value: 0.07563619838681655
top 	72:	index: 210	value: 0.074944928153577
top 	73:	index: 735	value: 0.07490359720471561
top 	74:	index: 2	value: 0.07442248568721783
top 	75:	index: 901	value: 0.0742826307604938
top 	76:	index: 155	value: 0.07417669946243857
top 	77:	index: 269	value: 0.07410029610781782
top 	78:	index: 87	value: 0.07321303187180447
top 	79:	index: 843	value: 0.07275463846550823
top 	80:	index: 424	value: 0.07269555856647063
top 	81:	index: 661	value: 0.07227876068199884
top 	82:	index: 1273	value: 0.07200057550915707
top 	83:	index: 1343	value: 0.07188779492563832
top 	84:	index: 397	value: 0.07127494966319586
top 	85:	index: 933	value: 0.07097642937049227
top 	86:	index: 334	value: 0.06997924807626352
top 	87:	index: 407	value: 0.06995530803537828
top 	88:	index: 947	value: 0.06985763274303727
top 	89:	index: 439	value: 0.0694585552315643
top 	90:	index: 270	value: 0.06938108441877537
top 	91:	index: 651	value: 0.06851395422770194
top 	92:	index: 1060	value: 0.06815839525717195
top 	93:	index: 1302	value: 0.06778759390333879
top 	94:	index: 521	value: 0.06731520323137534
top 	95:	index: 1300	value: 0.06722486068168283
top 	96:	index: 1239	value: 0.06700716005012233
top 	97:	index: 1236	value: 0.06629125799199441
top 	98:	index: 1304	value: 0.06629117771052774
top 	99:	index: 887	value: 0.06607376785683292
top 	100:	index: 974	value: 0.06564545199400493
query success! Cost time: 0.06 seconds

Enter document number to see content (enter nothing to exit):1398

============================================
stability of rectangular plates under shear and bending
forces .
  the author first discusses the problem of a plane, simply
supported rectangular plate loaded by shearing forces in
the plane of the plate on all four edges .  there are two
stiffeners attached one third and two thirds of the way
along the plate .  the critical load is calculated for various
stiffener rigidities .  also, the rigidity necessary to keep
the stiffeners straight when the plate buckles is found .
this stiffener rigidity is found to be slightly larger than
that necessary for a plate with one stiffener and the same
panel dimensions as the plate with two stiffeners .
  the second problem discussed by the author is that of a
plane, simply supported rectangular plate loaded by
uniformly distributed edge shearing forces in the plane of the
plate and linearly distributed tension and compression in
the plane of the plate at the ends .  the end forces vary
from tension, at one corner to, at the other corner,
so that their resultant is a bending moment .  the
presence of the edge shearing forces is found to diminish the
critical bending stress in this case .  calculations are made
for various magnitudes of bending and shearing forces for
plates of various proportions .
============================================

Enter document number to see content (enter nothing to exit):
Ready to query(enter nothing to stop):