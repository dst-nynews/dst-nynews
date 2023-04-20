--
-- PostgreSQL database cluster dump
--

-- Started on 2023-04-20 13:42:10

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;






--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.2

-- Started on 2023-04-20 13:42:10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2023-04-20 13:42:12

--
-- PostgreSQL database dump complete
--

--
-- Database "covid" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.2

-- Started on 2023-04-20 13:42:12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2955 (class 1262 OID 16384)
-- Name: covid; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE covid WITH TEMPLATE = template0 ENCODING = 'UTF8';


ALTER DATABASE covid OWNER TO postgres;

\connect covid

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16393)
-- Name: counties; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.counties (
    id integer NOT NULL,
    name character varying,
    fips integer,
    id_state integer
);


ALTER TABLE public.counties OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16406)
-- Name: counts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.counts (
    id integer NOT NULL,
    date date,
    cases integer,
    deaths integer,
    id_state integer,
    id_county integer
);


ALTER TABLE public.counts OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16421)
-- Name: mask_use; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mask_use (
    id integer NOT NULL,
    never double precision,
    rarely double precision,
    sometimes double precision,
    frequently double precision,
    always double precision,
    id_county integer
);


ALTER TABLE public.mask_use OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16385)
-- Name: states; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.states (
    id integer NOT NULL,
    name character varying,
    fips integer
);


ALTER TABLE public.states OWNER TO postgres;

--
-- TOC entry 2947 (class 0 OID 16393)
-- Dependencies: 203
-- Data for Name: counties; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.counties (id, name, fips, id_state) FROM stdin;
0	Abbeville	45001	44
1	Acadia	22001	20
2	Accomack	51001	51
3	Ada	16001	14
4	Adair	21001	19
5	Adair	29001	27
6	Adair	40001	39
7	Adair	19001	17
8	Adams	18001	16
9	Adams	16003	14
10	Adams	31001	29
11	Adams	55001	54
12	Adams	8001	6
13	Adams	38001	36
14	Adams	42001	41
15	Adams	28001	26
16	Adams	17001	15
17	Adams	39001	38
18	Adams	53001	52
19	Adams	19003	17
20	Addison	50001	49
21	Adjuntas	72001	42
22	Aguada	72003	42
23	Aguadilla	72005	42
24	Aguas Buenas	72007	42
25	Aibonito	72009	42
26	Aiken	45003	44
27	Aitkin	27001	25
28	Alachua	12001	10
29	Alamance	37001	35
30	Alameda	6001	5
31	Alamosa	8003	6
32	Albany	36001	34
33	Albany	56001	55
34	Albemarle	51003	51
35	Alcona	26001	24
36	Alcorn	28003	26
37	Aleutians East Borough	2013	1
38	Aleutians West Census Area	2016	1
39	Alexander	37003	35
40	Alexander	17003	15
41	Alexandria city	51510	51
42	Alfalfa	40003	39
43	Alger	26003	24
44	Allamakee	19005	17
45	Allegan	26005	24
46	Allegany	24001	22
47	Allegany	36003	34
48	Alleghany	51005	51
49	Alleghany	37005	35
50	Allegheny	42003	41
51	Allen	20001	18
52	Allen	22003	20
53	Allen	39003	38
54	Allen	21003	19
55	Allen	18003	16
56	Allendale	45005	44
57	Alpena	26007	24
58	Alpine	6003	5
59	Amador	6005	5
60	Amelia	51007	51
61	Amherst	51009	51
62	Amite	28005	26
63	Anasco	72011	42
64	Anchorage	2020	1
65	Anderson	47001	46
66	Anderson	45007	44
67	Anderson	48001	47
68	Anderson	21005	19
69	Anderson	20003	18
70	Andrew	29003	27
71	Andrews	48003	47
72	Androscoggin	23001	21
73	Angelina	48005	47
74	Anne Arundel	24003	22
75	Anoka	27003	25
76	Anson	37007	35
77	Antelope	31003	29
78	Antrim	26009	24
79	Apache	4001	3
80	Appanoose	19007	17
81	Appling	13001	11
82	Appomattox	51011	51
83	Aransas	48007	47
84	Arapahoe	8005	6
85	Archer	48009	47
86	Archuleta	8007	6
87	Arecibo	72013	42
88	Arenac	26011	24
89	Arkansas	5001	4
90	Arlington	51013	51
91	Armstrong	42005	41
92	Armstrong	48011	47
93	Aroostook	23003	21
94	Arroyo	72015	42
95	Arthur	31005	29
96	Ascension	22005	20
97	Ashe	37009	35
98	Ashland	55003	54
99	Ashland	39005	38
100	Ashley	5003	4
101	Ashtabula	39007	38
102	Asotin	53003	52
103	Assumption	22007	20
104	Atascosa	48013	47
105	Atchison	20005	18
106	Atchison	29005	27
107	Athens	39009	38
108	Atkinson	13003	11
109	Atlantic	34001	32
110	Atoka	40005	39
111	Attala	28007	26
112	Audrain	29007	27
113	Audubon	19009	17
114	Auglaize	39011	38
115	Augusta	51015	51
116	Aurora	46003	45
117	Austin	48015	47
118	Autauga	1001	0
119	Avery	37011	35
120	Avoyelles	22009	20
121	Baca	8009	6
122	Bacon	13005	11
123	Bailey	48017	47
124	Baker	41001	40
125	Baker	13007	11
126	Baker	12003	10
127	Baldwin	1003	0
128	Baldwin	13009	11
129	Ballard	21007	19
130	Baltimore	24005	22
131	Baltimore city	24510	22
132	Bamberg	45009	44
133	Bandera	48019	47
134	Banks	13011	11
135	Banner	31007	29
136	Bannock	16005	14
137	Baraga	26013	24
138	Barber	20007	18
139	Barbour	54001	53
140	Barbour	1005	0
141	Barceloneta	72017	42
142	Barnes	38003	36
143	Barnstable	25001	23
144	Barnwell	45011	44
145	Barranquitas	72019	42
146	Barren	21009	19
147	Barron	55005	54
148	Barrow	13013	11
149	Barry	29009	27
150	Barry	26015	24
151	Bartholomew	18005	16
152	Barton	20009	18
153	Barton	29011	27
154	Bartow	13015	11
155	Bastrop	48021	47
156	Bates	29013	27
157	Bath	21011	19
158	Bath	51017	51
159	Baxter	5005	4
160	Bay	12005	10
161	Bay	26017	24
162	Bayamon	72021	42
163	Bayfield	55007	54
164	Baylor	48023	47
165	Beadle	46005	45
166	Bear Lake	16007	14
167	Beaufort	45013	44
168	Beaufort	37013	35
169	Beauregard	22011	20
170	Beaver	40007	39
171	Beaver	42007	41
172	Beaver	49001	48
173	Beaverhead	30001	28
174	Becker	27005	25
175	Beckham	40009	39
176	Bedford	47003	46
177	Bedford	51019	51
178	Bedford	42009	41
179	Bee	48025	47
180	Belknap	33001	31
181	Bell	21013	19
182	Bell	48027	47
183	Belmont	39013	38
184	Beltrami	27007	25
185	Ben Hill	13017	11
186	Benewah	16009	14
187	Bennett	46007	45
188	Bennington	50003	49
189	Benson	38005	36
190	Bent	8011	6
191	Benton	27009	25
192	Benton	18007	16
193	Benton	5007	4
194	Benton	28009	26
195	Benton	47005	46
196	Benton	41003	40
197	Benton	19011	17
198	Benton	53005	52
199	Benton	29015	27
200	Benzie	26019	24
201	Bergen	34003	32
202	Berkeley	45015	44
203	Berkeley	54003	53
204	Berks	42011	41
205	Berkshire	25003	23
206	Bernalillo	35001	33
207	Berrien	13019	11
208	Berrien	26021	24
209	Bertie	37015	35
210	Bethel Census Area	2050	1
211	Bexar	48029	47
212	Bibb	1007	0
213	Bibb	13021	11
214	Bienville	22013	20
215	Big Horn	30003	28
216	Big Horn	56003	55
217	Big Stone	27011	25
218	Billings	38007	36
219	Bingham	16011	14
220	Black Hawk	19013	17
221	Blackford	18009	16
222	Bladen	37017	35
223	Blaine	40011	39
224	Blaine	16013	14
225	Blaine	30005	28
226	Blaine	31009	29
227	Blair	42013	41
228	Blanco	48031	47
229	Bland	51021	51
230	Bleckley	13023	11
231	Bledsoe	47007	46
232	Blount	1009	0
233	Blount	47009	46
234	Blue Earth	27013	25
235	Boise	16015	14
236	Bolivar	28011	26
237	Bollinger	29017	27
238	Bon Homme	46009	45
239	Bond	17005	15
240	Bonner	16017	14
241	Bonneville	16019	14
242	Boone	18011	16
243	Boone	31011	29
244	Boone	5009	4
245	Boone	54005	53
246	Boone	17007	15
247	Boone	19015	17
248	Boone	21015	19
249	Boone	29019	27
250	Borden	48033	47
251	Bosque	48035	47
252	Bossier	22015	20
253	Botetourt	51023	51
254	Bottineau	38009	36
255	Boulder	8013	6
256	Boundary	16021	14
257	Bourbon	20011	18
258	Bourbon	21017	19
259	Bowie	48037	47
260	Bowman	38011	36
261	Box Butte	31013	29
262	Box Elder	49003	48
263	Boyd	31015	29
264	Boyd	21019	19
265	Boyle	21021	19
266	Bracken	21023	19
267	Bradford	12007	10
268	Bradford	42015	41
269	Bradley	5011	4
270	Bradley	47011	46
271	Branch	26023	24
272	Brantley	13025	11
273	Braxton	54007	53
274	Brazoria	48039	47
275	Brazos	48041	47
276	Breathitt	21025	19
277	Breckinridge	21027	19
278	Bremer	19017	17
279	Brevard	12009	10
280	Brewster	48043	47
281	Briscoe	48045	47
282	Bristol	44001	43
283	Bristol	25005	23
284	Bristol Bay plus Lake and Peninsula	2997	1
285	Bristol city	51520	51
286	Broadwater	30007	28
287	Brooke	54009	53
288	Brookings	46011	45
289	Brooks	13027	11
290	Brooks	48047	47
291	Broome	36007	34
292	Broomfield	8014	6
293	Broward	12011	10
294	Brown	18013	16
295	Brown	27015	25
296	Brown	55009	54
297	Brown	39015	38
298	Brown	46013	45
299	Brown	17009	15
300	Brown	48049	47
301	Brown	20013	18
302	Brown	31017	29
303	Brule	46015	45
304	Brunswick	37019	35
305	Brunswick	51025	51
306	Bryan	13029	11
307	Bryan	40013	39
308	Buchanan	19019	17
309	Buchanan	51027	51
310	Buchanan	29021	27
311	Buckingham	51029	51
312	Bucks	42017	41
313	Buena Vista	19021	17
314	Buena Vista city	51530	51
315	Buffalo	46017	45
316	Buffalo	31019	29
317	Buffalo	55011	54
318	Bullitt	21029	19
319	Bulloch	13031	11
320	Bullock	1011	0
321	Buncombe	37021	35
322	Bureau	17011	15
323	Burke	38013	36
324	Burke	37023	35
325	Burke	13033	11
326	Burleigh	38015	36
327	Burleson	48051	47
328	Burlington	34005	32
329	Burnet	48053	47
330	Burnett	55013	54
331	Burt	31021	29
332	Butler	31023	29
333	Butler	42019	41
334	Butler	21031	19
335	Butler	39017	38
336	Butler	20015	18
337	Butler	29023	27
338	Butler	1013	0
339	Butler	19023	17
340	Butte	46019	45
341	Butte	16023	14
342	Butte	6007	5
343	Butts	13035	11
344	Cabarrus	37025	35
345	Cabell	54011	53
346	Cabo Rojo	72023	42
347	Cache	49005	48
348	Caddo	22017	20
349	Caddo	40015	39
350	Caguas	72025	42
351	Calaveras	6009	5
352	Calcasieu	22019	20
353	Caldwell	21033	19
354	Caldwell	37027	35
355	Caldwell	22021	20
356	Caldwell	48055	47
357	Caldwell	29025	27
358	Caledonia	50005	49
359	Calhoun	28013	26
360	Calhoun	54013	53
361	Calhoun	48057	47
362	Calhoun	26025	24
363	Calhoun	1015	0
364	Calhoun	17013	15
365	Calhoun	5013	4
366	Calhoun	19025	17
367	Calhoun	13037	11
368	Calhoun	12013	10
369	Calhoun	45017	44
370	Callahan	48059	47
371	Callaway	29027	27
372	Calloway	21035	19
373	Calumet	55015	54
374	Calvert	24009	22
375	Camas	16025	14
376	Cambria	42021	41
377	Camden	13039	11
378	Camden	37029	35
379	Camden	29029	27
380	Camden	34007	32
381	Cameron	42023	41
382	Cameron	48061	47
383	Cameron	22023	20
384	Camp	48063	47
385	Campbell	56005	55
386	Campbell	21037	19
387	Campbell	51031	51
388	Campbell	47013	46
389	Campbell	46021	45
390	Camuy	72027	42
391	Canadian	40017	39
392	Candler	13043	11
393	Cannon	47015	46
394	Canovanas	72029	42
395	Canyon	16027	14
396	Cape Girardeau	29031	27
397	Cape May	34009	32
398	Carbon	56007	55
399	Carbon	49007	48
400	Carbon	42025	41
401	Carbon	30009	28
402	Caribou	16029	14
403	Carlisle	21039	19
404	Carlton	27017	25
405	Carolina	72031	42
406	Caroline	51033	51
407	Caroline	24011	22
408	Carroll	33003	31
409	Carroll	47017	46
410	Carroll	5015	4
411	Carroll	29033	27
412	Carroll	19027	17
413	Carroll	21041	19
414	Carroll	17015	15
415	Carroll	39019	38
416	Carroll	24013	22
417	Carroll	51035	51
418	Carroll	18015	16
419	Carroll	28015	26
420	Carroll	13045	11
421	Carson	48065	47
422	Carson City	32510	30
423	Carter	30011	28
424	Carter	29035	27
425	Carter	21043	19
426	Carter	47019	46
427	Carter	40019	39
428	Carteret	37031	35
429	Carver	27019	25
430	Cascade	30013	28
431	Casey	21045	19
432	Cass	31025	29
433	Cass	38017	36
434	Cass	18017	16
435	Cass	29037	27
436	Cass	48067	47
437	Cass	26027	24
438	Cass	19029	17
439	Cass	17017	15
440	Cass	27021	25
441	Cassia	16031	14
442	Castro	48069	47
443	Caswell	37033	35
444	Catahoula	22025	20
445	Catano	72033	42
446	Catawba	37035	35
447	Catoosa	13047	11
448	Catron	35003	33
449	Cattaraugus	36009	34
450	Cavalier	38019	36
451	Cayey	72035	42
452	Cayuga	36011	34
453	Cecil	24015	22
454	Cedar	31027	29
455	Cedar	19031	17
456	Cedar	29039	27
457	Ceiba	72037	42
458	Centre	42027	41
459	Cerro Gordo	19033	17
460	Chaffee	8015	6
461	Chambers	1017	0
462	Chambers	48071	47
463	Champaign	17019	15
464	Champaign	39021	38
465	Chariton	29041	27
466	Charles	24017	22
467	Charles City	51036	51
468	Charles Mix	46023	45
469	Charleston	45019	44
470	Charlevoix	26029	24
471	Charlotte	51037	51
472	Charlotte	12015	10
473	Charlottesville city	51540	51
474	Charlton	13049	11
475	Chase	20017	18
476	Chase	31029	29
477	Chatham	37037	35
478	Chatham	13051	11
479	Chattahoochee	13053	11
480	Chattooga	13055	11
481	Chautauqua	20019	18
482	Chautauqua	36013	34
483	Chaves	35005	33
484	Cheatham	47021	46
485	Cheboygan	26031	24
486	Chelan	53007	52
487	Chemung	36015	34
488	Chenango	36017	34
489	Cherokee	40021	39
490	Cherokee	20021	18
491	Cherokee	19035	17
492	Cherokee	48073	47
493	Cherokee	1019	0
494	Cherokee	45021	44
495	Cherokee	13057	11
496	Cherokee	37039	35
497	Cherry	31031	29
498	Chesapeake city	51550	51
499	Cheshire	33005	31
500	Chester	47023	46
501	Chester	42029	41
502	Chester	45023	44
503	Chesterfield	51041	51
504	Chesterfield	45025	44
505	Cheyenne	8017	6
506	Cheyenne	20023	18
507	Cheyenne	31033	29
508	Chickasaw	28017	26
509	Chickasaw	19037	17
510	Chicot	5017	4
511	Childress	48075	47
512	Chilton	1021	0
513	Chippewa	26033	24
514	Chippewa	55017	54
515	Chippewa	27023	25
516	Chisago	27025	25
517	Chittenden	50007	49
518	Choctaw	1023	0
519	Choctaw	40023	39
520	Choctaw	28019	26
521	Chouteau	30015	28
522	Chowan	37041	35
523	Christian	17021	15
524	Christian	29043	27
525	Christian	21047	19
526	Churchill	32001	30
527	Ciales	72039	42
528	Cibola	35006	33
529	Cidra	72041	42
530	Cimarron	40025	39
531	Citrus	12017	10
532	Clackamas	41005	40
533	Claiborne	28021	26
534	Claiborne	47025	46
535	Claiborne	22027	20
536	Clallam	53009	52
537	Clare	26035	24
538	Clarendon	45027	44
539	Clarion	42031	41
540	Clark	39023	38
541	Clark	46025	45
542	Clark	18019	16
543	Clark	17023	15
544	Clark	5019	4
545	Clark	21049	19
546	Clark	29045	27
547	Clark	55019	54
548	Clark	20025	18
549	Clark	32003	30
550	Clark	16033	14
551	Clark	53011	52
552	Clarke	1025	0
553	Clarke	13059	11
554	Clarke	51043	51
555	Clarke	28023	26
556	Clarke	19039	17
557	Clatsop	41007	40
558	Clay	1027	0
559	Clay	46027	45
560	Clay	48077	47
561	Clay	12019	10
562	Clay	29047	27
563	Clay	47027	46
564	Clay	21051	19
565	Clay	27027	25
566	Clay	17025	15
567	Clay	18021	16
568	Clay	54015	53
569	Clay	20027	18
570	Clay	5021	4
571	Clay	13061	11
572	Clay	28025	26
573	Clay	37043	35
574	Clay	19041	17
575	Clay	31035	29
576	Clayton	13063	11
577	Clayton	19043	17
578	Clear Creek	8019	6
579	Clearfield	42033	41
580	Clearwater	27029	25
581	Clearwater	16035	14
582	Cleburne	5023	4
583	Cleburne	1029	0
584	Clermont	39025	38
585	Cleveland	5025	4
586	Cleveland	37045	35
587	Cleveland	40027	39
588	Clinch	13065	11
589	Clinton	26037	24
590	Clinton	36019	34
591	Clinton	42035	41
592	Clinton	17027	15
593	Clinton	19045	17
594	Clinton	29049	27
595	Clinton	21053	19
596	Clinton	18023	16
597	Clinton	39027	38
598	Cloud	20029	18
599	Coahoma	28027	26
600	Coal	40029	39
601	Coamo	72043	42
602	Cobb	13067	11
603	Cochise	4003	3
604	Cochran	48079	47
605	Cocke	47029	46
606	Coconino	4005	3
607	Codington	46029	45
608	Coffee	13069	11
609	Coffee	47031	46
610	Coffee	1031	0
611	Coffey	20031	18
612	Coke	48081	47
613	Colbert	1033	0
614	Cole	29051	27
615	Coleman	48083	47
616	Coles	17029	15
617	Colfax	35007	33
618	Colfax	31037	29
619	Colleton	45029	44
620	Collier	12021	10
621	Collin	48085	47
622	Collingsworth	48087	47
623	Colonial Heights city	51570	51
624	Colorado	48089	47
625	Colquitt	13071	11
626	Columbia	36021	34
627	Columbia	13073	11
628	Columbia	55021	54
629	Columbia	12023	10
630	Columbia	53013	52
631	Columbia	41009	40
632	Columbia	42037	41
633	Columbia	5027	4
634	Columbiana	39029	38
635	Columbus	37047	35
636	Colusa	6011	5
637	Comal	48091	47
638	Comanche	40031	39
639	Comanche	48093	47
640	Comanche	20033	18
641	Comerio	72045	42
642	Concho	48095	47
643	Concordia	22029	20
644	Conecuh	1035	0
645	Conejos	8021	6
646	Contra Costa	6013	5
647	Converse	56009	55
648	Conway	5029	4
649	Cook	17031	15
650	Cook	13075	11
651	Cook	27031	25
652	Cooke	48097	47
653	Cooper	29053	27
654	Coos	33007	31
655	Coos	41011	40
656	Coosa	1037	0
657	Copiah	28029	26
658	Corozal	72047	42
659	Corson	46031	45
660	Cortland	36023	34
661	Coryell	48099	47
662	Coshocton	39031	38
663	Costilla	8023	6
664	Cottle	48101	47
665	Cotton	40033	39
666	Cottonwood	27033	25
667	Covington	1039	0
668	Covington	28031	26
669	Covington city	51580	51
670	Coweta	13077	11
671	Cowley	20035	18
672	Cowlitz	53015	52
673	Craig	51045	51
674	Craig	40035	39
675	Craighead	5031	4
676	Crane	48103	47
677	Craven	37049	35
678	Crawford	20037	18
679	Crawford	39033	38
680	Crawford	42039	41
681	Crawford	5033	4
682	Crawford	55023	54
683	Crawford	29055	27
684	Crawford	19047	17
685	Crawford	17033	15
686	Crawford	18025	16
687	Crawford	13079	11
688	Crawford	26039	24
689	Creek	40037	39
690	Crenshaw	1041	0
691	Crisp	13081	11
692	Crittenden	5035	4
693	Crittenden	21055	19
694	Crockett	48105	47
695	Crockett	47033	46
696	Crook	41013	40
697	Crook	56011	55
698	Crosby	48107	47
699	Cross	5037	4
700	Crow Wing	27035	25
701	Crowley	8025	6
702	Culberson	48109	47
703	Culebra	72049	42
704	Cullman	1043	0
705	Culpeper	51047	51
706	Cumberland	23005	21
707	Cumberland	42041	41
708	Cumberland	21057	19
709	Cumberland	51049	51
710	Cumberland	17035	15
711	Cumberland	37051	35
712	Cumberland	47035	46
713	Cumberland	34011	32
714	Cuming	31039	29
715	Currituck	37053	35
716	Curry	41015	40
717	Curry	35009	33
718	Custer	16037	14
719	Custer	46033	45
720	Custer	31041	29
721	Custer	40039	39
722	Custer	8027	6
723	Custer	30017	28
724	Cuyahoga	39035	38
725	Dade	13083	11
726	Dade	29057	27
727	Daggett	49009	48
728	Dakota	27037	25
729	Dakota	31043	29
730	Dale	1045	0
731	Dallam	48111	47
732	Dallas	5039	4
733	Dallas	48113	47
734	Dallas	29059	27
735	Dallas	1047	0
736	Dallas	19049	17
737	Dane	55025	54
738	Daniels	30019	28
739	Danville city	51590	51
740	Dare	37055	35
741	Darke	39037	38
742	Darlington	45031	44
743	Dauphin	42043	41
744	Davidson	47037	46
745	Davidson	37057	35
746	Davie	37059	35
747	Daviess	18027	16
748	Daviess	21059	19
749	Daviess	29061	27
750	Davis	19051	17
751	Davis	49011	48
752	Davison	46035	45
753	Dawes	31045	29
754	Dawson	48115	47
755	Dawson	30021	28
756	Dawson	13085	11
757	Dawson	31047	29
758	Day	46037	45
759	De Baca	35011	33
760	De Soto	22031	20
761	De Witt	17039	15
762	DeKalb	17037	15
763	DeKalb	18033	16
764	DeKalb	29063	27
765	DeKalb	13089	11
766	DeKalb	47041	46
767	DeKalb	1049	0
768	DeSoto	28033	26
769	DeSoto	12027	10
770	DeWitt	48123	47
771	Deaf Smith	48117	47
772	Dearborn	18029	16
773	Decatur	47039	46
774	Decatur	18031	16
775	Decatur	20039	18
776	Decatur	19053	17
777	Decatur	13087	11
778	Deer Lodge	30023	28
779	Defiance	39039	38
780	Del Norte	6015	5
781	Delaware	40041	39
782	Delaware	39041	38
783	Delaware	19055	17
784	Delaware	18035	16
785	Delaware	36025	34
786	Delaware	42045	41
787	Delta	48119	47
788	Delta	8029	6
789	Delta	26041	24
790	Denali Borough	2068	1
791	Dent	29065	27
792	Denton	48121	47
793	Denver	8031	6
794	Des Moines	19057	17
795	Deschutes	41017	40
796	Desha	5041	4
797	Deuel	46039	45
798	Deuel	31049	29
799	Dewey	40043	39
800	Dewey	46041	45
801	Dickens	48125	47
802	Dickenson	51051	51
803	Dickey	38021	36
804	Dickinson	20041	18
805	Dickinson	19059	17
806	Dickinson	26043	24
807	Dickson	47043	46
808	Dillingham Census Area	2070	1
809	Dillon	45033	44
810	Dimmit	48127	47
811	Dinwiddie	51053	51
812	District of Columbia	11001	9
813	Divide	38023	36
814	Dixie	12029	10
815	Dixon	31051	29
816	Doddridge	54017	53
817	Dodge	27039	25
818	Dodge	31053	29
819	Dodge	55027	54
820	Dodge	13091	11
821	Dolores	8033	6
822	Doniphan	20043	18
823	Donley	48129	47
824	Dooly	13093	11
825	Door	55029	54
826	Dorado	72051	42
827	Dorchester	24019	22
828	Dorchester	45035	44
829	Dougherty	13095	11
830	Douglas	13097	11
831	Douglas	17041	15
832	Douglas	32005	30
833	Douglas	29067	27
834	Douglas	27041	25
835	Douglas	53017	52
836	Douglas	31055	29
837	Douglas	8035	6
838	Douglas	46043	45
839	Douglas	20045	18
840	Douglas	41019	40
841	Douglas	55031	54
842	Doña Ana	35013	33
843	Drew	5043	4
844	DuPage	17043	15
845	Dubois	18037	16
846	Dubuque	19061	17
847	Duchesne	49013	48
848	Dukes	25007	23
849	Dundy	31057	29
850	Dunklin	29069	27
851	Dunn	38025	36
852	Dunn	55033	54
853	Duplin	37061	35
854	Durham	37063	35
855	Dutchess	36027	34
856	Duval	48131	47
857	Duval	12031	10
858	Dyer	47045	46
859	Eagle	8037	6
860	Early	13099	11
861	East Baton Rouge	22033	20
862	East Carroll	22035	20
863	East Feliciana	22037	20
864	Eastland	48133	47
865	Eaton	26045	24
866	Eau Claire	55035	54
867	Echols	13101	11
868	Ector	48135	47
869	Eddy	35015	33
870	Eddy	38027	36
871	Edgar	17045	15
872	Edgecombe	37065	35
873	Edgefield	45037	44
874	Edmonson	21061	19
875	Edmunds	46045	45
876	Edwards	48137	47
877	Edwards	17047	15
878	Edwards	20047	18
879	Effingham	17049	15
880	Effingham	13103	11
881	El Dorado	6017	5
882	El Paso	8041	6
883	El Paso	48141	47
884	Elbert	8039	6
885	Elbert	13105	11
886	Elk	20049	18
887	Elk	42047	41
888	Elkhart	18039	16
889	Elko	32007	30
890	Elliott	21063	19
891	Ellis	40045	39
892	Ellis	20051	18
893	Ellis	48139	47
894	Ellsworth	20053	18
895	Elmore	1051	0
896	Elmore	16039	14
897	Emanuel	13107	11
898	Emery	49015	48
899	Emmet	26047	24
900	Emmet	19063	17
901	Emmons	38029	36
902	Emporia city	51595	51
903	Erath	48143	47
904	Erie	36029	34
905	Erie	39043	38
906	Erie	42049	41
907	Escambia	1053	0
908	Escambia	12033	10
909	Esmeralda	32009	30
910	Essex	34013	32
911	Essex	25009	23
912	Essex	36031	34
913	Essex	51057	51
914	Essex	50009	49
915	Estill	21065	19
916	Etowah	1055	0
917	Eureka	32011	30
918	Evangeline	22039	20
919	Evans	13109	11
920	Fairbanks North Star Borough	2090	1
921	Fairfax	51059	51
922	Fairfax city	51600	51
923	Fairfield	9001	7
924	Fairfield	39045	38
925	Fairfield	45039	44
926	Fajardo	72053	42
927	Fall River	46047	45
928	Fallon	30025	28
929	Falls	48145	47
930	Falls Church city	51610	51
931	Fannin	48147	47
932	Fannin	13111	11
933	Faribault	27043	25
934	Faulk	46049	45
935	Faulkner	5045	4
936	Fauquier	51061	51
937	Fayette	13113	11
938	Fayette	18041	16
939	Fayette	19065	17
940	Fayette	42051	41
941	Fayette	17051	15
942	Fayette	1057	0
943	Fayette	39047	38
944	Fayette	21067	19
945	Fayette	47047	46
946	Fayette	48149	47
947	Fayette	54019	53
948	Fentress	47049	46
949	Fergus	30027	28
950	Ferry	53019	52
951	Fillmore	27045	25
952	Fillmore	31059	29
953	Finney	20055	18
954	Fisher	48151	47
955	Flagler	12035	10
956	Flathead	30029	28
957	Fleming	21069	19
958	Florence	55037	54
959	Florence	45041	44
960	Florida	72054	42
961	Floyd	21071	19
962	Floyd	19067	17
963	Floyd	18043	16
964	Floyd	13115	11
965	Floyd	51063	51
966	Floyd	48153	47
967	Fluvanna	51065	51
968	Foard	48155	47
969	Fond du Lac	55039	54
970	Ford	20057	18
971	Ford	17053	15
972	Forest	42053	41
973	Forest	55041	54
974	Forrest	28035	26
975	Forsyth	13117	11
976	Forsyth	37067	35
977	Fort Bend	48157	47
978	Foster	38031	36
979	Fountain	18045	16
980	Franklin	22041	20
981	Franklin	12037	10
982	Franklin	23007	21
983	Franklin	39049	38
984	Franklin	25011	23
985	Franklin	21073	19
986	Franklin	20059	18
987	Franklin	29071	27
988	Franklin	18047	16
989	Franklin	17055	15
990	Franklin	50011	49
991	Franklin	19069	17
992	Franklin	37069	35
993	Franklin	13119	11
994	Franklin	48159	47
995	Franklin	42055	41
996	Franklin	1059	0
997	Franklin	47051	46
998	Franklin	53021	52
999	Franklin	31061	29
1000	Franklin	5047	4
1001	Franklin	36033	34
1002	Franklin	28037	26
1003	Franklin	51067	51
1004	Franklin	16041	14
1005	Franklin city	51620	51
1006	Frederick	51069	51
1007	Frederick	24021	22
1008	Fredericksburg city	51630	51
1009	Freeborn	27047	25
1010	Freestone	48161	47
1011	Fremont	16043	14
1012	Fremont	56013	55
1013	Fremont	19071	17
1014	Fremont	8043	6
1015	Fresno	6019	5
1016	Frio	48163	47
1017	Frontier	31063	29
1018	Fulton	39051	38
1019	Fulton	17057	15
1020	Fulton	36035	34
1021	Fulton	42057	41
1022	Fulton	18049	16
1023	Fulton	21075	19
1024	Fulton	5049	4
1025	Fulton	13121	11
1026	Furnas	31065	29
1027	Gadsden	12039	10
1028	Gage	31067	29
1029	Gaines	48165	47
1030	Galax city	51640	51
1031	Gallatin	17059	15
1032	Gallatin	30031	28
1033	Gallatin	21077	19
1034	Gallia	39053	38
1035	Galveston	48167	47
1036	Garden	31069	29
1037	Garfield	49017	48
1038	Garfield	31071	29
1039	Garfield	8045	6
1040	Garfield	40047	39
1041	Garfield	30033	28
1042	Garfield	53023	52
1043	Garland	5051	4
1044	Garrard	21079	19
1045	Garrett	24023	22
1046	Garvin	40049	39
1047	Garza	48169	47
1048	Gasconade	29073	27
1049	Gaston	37071	35
1050	Gates	37073	35
1051	Geary	20061	18
1052	Geauga	39055	38
1053	Gem	16045	14
1054	Genesee	26049	24
1055	Genesee	36037	34
1056	Geneva	1061	0
1057	Gentry	29075	27
1058	George	28039	26
1059	Georgetown	45043	44
1060	Gibson	47053	46
1061	Gibson	18051	16
1062	Gila	4007	3
1063	Gilchrist	12041	10
1064	Giles	51071	51
1065	Giles	47055	46
1066	Gillespie	48171	47
1067	Gilliam	41021	40
1068	Gilmer	13123	11
1069	Gilmer	54021	53
1070	Gilpin	8047	6
1071	Glacier	30035	28
1072	Glades	12043	10
1073	Gladwin	26051	24
1074	Glascock	13125	11
1075	Glasscock	48173	47
1076	Glenn	6021	5
1077	Gloucester	34015	32
1078	Gloucester	51073	51
1079	Glynn	13127	11
1080	Gogebic	26053	24
1081	Golden Valley	30037	28
1082	Golden Valley	38033	36
1083	Goliad	48175	47
1084	Gonzales	48177	47
1085	Goochland	51075	51
1086	Goodhue	27049	25
1087	Gooding	16047	14
1088	Gordon	13129	11
1089	Goshen	56015	55
1090	Gosper	31073	29
1091	Gove	20063	18
1092	Grady	40051	39
1093	Grady	13131	11
1094	Grafton	33009	31
1095	Graham	20065	18
1096	Graham	4009	3
1097	Graham	37075	35
1098	Grainger	47057	46
1099	Grand	49019	48
1100	Grand	8049	6
1101	Grand Forks	38035	36
1102	Grand Isle	50013	49
1103	Grand Traverse	26055	24
1104	Granite	30039	28
1105	Grant	46051	45
1106	Grant	54023	53
1107	Grant	20067	18
1108	Grant	35017	33
1109	Grant	5053	4
1110	Grant	18053	16
1111	Grant	22043	20
1112	Grant	21081	19
1113	Grant	38037	36
1114	Grant	41023	40
1115	Grant	53025	52
1116	Grant	40053	39
1117	Grant	31075	29
1118	Grant	27051	25
1119	Grant	55043	54
1120	Granville	37077	35
1121	Gratiot	26057	24
1122	Graves	21083	19
1123	Gray	48179	47
1124	Gray	20069	18
1125	Grays Harbor	53027	52
1126	Grayson	48181	47
1127	Grayson	51077	51
1128	Grayson	21085	19
1129	Greeley	20071	18
1130	Greeley	31077	29
1131	Green	21087	19
1132	Green	55045	54
1133	Green Lake	55047	54
1134	Greenbrier	54025	53
1135	Greene	19073	17
1136	Greene	37079	35
1137	Greene	42059	41
1138	Greene	13133	11
1139	Greene	51079	51
1140	Greene	29077	27
1141	Greene	39057	38
1142	Greene	47059	46
1143	Greene	18055	16
1144	Greene	36039	34
1145	Greene	28041	26
1146	Greene	17061	15
1147	Greene	1063	0
1148	Greene	5055	4
1149	Greenlee	4011	3
1150	Greensville	51081	51
1151	Greenup	21089	19
1152	Greenville	45045	44
1153	Greenwood	20073	18
1154	Greenwood	45047	44
1155	Greer	40055	39
1156	Gregg	48183	47
1157	Gregory	46053	45
1158	Grenada	28043	26
1159	Griggs	38039	36
1160	Grimes	48185	47
1161	Grundy	47061	46
1162	Grundy	17063	15
1163	Grundy	29079	27
1164	Grundy	19075	17
1165	Guadalupe	35019	33
1166	Guadalupe	48187	47
1167	Guanica	72055	42
1168	Guayama	72057	42
1169	Guayanilla	72059	42
1170	Guaynabo	72061	42
1171	Guernsey	39059	38
1172	Guilford	37081	35
1173	Gulf	12045	10
1174	Gunnison	8051	6
1175	Gurabo	72063	42
1176	Guthrie	19077	17
1177	Gwinnett	13135	11
1178	Haakon	46055	45
1179	Habersham	13137	11
1180	Haines Borough	2100	1
1181	Hale	48189	47
1182	Hale	1065	0
1183	Halifax	37083	35
1184	Halifax	51083	51
1185	Hall	31079	29
1186	Hall	13139	11
1187	Hall	48191	47
1188	Hamblen	47063	46
1189	Hamilton	17065	15
1190	Hamilton	19079	17
1191	Hamilton	39061	38
1192	Hamilton	48193	47
1193	Hamilton	12047	10
1194	Hamilton	47065	46
1195	Hamilton	31081	29
1196	Hamilton	18057	16
1197	Hamilton	36041	34
1198	Hamilton	20075	18
1199	Hamlin	46057	45
1200	Hampden	25013	23
1201	Hampshire	25015	23
1202	Hampshire	54027	53
1203	Hampton	45049	44
1204	Hampton city	51650	51
1205	Hancock	23009	21
1206	Hancock	28045	26
1207	Hancock	47067	46
1208	Hancock	21091	19
1209	Hancock	39063	38
1210	Hancock	17067	15
1211	Hancock	13141	11
1212	Hancock	54029	53
1213	Hancock	19081	17
1214	Hancock	18059	16
1215	Hand	46059	45
1216	Hanover	51085	51
1217	Hansford	48195	47
1218	Hanson	46061	45
1219	Haralson	13143	11
1220	Hardee	12049	10
1221	Hardeman	47069	46
1222	Hardeman	48197	47
1223	Hardin	21093	19
1224	Hardin	47071	46
1225	Hardin	19083	17
1226	Hardin	17069	15
1227	Hardin	39065	38
1228	Hardin	48199	47
1229	Harding	46063	45
1230	Harding	35021	33
1231	Hardy	54031	53
1232	Harford	24025	22
1233	Harlan	31083	29
1234	Harlan	21095	19
1235	Harmon	40057	39
1236	Harnett	37085	35
1237	Harney	41025	40
1238	Harper	20077	18
1239	Harper	40059	39
1240	Harris	13145	11
1241	Harris	48201	47
1242	Harrison	54033	53
1243	Harrison	19085	17
1244	Harrison	21097	19
1245	Harrison	48203	47
1246	Harrison	39067	38
1247	Harrison	28047	26
1248	Harrison	29081	27
1249	Harrison	18061	16
1250	Harrisonburg city	51660	51
1251	Hart	13147	11
1252	Hart	21099	19
1253	Hartford	9003	7
1254	Hartley	48205	47
1255	Harvey	20079	18
1256	Haskell	48207	47
1257	Haskell	20081	18
1258	Haskell	40061	39
1259	Hatillo	72065	42
1260	Hawaii	15001	13
1261	Hawkins	47073	46
1262	Hayes	31085	29
1263	Hays	48209	47
1264	Haywood	47075	46
1265	Haywood	37087	35
1266	Heard	13149	11
1267	Hemphill	48211	47
1268	Hempstead	5057	4
1269	Henderson	47077	46
1270	Henderson	21101	19
1271	Henderson	48213	47
1272	Henderson	37089	35
1273	Henderson	17071	15
1274	Hendricks	18063	16
1275	Hendry	12051	10
1276	Hennepin	27053	25
1277	Henrico	51087	51
1278	Henry	47079	46
1279	Henry	21103	19
1280	Henry	29083	27
1281	Henry	13151	11
1282	Henry	19087	17
1283	Henry	39069	38
1284	Henry	51089	51
1285	Henry	1067	0
1286	Henry	18065	16
1287	Henry	17073	15
1288	Herkimer	36043	34
1289	Hernando	12053	10
1290	Hertford	37091	35
1291	Hettinger	38041	36
1292	Hickman	47081	46
1293	Hickman	21105	19
1294	Hickory	29085	27
1295	Hidalgo	48215	47
1296	Hidalgo	35023	33
1297	Highland	51091	51
1298	Highland	39071	38
1299	Highlands	12055	10
1300	Hill	30041	28
1301	Hill	48217	47
1302	Hillsborough	12057	10
1303	Hillsborough	33011	31
1304	Hillsdale	26059	24
1305	Hinds	28049	26
1306	Hinsdale	8053	6
1307	Hitchcock	31087	29
1308	Hocking	39073	38
1309	Hockley	48219	47
1310	Hodgeman	20083	18
1311	Hoke	37093	35
1312	Holmes	39075	38
1313	Holmes	28051	26
1314	Holmes	12059	10
1315	Holt	31089	29
1316	Holt	29087	27
1317	Honolulu	15003	13
1318	Hood	48221	47
1319	Hood River	41027	40
1320	Hooker	31091	29
1321	Hopewell city	51670	51
1322	Hopkins	48223	47
1323	Hopkins	21107	19
1324	Hormigueros	72067	42
1325	Horry	45051	44
1326	Hot Spring	5059	4
1327	Hot Springs	56017	55
1328	Houghton	26061	24
1329	Houston	1069	0
1330	Houston	47083	46
1331	Houston	27055	25
1332	Houston	48225	47
1333	Houston	13153	11
1334	Howard	48227	47
1335	Howard	18067	16
1336	Howard	29089	27
1337	Howard	31093	29
1338	Howard	19089	17
1339	Howard	24027	22
1340	Howard	5061	4
1341	Howell	29091	27
1342	Hubbard	27057	25
1343	Hudson	34017	32
1344	Hudspeth	48229	47
1345	Huerfano	8055	6
1346	Hughes	40063	39
1347	Hughes	46065	45
1348	Humacao	72069	42
1349	Humboldt	6023	5
1350	Humboldt	19091	17
1351	Humboldt	32013	30
1352	Humphreys	28053	26
1353	Humphreys	47085	46
1354	Hunt	48231	47
1355	Hunterdon	34019	32
1356	Huntingdon	42061	41
1357	Huntington	18069	16
1358	Huron	26063	24
1359	Huron	39077	38
1360	Hutchinson	46067	45
1361	Hutchinson	48233	47
1362	Hyde	37095	35
1363	Hyde	46069	45
1364	Iberia	22045	20
1365	Iberville	22047	20
1366	Ida	19093	17
1367	Idaho	16049	14
1368	Imperial	6025	5
1369	Independence	5063	4
1370	Indian River	12061	10
1371	Indiana	42063	41
1372	Ingham	26065	24
1373	Inyo	6027	5
1374	Ionia	26067	24
1375	Iosco	26069	24
1376	Iowa	19095	17
1377	Iowa	55049	54
1378	Iredell	37097	35
1379	Irion	48235	47
1380	Iron	26071	24
1381	Iron	55051	54
1382	Iron	49021	48
1383	Iron	29093	27
1384	Iroquois	17075	15
1385	Irwin	13155	11
1386	Isabela	72071	42
1387	Isabella	26073	24
1388	Isanti	27059	25
1389	Island	53029	52
1390	Isle of Wight	51093	51
1391	Issaquena	28055	26
1392	Itasca	27061	25
1393	Itawamba	28057	26
1394	Izard	5065	4
1395	Jack	48237	47
1396	Jackson	22049	20
1397	Jackson	41029	40
1398	Jackson	47087	46
1399	Jackson	19097	17
1400	Jackson	20085	18
1401	Jackson	8057	6
1402	Jackson	37099	35
1403	Jackson	5067	4
1404	Jackson	12063	10
1405	Jackson	21109	19
1406	Jackson	39079	38
1407	Jackson	40065	39
1408	Jackson	27063	25
1409	Jackson	46071	45
1410	Jackson	26075	24
1411	Jackson	48239	47
1412	Jackson	13157	11
1413	Jackson	55053	54
1414	Jackson	54035	53
1415	Jackson	1071	0
1416	Jackson	18071	16
1417	Jackson	28059	26
1418	Jackson	29095	27
1419	Jackson	17077	15
1420	James City	51095	51
1421	Jasper	13159	11
1422	Jasper	29097	27
1423	Jasper	19099	17
1424	Jasper	28061	26
1425	Jasper	45053	44
1426	Jasper	18073	16
1427	Jasper	48241	47
1428	Jasper	17079	15
1429	Jay	18075	16
1430	Jayuya	72073	42
1431	Jeff Davis	13161	11
1432	Jeff Davis	48243	47
1433	Jefferson	17081	15
1434	Jefferson	20087	18
1435	Jefferson	30043	28
1436	Jefferson	8059	6
1437	Jefferson	18077	16
1438	Jefferson	1073	0
1439	Jefferson	42065	41
1440	Jefferson	29099	27
1441	Jefferson	28063	26
1442	Jefferson	40067	39
1443	Jefferson	41031	40
1444	Jefferson	48245	47
1445	Jefferson	36045	34
1446	Jefferson	21111	19
1447	Jefferson	31095	29
1448	Jefferson	47089	46
1449	Jefferson	39081	38
1450	Jefferson	12065	10
1451	Jefferson	13163	11
1452	Jefferson	54037	53
1453	Jefferson	16051	14
1454	Jefferson	53031	52
1455	Jefferson	55055	54
1456	Jefferson	22051	20
1457	Jefferson	5069	4
1458	Jefferson	19101	17
1459	Jefferson Davis	28065	26
1460	Jefferson Davis	22053	20
1461	Jenkins	13165	11
1462	Jennings	18079	16
1463	Jerauld	46073	45
1464	Jerome	16053	14
1465	Jersey	17083	15
1466	Jessamine	21113	19
1467	Jewell	20089	18
1468	Jim Hogg	48247	47
1469	Jim Wells	48249	47
1470	Jo Daviess	17085	15
1471	Johnson	48251	47
1472	Johnson	56019	55
1473	Johnson	20091	18
1474	Johnson	19103	17
1475	Johnson	18081	16
1476	Johnson	17087	15
1477	Johnson	21115	19
1478	Johnson	29101	27
1479	Johnson	13167	11
1480	Johnson	31097	29
1481	Johnson	5071	4
1482	Johnson	47091	46
1483	Johnston	40069	39
1484	Johnston	37101	35
1485	Jones	46075	45
1486	Jones	13169	11
1487	Jones	37103	35
1488	Jones	48253	47
1489	Jones	19105	17
1490	Jones	28067	26
1491	Joplin	\N	27
1492	Josephine	41033	40
1493	Juab	49023	48
1494	Juana Diaz	72075	42
1495	Judith Basin	30045	28
1496	Juncos	72077	42
1497	Juneau	55057	54
1498	Juneau City and Borough	2110	1
1499	Juniata	42067	41
1500	Kalamazoo	26077	24
1501	Kalawao	15005	13
1502	Kalkaska	26079	24
1503	Kanabec	27065	25
1504	Kanawha	54039	53
1505	Kandiyohi	27067	25
1506	Kane	49025	48
1507	Kane	17089	15
1508	Kankakee	17091	15
1509	Kansas City	\N	27
1510	Karnes	48255	47
1511	Kauai	15007	13
1512	Kaufman	48257	47
1513	Kay	40071	39
1514	Kearney	31099	29
1515	Kearny	20093	18
1516	Keith	31101	29
1517	Kemper	28069	26
1518	Kenai Peninsula Borough	2122	1
1519	Kendall	48259	47
1520	Kendall	17093	15
1521	Kenedy	48261	47
1522	Kennebec	23011	21
1523	Kenosha	55059	54
1524	Kent	24029	22
1525	Kent	44003	43
1526	Kent	26081	24
1527	Kent	48263	47
1528	Kent	10001	8
1529	Kenton	21117	19
1530	Keokuk	19107	17
1531	Kern	6029	5
1532	Kerr	48265	47
1533	Kershaw	45055	44
1534	Ketchikan Gateway Borough	2130	1
1535	Kewaunee	55061	54
1536	Keweenaw	26083	24
1537	Keya Paha	31103	29
1538	Kidder	38043	36
1539	Kimball	31105	29
1540	Kimble	48267	47
1541	King	48269	47
1542	King	53033	52
1543	King George	51099	51
1544	King William	51101	51
1545	King and Queen	51097	51
1546	Kingfisher	40073	39
1547	Kingman	20095	18
1548	Kings	6031	5
1549	Kingsbury	46077	45
1550	Kinney	48271	47
1551	Kiowa	8061	6
1552	Kiowa	40075	39
1553	Kiowa	20097	18
1554	Kit Carson	8063	6
1555	Kitsap	53035	52
1556	Kittitas	53037	52
1557	Kittson	27069	25
1558	Klamath	41035	40
1559	Kleberg	48273	47
1560	Klickitat	53039	52
1561	Knott	21119	19
1562	Knox	48275	47
1563	Knox	31107	29
1564	Knox	21121	19
1565	Knox	18083	16
1566	Knox	39083	38
1567	Knox	17095	15
1568	Knox	47093	46
1569	Knox	23013	21
1570	Knox	29103	27
1571	Kodiak Island Borough	2150	1
1572	Koochiching	27071	25
1573	Kootenai	16055	14
1574	Kosciusko	18085	16
1575	Kossuth	19109	17
1576	Kusilvak Census Area	2158	1
1577	La Crosse	55063	54
1578	La Paz	4012	3
1579	La Plata	8067	6
1580	La Salle	48283	47
1581	LaGrange	18087	16
1582	LaMoure	38045	36
1583	LaPorte	18091	16
1584	LaSalle	22059	20
1585	LaSalle	17099	15
1586	Labette	20099	18
1587	Lac qui Parle	27073	25
1588	Lackawanna	42069	41
1589	Laclede	29105	27
1590	Lafayette	12067	10
1591	Lafayette	55065	54
1592	Lafayette	28071	26
1593	Lafayette	5073	4
1594	Lafayette	29107	27
1595	Lafayette	22055	20
1596	Lafourche	22057	20
1597	Lajas	72079	42
1598	Lake	18089	16
1599	Lake	12069	10
1600	Lake	6033	5
1601	Lake	41037	40
1602	Lake	46079	45
1603	Lake	26085	24
1604	Lake	39085	38
1605	Lake	8065	6
1606	Lake	27075	25
1607	Lake	30047	28
1608	Lake	17097	15
1609	Lake	47095	46
1610	Lake of the Woods	27077	25
1611	Lamar	28073	26
1612	Lamar	1075	0
1613	Lamar	48277	47
1614	Lamar	13171	11
1615	Lamb	48279	47
1616	Lamoille	50015	49
1617	Lampasas	48281	47
1618	Lancaster	45057	44
1619	Lancaster	42071	41
1620	Lancaster	31109	29
1621	Lancaster	51103	51
1622	Lander	32015	30
1623	Lane	20101	18
1624	Lane	41039	40
1625	Langlade	55067	54
1626	Lanier	13173	11
1627	Lapeer	26087	24
1628	Laramie	56021	55
1629	Lares	72081	42
1630	Larimer	8069	6
1631	Larue	21123	19
1632	Las Animas	8071	6
1633	Las Marias	72083	42
1634	Las Piedras	72085	42
1635	Lassen	6035	5
1636	Latah	16057	14
1637	Latimer	40077	39
1638	Lauderdale	1077	0
1639	Lauderdale	47097	46
1640	Lauderdale	28075	26
1641	Laurel	21125	19
1642	Laurens	13175	11
1643	Laurens	45059	44
1644	Lavaca	48285	47
1645	Lawrence	29109	27
1646	Lawrence	21127	19
1647	Lawrence	1079	0
1648	Lawrence	5075	4
1649	Lawrence	18093	16
1650	Lawrence	39087	38
1651	Lawrence	28077	26
1652	Lawrence	46081	45
1653	Lawrence	42073	41
1654	Lawrence	17101	15
1655	Lawrence	47099	46
1656	Le Flore	40079	39
1657	Le Sueur	27079	25
1658	Lea	35025	33
1659	Leake	28079	26
1660	Leavenworth	20103	18
1661	Lebanon	42075	41
1662	Lee	13177	11
1663	Lee	28081	26
1664	Lee	45061	44
1665	Lee	5077	4
1666	Lee	17103	15
1667	Lee	21129	19
1668	Lee	37105	35
1669	Lee	1081	0
1670	Lee	48287	47
1671	Lee	12071	10
1672	Lee	19111	17
1673	Lee	51105	51
1674	Leelanau	26089	24
1675	Leflore	28083	26
1676	Lehigh	42077	41
1677	Lemhi	16059	14
1678	Lenawee	26091	24
1679	Lenoir	37107	35
1680	Leon	48289	47
1681	Leon	12073	10
1682	Leslie	21131	19
1683	Letcher	21133	19
1684	Levy	12075	10
1685	Lewis	47101	46
1686	Lewis	53041	52
1687	Lewis	54041	53
1688	Lewis	16061	14
1689	Lewis	36049	34
1690	Lewis	29111	27
1691	Lewis	21135	19
1692	Lewis and Clark	30049	28
1693	Lexington	45063	44
1694	Lexington city	51678	51
1695	Liberty	13179	11
1696	Liberty	12077	10
1697	Liberty	30051	28
1698	Liberty	48291	47
1699	Licking	39089	38
1700	Limestone	48293	47
1701	Limestone	1083	0
1702	Lincoln	29113	27
1703	Lincoln	47103	46
1704	Lincoln	37109	35
1705	Lincoln	16063	14
1706	Lincoln	54043	53
1707	Lincoln	8073	6
1708	Lincoln	31111	29
1709	Lincoln	27081	25
1710	Lincoln	28085	26
1711	Lincoln	23015	21
1712	Lincoln	22061	20
1713	Lincoln	21137	19
1714	Lincoln	5079	4
1715	Lincoln	13181	11
1716	Lincoln	40081	39
1717	Lincoln	56023	55
1718	Lincoln	55069	54
1719	Lincoln	35027	33
1720	Lincoln	32017	30
1721	Lincoln	41041	40
1722	Lincoln	53043	52
1723	Lincoln	30053	28
1724	Lincoln	46083	45
1725	Lincoln	20105	18
1726	Linn	29115	27
1727	Linn	41043	40
1728	Linn	20107	18
1729	Linn	19113	17
1730	Lipscomb	48295	47
1731	Litchfield	9005	7
1732	Little River	5081	4
1733	Live Oak	48297	47
1734	Livingston	26093	24
1735	Livingston	22063	20
1736	Livingston	29117	27
1737	Livingston	36051	34
1738	Livingston	17105	15
1739	Livingston	21139	19
1740	Llano	48299	47
1741	Logan	5083	4
1742	Logan	38047	36
1743	Logan	54045	53
1744	Logan	40083	39
1745	Logan	20109	18
1746	Logan	17107	15
1747	Logan	21141	19
1748	Logan	8075	6
1749	Logan	39091	38
1750	Logan	31113	29
1751	Loiza	72087	42
1752	Long	13183	11
1753	Lonoke	5085	4
1754	Lorain	39093	38
1755	Los Alamos	35028	33
1756	Los Angeles	6037	5
1757	Loudon	47105	46
1758	Loudoun	51107	51
1759	Louisa	19115	17
1760	Louisa	51109	51
1761	Loup	31115	29
1762	Love	40085	39
1763	Loving	48301	47
1764	Lowndes	28087	26
1765	Lowndes	13185	11
1766	Lowndes	1085	0
1767	Lubbock	48303	47
1768	Lucas	39095	38
1769	Lucas	19117	17
1770	Luce	26095	24
1771	Lumpkin	13187	11
1772	Luna	35029	33
1773	Lunenburg	51111	51
1774	Luquillo	72089	42
1775	Luzerne	42079	41
1776	Lycoming	42081	41
1777	Lyman	46085	45
1778	Lynchburg city	51680	51
1779	Lynn	48305	47
1780	Lyon	21143	19
1781	Lyon	20111	18
1782	Lyon	32019	30
1783	Lyon	19119	17
1784	Lyon	27083	25
1785	Mackinac	26097	24
1786	Macomb	26099	24
1787	Macon	47111	46
1788	Macon	1087	0
1789	Macon	13193	11
1790	Macon	17115	15
1791	Macon	29121	27
1792	Macon	37113	35
1793	Macoupin	17117	15
1794	Madera	6039	5
1795	Madison	47113	46
1796	Madison	39097	38
1797	Madison	5087	4
1798	Madison	48313	47
1799	Madison	37115	35
1800	Madison	51113	51
1801	Madison	16065	14
1802	Madison	21151	19
1803	Madison	36053	34
1804	Madison	30057	28
1805	Madison	28089	26
1806	Madison	1089	0
1807	Madison	18095	16
1808	Madison	29123	27
1809	Madison	17119	15
1810	Madison	22065	20
1811	Madison	12079	10
1812	Madison	19121	17
1813	Madison	13195	11
1814	Madison	31119	29
1815	Magoffin	21153	19
1816	Mahaska	19123	17
1817	Mahnomen	27087	25
1818	Mahoning	39099	38
1819	Major	40093	39
1820	Malheur	41045	40
1821	Manassas Park city	51685	51
1822	Manassas city	51683	51
1823	Manatee	12081	10
1824	Manati	72091	42
1825	Manistee	26101	24
1826	Manitowoc	55071	54
1827	Marathon	55073	54
1828	Marengo	1091	0
1829	Maricao	72093	42
1830	Maricopa	4013	3
1831	Maries	29125	27
1832	Marin	6041	5
1833	Marinette	55075	54
1834	Marion	48315	47
1835	Marion	54049	53
1836	Marion	19125	17
1837	Marion	28091	26
1838	Marion	17121	15
1839	Marion	47115	46
1840	Marion	5089	4
1841	Marion	18097	16
1842	Marion	45067	44
1843	Marion	1093	0
1844	Marion	41047	40
1845	Marion	39101	38
1846	Marion	13197	11
1847	Marion	20115	18
1848	Marion	29127	27
1849	Marion	12083	10
1850	Marion	21155	19
1851	Mariposa	6043	5
1852	Marlboro	45069	44
1853	Marquette	55077	54
1854	Marquette	26103	24
1855	Marshall	40095	39
1856	Marshall	17123	15
1857	Marshall	1095	0
1858	Marshall	21157	19
1859	Marshall	27089	25
1860	Marshall	19127	17
1861	Marshall	28093	26
1862	Marshall	46091	45
1863	Marshall	47117	46
1864	Marshall	20117	18
1865	Marshall	18099	16
1866	Marshall	54051	53
1867	Martin	18101	16
1868	Martin	21159	19
1869	Martin	27091	25
1870	Martin	12085	10
1871	Martin	48317	47
1872	Martin	37117	35
1873	Martinsville city	51690	51
1874	Mason	26105	24
1875	Mason	17125	15
1876	Mason	54053	53
1877	Mason	48319	47
1878	Mason	53045	52
1879	Mason	21161	19
1880	Massac	17127	15
1881	Matagorda	48321	47
1882	Matanuska-Susitna Borough	2170	1
1883	Mathews	51115	51
1884	Maui	15009	13
1885	Maunabo	72095	42
1886	Maury	47119	46
1887	Maverick	48323	47
1888	Mayaguez	72097	42
1889	Mayes	40097	39
1890	McClain	40087	39
1891	McCone	30055	28
1892	McCook	46087	45
1893	McCormick	45065	44
1894	McCracken	21145	19
1895	McCreary	21147	19
1896	McCulloch	48307	47
1897	McCurtain	40089	39
1898	McDonald	29119	27
1899	McDonough	17109	15
1900	McDowell	37111	35
1901	McDowell	54047	53
1902	McDuffie	13189	11
1903	McHenry	38049	36
1904	McHenry	17111	15
1905	McIntosh	38051	36
1906	McIntosh	40091	39
1907	McIntosh	13191	11
1908	McKean	42083	41
1909	McKenzie	38053	36
1910	McKinley	35031	33
1911	McLean	17113	15
1912	McLean	21149	19
1913	McLean	38055	36
1914	McLennan	48309	47
1915	McLeod	27085	25
1916	McMinn	47107	46
1917	McMullen	48311	47
1918	McNairy	47109	46
1919	McPherson	31117	29
1920	McPherson	20113	18
1921	McPherson	46089	45
1922	Meade	20119	18
1923	Meade	21163	19
1924	Meade	46093	45
1925	Meagher	30059	28
1926	Mecklenburg	37119	35
1927	Mecklenburg	51117	51
1928	Mecosta	26107	24
1929	Medina	48325	47
1930	Medina	39103	38
1931	Meeker	27093	25
1932	Meigs	39105	38
1933	Meigs	47121	46
1934	Mellette	46095	45
1935	Menard	17129	15
1936	Menard	48327	47
1937	Mendocino	6045	5
1938	Menifee	21165	19
1939	Menominee	55078	54
1940	Menominee	26109	24
1941	Merced	6047	5
1942	Mercer	34021	32
1943	Mercer	42085	41
1944	Mercer	39107	38
1945	Mercer	21167	19
1946	Mercer	38057	36
1947	Mercer	54055	53
1948	Mercer	29129	27
1949	Mercer	17131	15
1950	Meriwether	13199	11
1951	Merrick	31121	29
1952	Merrimack	33013	31
1953	Mesa	8077	6
1954	Metcalfe	21169	19
1955	Miami	20121	18
1956	Miami	18103	16
1957	Miami	39109	38
1958	Miami-Dade	12086	10
1959	Middlesex	51119	51
1960	Middlesex	25017	23
1961	Middlesex	34023	32
1962	Middlesex	9007	7
1963	Midland	48329	47
1964	Midland	26111	24
1965	Mifflin	42087	41
1966	Milam	48331	47
1967	Millard	49027	48
1968	Mille Lacs	27095	25
1969	Miller	13201	11
1970	Miller	29131	27
1971	Miller	5091	4
1972	Mills	19129	17
1973	Mills	48333	47
1974	Milwaukee	55079	54
1975	Miner	46097	45
1976	Mineral	30061	28
1977	Mineral	54057	53
1978	Mineral	32021	30
1979	Mineral	8079	6
1980	Mingo	54059	53
1981	Minidoka	16067	14
1982	Minnehaha	46099	45
1983	Missaukee	26113	24
1984	Mississippi	5093	4
1985	Mississippi	29133	27
1986	Missoula	30063	28
1987	Mitchell	13205	11
1988	Mitchell	19131	17
1989	Mitchell	48335	47
1990	Mitchell	37121	35
1991	Mitchell	20123	18
1992	Mobile	1097	0
1993	Moca	72099	42
1994	Modoc	6049	5
1995	Moffat	8081	6
1996	Mohave	4015	3
1997	Moniteau	29135	27
1998	Monmouth	34025	32
1999	Mono	6051	5
2000	Monona	19133	17
2001	Monongalia	54061	53
2002	Monroe	21171	19
2003	Monroe	18105	16
2004	Monroe	29137	27
2005	Monroe	28095	26
2006	Monroe	5095	4
2007	Monroe	1099	0
2008	Monroe	17133	15
2009	Monroe	26115	24
2010	Monroe	12087	10
2011	Monroe	55081	54
2012	Monroe	36055	34
2013	Monroe	42089	41
2014	Monroe	47123	46
2015	Monroe	13207	11
2016	Monroe	19135	17
2017	Monroe	54063	53
2018	Monroe	39111	38
2019	Montague	48337	47
2020	Montcalm	26117	24
2021	Monterey	6053	5
2022	Montezuma	8083	6
2023	Montgomery	51121	51
2024	Montgomery	1101	0
2025	Montgomery	17135	15
2026	Montgomery	29139	27
2027	Montgomery	21173	19
2028	Montgomery	48339	47
2029	Montgomery	5097	4
2030	Montgomery	36057	34
2031	Montgomery	28097	26
2032	Montgomery	47125	46
2033	Montgomery	13209	11
2034	Montgomery	19137	17
2035	Montgomery	37123	35
2036	Montgomery	39113	38
2037	Montgomery	20125	18
2038	Montgomery	24031	22
2039	Montgomery	18107	16
2040	Montgomery	42091	41
2041	Montmorency	26119	24
2042	Montour	42093	41
2043	Montrose	8085	6
2044	Moody	46101	45
2045	Moore	48341	47
2046	Moore	37125	35
2047	Moore	47127	46
2048	Mora	35033	33
2049	Morehouse	22067	20
2050	Morgan	18109	16
2051	Morgan	54065	53
2052	Morgan	17137	15
2053	Morgan	13211	11
2054	Morgan	47129	46
2055	Morgan	21175	19
2056	Morgan	49029	48
2057	Morgan	1103	0
2058	Morgan	29141	27
2059	Morgan	39115	38
2060	Morgan	8087	6
2061	Morovis	72101	42
2062	Morrill	31123	29
2063	Morris	34027	32
2064	Morris	20127	18
2065	Morris	48343	47
2066	Morrison	27097	25
2067	Morrow	41049	40
2068	Morrow	39117	38
2069	Morton	38059	36
2070	Morton	20129	18
2071	Motley	48345	47
2072	Moultrie	17139	15
2073	Mountrail	38061	36
2074	Mower	27099	25
2075	Muhlenberg	21177	19
2076	Multnomah	41051	40
2077	Murray	27101	25
2078	Murray	40099	39
2079	Murray	13213	11
2080	Muscatine	19139	17
2081	Muscogee	13215	11
2082	Muskegon	26121	24
2083	Muskingum	39119	38
2084	Muskogee	40101	39
2085	Musselshell	30065	28
2086	Nacogdoches	48347	47
2087	Naguabo	72103	42
2088	Nance	31125	29
2089	Nantucket	25019	23
2090	Napa	6055	5
2091	Naranjito	72105	42
2092	Nash	37127	35
2093	Nassau	36059	34
2094	Nassau	12089	10
2095	Natchitoches	22069	20
2096	Natrona	56025	55
2097	Navajo	4017	3
2098	Navarro	48349	47
2099	Nelson	51125	51
2100	Nelson	21179	19
2101	Nelson	38063	36
2102	Nemaha	20131	18
2103	Nemaha	31127	29
2104	Neosho	20133	18
2105	Neshoba	28099	26
2106	Ness	20135	18
2107	Nevada	6057	5
2108	Nevada	5099	4
2109	New Castle	10003	8
2110	New Hanover	37129	35
2111	New Haven	9009	7
2112	New Kent	51127	51
2113	New London	9011	7
2114	New Madrid	29143	27
2115	New York City	\N	34
2116	Newaygo	26123	24
2117	Newberry	45071	44
2118	Newport	44005	43
2119	Newport News city	51700	51
2120	Newton	48351	47
2121	Newton	18111	16
2122	Newton	5101	4
2123	Newton	29145	27
2124	Newton	28101	26
2125	Newton	13217	11
2126	Nez Perce	16069	14
2127	Niagara	36063	34
2128	Nicholas	54067	53
2129	Nicholas	21181	19
2130	Nicollet	27103	25
2131	Niobrara	56027	55
2132	Noble	18113	16
2133	Noble	39121	38
2134	Noble	40103	39
2135	Nobles	27105	25
2136	Nodaway	29147	27
2137	Nolan	48353	47
2138	Nome Census Area	2180	1
2139	Norfolk	25021	23
2140	Norfolk city	51710	51
2141	Norman	27107	25
2142	North Slope Borough	2185	1
2143	Northampton	42095	41
2144	Northampton	51131	51
2145	Northampton	37131	35
2146	Northumberland	51133	51
2147	Northumberland	42097	41
2148	Northwest Arctic Borough	2188	1
2149	Norton	20137	18
2150	Norton city	51720	51
2151	Nottoway	51135	51
2152	Nowata	40105	39
2153	Noxubee	28103	26
2154	Nuckolls	31129	29
2155	Nueces	48355	47
2156	Nye	32023	30
2157	O'Brien	19141	17
2158	Oakland	26125	24
2159	Obion	47131	46
2160	Ocean	34029	32
2161	Oceana	26127	24
2162	Ochiltree	48357	47
2163	Oconee	45073	44
2164	Oconee	13219	11
2165	Oconto	55083	54
2166	Ogemaw	26129	24
2167	Oglala Lakota	46102	45
2168	Ogle	17141	15
2169	Oglethorpe	13221	11
2170	Ohio	54069	53
2171	Ohio	18115	16
2172	Ohio	21183	19
2173	Okaloosa	12091	10
2174	Okanogan	53047	52
2175	Okeechobee	12093	10
2176	Okfuskee	40107	39
2177	Oklahoma	40109	39
2178	Okmulgee	40111	39
2179	Oktibbeha	28105	26
2180	Oldham	48359	47
2181	Oldham	21185	19
2182	Oliver	38065	36
2183	Olmsted	27109	25
2184	Oneida	55085	54
2185	Oneida	16071	14
2186	Oneida	36065	34
2187	Onondaga	36067	34
2188	Onslow	37133	35
2189	Ontario	36069	34
2190	Ontonagon	26131	24
2191	Orange	36071	34
2192	Orange	6059	5
2193	Orange	37135	35
2194	Orange	51137	51
2195	Orange	12095	10
2196	Orange	50017	49
2197	Orange	48361	47
2198	Orange	18117	16
2199	Orangeburg	45075	44
2200	Oregon	29149	27
2201	Orleans	36073	34
2202	Orleans	50019	49
2203	Orleans	22071	20
2204	Orocovis	72107	42
2205	Osage	40113	39
2206	Osage	29151	27
2207	Osage	20139	18
2208	Osborne	20141	18
2209	Osceola	19143	17
2210	Osceola	26133	24
2211	Osceola	12097	10
2212	Oscoda	26135	24
2213	Oswego	36075	34
2214	Otero	8089	6
2215	Otero	35035	33
2216	Otoe	31131	29
2217	Otsego	36077	34
2218	Otsego	26137	24
2219	Ottawa	39123	38
2220	Ottawa	20143	18
2221	Ottawa	26139	24
2222	Ottawa	40115	39
2223	Otter Tail	27111	25
2224	Ouachita	5103	4
2225	Ouachita	22073	20
2226	Ouray	8091	6
2227	Outagamie	55087	54
2228	Overton	47133	46
2229	Owen	21187	19
2230	Owen	18119	16
2231	Owsley	21189	19
2232	Owyhee	16073	14
2233	Oxford	23017	21
2234	Ozark	29153	27
2235	Ozaukee	55089	54
2236	Pacific	53049	52
2237	Page	19145	17
2238	Page	51139	51
2239	Palm Beach	12099	10
2240	Palo Alto	19147	17
2241	Palo Pinto	48363	47
2242	Pamlico	37137	35
2243	Panola	28107	26
2244	Panola	48365	47
2245	Park	56029	55
2246	Park	30067	28
2247	Park	8093	6
2248	Parke	18121	16
2249	Parker	48367	47
2250	Parmer	48369	47
2251	Pasco	12101	10
2252	Pasquotank	37139	35
2253	Passaic	34031	32
2254	Patillas	72109	42
2255	Patrick	51141	51
2256	Paulding	13223	11
2257	Paulding	39125	38
2258	Pawnee	20145	18
2259	Pawnee	31133	29
2260	Pawnee	40117	39
2261	Payette	16075	14
2262	Payne	40119	39
2263	Peach	13225	11
2264	Pearl River	28109	26
2265	Pecos	48371	47
2266	Pembina	38067	36
2267	Pemiscot	29155	27
2268	Pend Oreille	53051	52
2269	Pender	37141	35
2270	Pendleton	21191	19
2271	Pendleton	54071	53
2272	Pennington	27113	25
2273	Pennington	46103	45
2274	Penobscot	23019	21
2275	Penuelas	72111	42
2276	Peoria	17143	15
2277	Pepin	55091	54
2278	Perkins	46105	45
2279	Perkins	31135	29
2280	Perquimans	37143	35
2281	Perry	17145	15
2282	Perry	28111	26
2283	Perry	39127	38
2284	Perry	5105	4
2285	Perry	47135	46
2286	Perry	18123	16
2287	Perry	29157	27
2288	Perry	21193	19
2289	Perry	42099	41
2290	Perry	1105	0
2291	Pershing	32027	30
2292	Person	37145	35
2293	Petersburg Borough	2195	1
2294	Petersburg city	51730	51
2295	Petroleum	30069	28
2296	Pettis	29159	27
2297	Phelps	29161	27
2298	Phelps	31137	29
2299	Philadelphia	42101	41
2300	Phillips	5107	4
2301	Phillips	20147	18
2302	Phillips	8095	6
2303	Phillips	30071	28
2304	Piatt	17147	15
2305	Pickaway	39129	38
2306	Pickens	1107	0
2307	Pickens	45077	44
2308	Pickens	13227	11
2309	Pickett	47137	46
2310	Pierce	55093	54
2311	Pierce	13229	11
2312	Pierce	31139	29
2313	Pierce	38069	36
2314	Pierce	53053	52
2315	Pike	29163	27
2316	Pike	18125	16
2317	Pike	1109	0
2318	Pike	17149	15
2319	Pike	28113	26
2320	Pike	21195	19
2321	Pike	39131	38
2322	Pike	5109	4
2323	Pike	13231	11
2324	Pike	42103	41
2325	Pima	4019	3
2326	Pinal	4021	3
2327	Pine	27115	25
2328	Pinellas	12103	10
2329	Pipestone	27117	25
2330	Piscataquis	23021	21
2331	Pitkin	8097	6
2332	Pitt	37147	35
2333	Pittsburg	40121	39
2334	Pittsylvania	51143	51
2335	Piute	49031	48
2336	Placer	6061	5
2337	Plaquemines	22075	20
2338	Platte	56031	55
2339	Platte	31141	29
2340	Platte	29165	27
2341	Pleasants	54073	53
2342	Plumas	6063	5
2343	Plymouth	25023	23
2344	Plymouth	19149	17
2345	Pocahontas	54075	53
2346	Pocahontas	19151	17
2347	Poinsett	5111	4
2348	Pointe Coupee	22077	20
2349	Polk	37149	35
2350	Polk	29167	27
2351	Polk	27119	25
2352	Polk	12105	10
2353	Polk	13233	11
2354	Polk	48373	47
2355	Polk	31143	29
2356	Polk	41053	40
2357	Polk	19153	17
2358	Polk	47139	46
2359	Polk	55095	54
2360	Polk	5113	4
2361	Ponce	72113	42
2362	Pondera	30073	28
2363	Pontotoc	28115	26
2364	Pontotoc	40123	39
2365	Pope	27121	25
2366	Pope	17151	15
2367	Pope	5115	4
2368	Poquoson city	51735	51
2369	Portage	55097	54
2370	Portage	39133	38
2371	Porter	18127	16
2372	Portsmouth city	51740	51
2373	Posey	18129	16
2374	Pottawatomie	20149	18
2375	Pottawatomie	40125	39
2376	Pottawattamie	19155	17
2377	Potter	48375	47
2378	Potter	42105	41
2379	Potter	46107	45
2380	Powder River	30075	28
2381	Powell	30077	28
2382	Powell	21197	19
2383	Power	16077	14
2384	Poweshiek	19157	17
2385	Powhatan	51145	51
2386	Prairie	5117	4
2387	Prairie	30079	28
2388	Pratt	20151	18
2389	Preble	39135	38
2390	Prentiss	28117	26
2391	Presidio	48377	47
2392	Presque Isle	26141	24
2393	Preston	54077	53
2394	Price	55099	54
2395	Prince Edward	51147	51
2396	Prince George	51149	51
2397	Prince George's	24033	22
2398	Prince William	51153	51
2399	Prince of Wales-Hyder Census Area	2198	1
2400	Providence	44007	43
2401	Prowers	8099	6
2402	Pueblo	8101	6
2403	Pulaski	29169	27
2404	Pulaski	17153	15
2405	Pulaski	21199	19
2406	Pulaski	18131	16
2407	Pulaski	51155	51
2408	Pulaski	5119	4
2409	Pulaski	13235	11
2410	Pushmataha	40127	39
2411	Putnam	18133	16
2412	Putnam	12107	10
2413	Putnam	17155	15
2414	Putnam	54079	53
2415	Putnam	39137	38
2416	Putnam	13237	11
2417	Putnam	29171	27
2418	Putnam	47141	46
2419	Putnam	36079	34
2420	Quay	35037	33
2421	Quebradillas	72115	42
2422	Queen Anne's	24035	22
2423	Quitman	13239	11
2424	Quitman	28119	26
2425	Rabun	13241	11
2426	Racine	55101	54
2427	Radford city	51750	51
2428	Rains	48379	47
2429	Raleigh	54081	53
2430	Ralls	29173	27
2431	Ramsey	38071	36
2432	Ramsey	27123	25
2433	Randall	48381	47
2434	Randolph	5121	4
2435	Randolph	13243	11
2436	Randolph	1111	0
2437	Randolph	17157	15
2438	Randolph	18135	16
2439	Randolph	54083	53
2440	Randolph	37151	35
2441	Randolph	29175	27
2442	Rankin	28121	26
2443	Ransom	38073	36
2444	Rapides	22079	20
2445	Rappahannock	51157	51
2446	Ravalli	30081	28
2447	Rawlins	20153	18
2448	Ray	29177	27
2449	Reagan	48383	47
2450	Real	48385	47
2451	Red Lake	27125	25
2452	Red River	48387	47
2453	Red River	22081	20
2454	Red Willow	31145	29
2455	Redwood	27127	25
2456	Reeves	48389	47
2457	Refugio	48391	47
2458	Reno	20155	18
2459	Rensselaer	36083	34
2460	Renville	27129	25
2461	Renville	38075	36
2462	Republic	20157	18
2463	Reynolds	29179	27
2464	Rhea	47143	46
2465	Rice	20159	18
2466	Rice	27131	25
2467	Rich	49033	48
2468	Richardson	31147	29
2469	Richland	55103	54
2470	Richland	38077	36
2471	Richland	22083	20
2472	Richland	39139	38
2473	Richland	17159	15
2474	Richland	45079	44
2475	Richland	30083	28
2476	Richmond	37153	35
2477	Richmond	13245	11
2478	Richmond	51159	51
2479	Richmond city	51760	51
2480	Riley	20161	18
2481	Rincon	72117	42
2482	Ringgold	19159	17
2483	Rio Arriba	35039	33
2484	Rio Blanco	8103	6
2485	Rio Grande	8105	6
2486	Rio Grande	72119	42
2487	Ripley	29181	27
2488	Ripley	18137	16
2489	Ritchie	54085	53
2490	Riverside	6065	5
2491	Roane	47145	46
2492	Roane	54087	53
2493	Roanoke	51161	51
2494	Roanoke city	51770	51
2495	Roberts	48393	47
2496	Roberts	46109	45
2497	Robertson	21201	19
2498	Robertson	47147	46
2499	Robertson	48395	47
2500	Robeson	37155	35
2501	Rock	31149	29
2502	Rock	27133	25
2503	Rock	55105	54
2504	Rock Island	17161	15
2505	Rockbridge	51163	51
2506	Rockcastle	21203	19
2507	Rockdale	13247	11
2508	Rockingham	33015	31
2509	Rockingham	51165	51
2510	Rockingham	37157	35
2511	Rockland	36087	34
2512	Rockwall	48397	47
2513	Roger Mills	40129	39
2514	Rogers	40131	39
2515	Rolette	38079	36
2516	Rooks	20163	18
2517	Roosevelt	35041	33
2518	Roosevelt	30085	28
2519	Roscommon	26143	24
2520	Roseau	27135	25
2521	Rosebud	30087	28
2522	Ross	39141	38
2523	Routt	8107	6
2524	Rowan	37159	35
2525	Rowan	21205	19
2526	Runnels	48399	47
2527	Rush	20165	18
2528	Rush	18139	16
2529	Rusk	55107	54
2530	Rusk	48401	47
2531	Russell	1113	0
2532	Russell	20167	18
2533	Russell	21207	19
2534	Russell	51167	51
2535	Rutherford	47149	46
2536	Rutherford	37161	35
2537	Rutland	50021	49
2538	Sabana Grande	72121	42
2539	Sabine	22085	20
2540	Sabine	48403	47
2541	Sac	19161	17
2542	Sacramento	6067	5
2543	Sagadahoc	23023	21
2544	Saginaw	26145	24
2545	Saguache	8109	6
2546	Saipan	69110	37
2547	Salem	34033	32
2548	Salem city	51775	51
2549	Salinas	72123	42
2550	Saline	29195	27
2551	Saline	5125	4
2552	Saline	17165	15
2553	Saline	20169	18
2554	Saline	31151	29
2555	Salt Lake	49035	48
2556	Saluda	45081	44
2557	Sampson	37163	35
2558	San Augustine	48405	47
2559	San Benito	6069	5
2560	San Bernardino	6071	5
2561	San Diego	6073	5
2562	San Francisco	6075	5
2563	San German	72125	42
2564	San Jacinto	48407	47
2565	San Joaquin	6077	5
2566	San Juan	35045	33
2567	San Juan	53055	52
2568	San Juan	72127	42
2569	San Juan	49037	48
2570	San Juan	8111	6
2571	San Lorenzo	72129	42
2572	San Luis Obispo	6079	5
2573	San Mateo	6081	5
2574	San Miguel	35047	33
2575	San Miguel	8113	6
2576	San Patricio	48409	47
2577	San Saba	48411	47
2578	San Sebastian	72131	42
2579	Sanborn	46111	45
2580	Sanders	30089	28
2581	Sandoval	35043	33
2582	Sandusky	39143	38
2583	Sangamon	17167	15
2584	Sanilac	26151	24
2585	Sanpete	49039	48
2586	Santa Barbara	6083	5
2587	Santa Clara	6085	5
2588	Santa Cruz	4023	3
2589	Santa Cruz	6087	5
2590	Santa Fe	35049	33
2591	Santa Isabel	72133	42
2592	Santa Rosa	12113	10
2593	Sarasota	12115	10
2594	Saratoga	36091	34
2595	Sargent	38081	36
2596	Sarpy	31153	29
2597	Sauk	55111	54
2598	Saunders	31155	29
2599	Sawyer	55113	54
2600	Schenectady	36093	34
2601	Schleicher	48413	47
2602	Schley	13249	11
2603	Schoharie	36095	34
2604	Schoolcraft	26153	24
2605	Schuyler	17169	15
2606	Schuyler	29197	27
2607	Schuyler	36097	34
2608	Schuylkill	42107	41
2609	Scioto	39145	38
2610	Scotland	37165	35
2611	Scotland	29199	27
2612	Scott	19163	17
2613	Scott	28123	26
2614	Scott	17171	15
2615	Scott	51169	51
2616	Scott	21209	19
2617	Scott	27139	25
2618	Scott	5127	4
2619	Scott	47151	46
2620	Scott	29201	27
2621	Scott	20171	18
2622	Scott	18143	16
2623	Scotts Bluff	31157	29
2624	Screven	13251	11
2625	Scurry	48415	47
2626	Searcy	5129	4
2627	Sebastian	5131	4
2628	Sedgwick	8115	6
2629	Sedgwick	20173	18
2630	Seminole	40133	39
2631	Seminole	12117	10
2632	Seminole	13253	11
2633	Seneca	39147	38
2634	Seneca	36099	34
2635	Sequatchie	47153	46
2636	Sequoyah	40135	39
2637	Sevier	47155	46
2638	Sevier	5133	4
2639	Sevier	49041	48
2640	Seward	31159	29
2641	Seward	20175	18
2642	Shackelford	48417	47
2643	Shannon	29203	27
2644	Sharkey	28125	26
2645	Sharp	5135	4
2646	Shasta	6089	5
2647	Shawano	55115	54
2648	Shawnee	20177	18
2649	Sheboygan	55117	54
2650	Shelby	18145	16
2651	Shelby	29205	27
2652	Shelby	17173	15
2653	Shelby	1117	0
2654	Shelby	47157	46
2655	Shelby	19165	17
2656	Shelby	39149	38
2657	Shelby	48419	47
2658	Shelby	21211	19
2659	Shenandoah	51171	51
2660	Sherburne	27141	25
2661	Sheridan	30091	28
2662	Sheridan	20179	18
2663	Sheridan	38083	36
2664	Sheridan	56033	55
2665	Sheridan	31161	29
2666	Sherman	20181	18
2667	Sherman	41055	40
2668	Sherman	48421	47
2669	Sherman	31163	29
2670	Shiawassee	26155	24
2671	Shoshone	16079	14
2672	Sibley	27143	25
2673	Sierra	35051	33
2674	Sierra	6091	5
2675	Silver Bow	30093	28
2676	Simpson	21213	19
2677	Simpson	28127	26
2678	Sioux	38085	36
2679	Sioux	19167	17
2680	Sioux	31165	29
2681	Siskiyou	6093	5
2682	Sitka City and Borough	2220	1
2683	Skagit	53057	52
2684	Skagway Municipality	2230	1
2685	Skamania	53059	52
2686	Slope	38087	36
2687	Smith	20183	18
2688	Smith	48423	47
2689	Smith	47159	46
2690	Smith	28129	26
2691	Smyth	51173	51
2692	Snohomish	53061	52
2693	Snyder	42109	41
2694	Socorro	35053	33
2695	Solano	6095	5
2696	Somerset	24039	22
2697	Somerset	34035	32
2698	Somerset	23025	21
2699	Somerset	42111	41
2700	Somervell	48425	47
2701	Sonoma	6097	5
2702	Southampton	51175	51
2703	Southeast Fairbanks Census Area	2240	1
2704	Spalding	13255	11
2705	Spartanburg	45083	44
2706	Spencer	21215	19
2707	Spencer	18147	16
2708	Spink	46115	45
2709	Spokane	53063	52
2710	Spotsylvania	51177	51
2711	St. Bernard	22087	20
2712	St. Charles	22089	20
2713	St. Charles	29183	27
2714	St. Clair	29185	27
2715	St. Clair	1115	0
2716	St. Clair	17163	15
2717	St. Clair	26147	24
2718	St. Croix	78010	50
2719	St. Croix	55109	54
2720	St. Francis	5123	4
2721	St. Francois	29187	27
2722	St. Helena	22091	20
2723	St. James	22093	20
2724	St. John	78020	50
2725	St. John the Baptist	22095	20
2726	St. Johns	12109	10
2727	St. Joseph	18141	16
2728	St. Joseph	26149	24
2729	St. Landry	22097	20
2730	St. Lawrence	36089	34
2731	St. Louis	29189	27
2732	St. Louis	27137	25
2733	St. Louis city	29510	27
2734	St. Lucie	12111	10
2735	St. Martin	22099	20
2736	St. Mary	22101	20
2737	St. Mary's	24037	22
2738	St. Tammany	22103	20
2739	St. Thomas	78030	50
2740	Stafford	20185	18
2741	Stafford	51179	51
2742	Stanislaus	6099	5
2743	Stanley	46117	45
2744	Stanly	37167	35
2745	Stanton	20187	18
2746	Stanton	31167	29
2747	Stark	38089	36
2748	Stark	39151	38
2749	Stark	17175	15
2750	Starke	18149	16
2751	Starr	48427	47
2752	Staunton city	51790	51
2753	Ste. Genevieve	29186	27
2754	Stearns	27145	25
2755	Steele	27147	25
2756	Steele	38091	36
2757	Stephens	48429	47
2758	Stephens	40137	39
2759	Stephens	13257	11
2760	Stephenson	17177	15
2761	Sterling	48431	47
2762	Steuben	36101	34
2763	Steuben	18151	16
2764	Stevens	27149	25
2765	Stevens	53065	52
2766	Stevens	20189	18
2767	Stewart	13259	11
2768	Stewart	47161	46
2769	Stillwater	30095	28
2770	Stoddard	29207	27
2771	Stokes	37169	35
2772	Stone	29209	27
2773	Stone	28131	26
2774	Stone	5137	4
2775	Stonewall	48433	47
2776	Storey	32029	30
2777	Story	19169	17
2778	Strafford	33017	31
2779	Stutsman	38093	36
2780	Sublette	56035	55
2781	Suffolk	25025	23
2782	Suffolk	36103	34
2783	Suffolk city	51800	51
2784	Sullivan	33019	31
2785	Sullivan	29211	27
2786	Sullivan	42113	41
2787	Sullivan	18153	16
2788	Sullivan	36105	34
2789	Sullivan	47163	46
2790	Sully	46119	45
2791	Summers	54089	53
2792	Summit	8117	6
2793	Summit	39153	38
2794	Summit	49043	48
2795	Sumner	20191	18
2796	Sumner	47165	46
2797	Sumter	1119	0
2798	Sumter	45085	44
2799	Sumter	13261	11
2800	Sumter	12119	10
2801	Sunflower	28133	26
2802	Surry	37171	35
2803	Surry	51181	51
2804	Susquehanna	42115	41
2805	Sussex	34037	32
2806	Sussex	10005	8
2807	Sussex	51183	51
2808	Sutter	6101	5
2809	Sutton	48435	47
2810	Suwannee	12121	10
2811	Swain	37173	35
2812	Sweet Grass	30097	28
2813	Sweetwater	56037	55
2814	Swift	27151	25
2815	Swisher	48437	47
2816	Switzerland	18155	16
2817	Talbot	24041	22
2818	Talbot	13263	11
2819	Taliaferro	13265	11
2820	Talladega	1121	0
2821	Tallahatchie	28135	26
2822	Tallapoosa	1123	0
2823	Tama	19171	17
2824	Taney	29213	27
2825	Tangipahoa	22105	20
2826	Taos	35055	33
2827	Tarrant	48439	47
2828	Tate	28137	26
2829	Tattnall	13267	11
2830	Taylor	54091	53
2831	Taylor	21217	19
2832	Taylor	12123	10
2833	Taylor	13269	11
2834	Taylor	19173	17
2835	Taylor	55119	54
2836	Taylor	48441	47
2837	Tazewell	17179	15
2838	Tazewell	51185	51
2839	Tehama	6103	5
2840	Telfair	13271	11
2841	Teller	8119	6
2842	Tensas	22107	20
2843	Terrebonne	22109	20
2844	Terrell	48443	47
2845	Terrell	13273	11
2846	Terry	48445	47
2847	Teton	30099	28
2848	Teton	16081	14
2849	Teton	56039	55
2850	Texas	29215	27
2851	Texas	40139	39
2852	Thayer	31169	29
2853	Thomas	31171	29
2854	Thomas	20193	18
2855	Thomas	13275	11
2856	Throckmorton	48447	47
2857	Thurston	53067	52
2858	Thurston	31173	29
2859	Tift	13277	11
2860	Tillamook	41057	40
2861	Tillman	40141	39
2862	Tinian	69120	37
2863	Tioga	36107	34
2864	Tioga	42117	41
2865	Tippah	28139	26
2866	Tippecanoe	18157	16
2867	Tipton	47167	46
2868	Tipton	18159	16
2869	Tishomingo	28141	26
2870	Titus	48449	47
2871	Toa Alta	72135	42
2872	Toa Baja	72137	42
2873	Todd	27153	25
2874	Todd	46121	45
2875	Todd	21219	19
2876	Tolland	9013	7
2877	Tom Green	48451	47
2878	Tompkins	36109	34
2879	Tooele	49045	48
2880	Toole	30101	28
2881	Toombs	13279	11
2882	Torrance	35057	33
2883	Towner	38095	36
2884	Towns	13281	11
2885	Traill	38097	36
2886	Transylvania	37175	35
2887	Traverse	27155	25
2888	Travis	48453	47
2889	Treasure	30103	28
2890	Trego	20195	18
2891	Trempealeau	55121	54
2892	Treutlen	13283	11
2893	Trigg	21221	19
2894	Trimble	21223	19
2895	Trinity	48455	47
2896	Trinity	6105	5
2897	Tripp	46123	45
2898	Troup	13285	11
2899	Trousdale	47169	46
2900	Trujillo Alto	72139	42
2901	Trumbull	39155	38
2902	Tucker	54093	53
2903	Tulare	6107	5
2904	Tulsa	40143	39
2905	Tunica	28143	26
2906	Tuolumne	6109	5
2907	Turner	13287	11
2908	Turner	46125	45
2909	Tuscaloosa	1125	0
2910	Tuscarawas	39157	38
2911	Tuscola	26157	24
2912	Twiggs	13289	11
2913	Twin Falls	16083	14
2914	Tyler	48457	47
2915	Tyler	54095	53
2916	Tyrrell	37177	35
2917	Uinta	56041	55
2918	Uintah	49047	48
2919	Ulster	36111	34
2920	Umatilla	41059	40
2921	Unicoi	47171	46
2922	Union	34039	32
2923	Union	47173	46
2924	Union	18161	16
2925	Union	45087	44
2926	Union	21225	19
2927	Union	35059	33
2928	Union	5139	4
2929	Union	13291	11
2930	Union	12125	10
2931	Union	28145	26
2932	Union	39159	38
2933	Union	46127	45
2934	Union	17181	15
2935	Union	37179	35
2936	Union	22111	20
2937	Union	41061	40
2938	Union	42119	41
2939	Union	19175	17
2940	Unknown	\N	13
2941	Unknown	\N	14
2942	Unknown	\N	18
2943	Unknown	\N	3
2944	Unknown	\N	38
2945	Unknown	\N	46
2946	Unknown	\N	45
2947	Unknown	\N	40
2948	Unknown	\N	7
2949	Unknown	\N	54
2950	Unknown	\N	37
2951	Unknown	\N	31
2952	Unknown	\N	15
2953	Unknown	\N	49
2954	Unknown	\N	5
2955	Unknown	\N	21
2956	Unknown	\N	6
2957	Unknown	\N	32
2958	Unknown	\N	34
2959	Unknown	\N	10
2960	Unknown	\N	23
2961	Unknown	\N	30
2962	Unknown	\N	29
2963	Unknown	\N	28
2964	Unknown	\N	44
2965	Unknown	\N	12
2966	Unknown	\N	43
2967	Unknown	\N	19
2968	Unknown	\N	25
2969	Unknown	\N	42
2970	Unknown	\N	48
2971	Unknown	\N	16
2972	Unknown	\N	17
2973	Unknown	\N	4
2974	Unknown	\N	22
2975	Unknown	\N	33
2976	Unknown	\N	26
2977	Unknown	\N	20
2978	Unknown	\N	47
2979	Unknown	\N	1
2980	Unknown	\N	36
2981	Unknown	\N	51
2982	Unknown	\N	27
2983	Unknown	\N	53
2984	Unknown	\N	55
2985	Unknown	\N	24
2986	Unknown	\N	39
2987	Unknown	\N	41
2988	Unknown	\N	8
2989	Unknown	\N	52
2990	Unknown	\N	11
2991	Unknown	\N	50
2992	Upshur	54097	53
2993	Upshur	48459	47
2994	Upson	13293	11
2995	Upton	48461	47
2996	Utah	49049	48
2997	Utuado	72141	42
2998	Uvalde	48463	47
2999	Val Verde	48465	47
3000	Valdez-Cordova Census Area	2261	1
3001	Valencia	35061	33
3002	Valley	30105	28
3003	Valley	31175	29
3004	Valley	16085	14
3005	Van Buren	26159	24
3006	Van Buren	19177	17
3007	Van Buren	5141	4
3008	Van Buren	47175	46
3009	Van Wert	39161	38
3010	Van Zandt	48467	47
3011	Vance	37181	35
3012	Vanderburgh	18163	16
3013	Vega Alta	72143	42
3014	Vega Baja	72145	42
3015	Venango	42121	41
3016	Ventura	6111	5
3017	Vermilion	22113	20
3018	Vermilion	17183	15
3019	Vermillion	18165	16
3020	Vernon	55123	54
3021	Vernon	29217	27
3022	Vernon	22115	20
3023	Victoria	48469	47
3024	Vieques	72147	42
3025	Vigo	18167	16
3026	Vilas	55125	54
3027	Villalba	72149	42
3028	Vinton	39163	38
3029	Virginia Beach city	51810	51
3030	Volusia	12127	10
3031	Wabash	18169	16
3032	Wabash	17185	15
3033	Wabasha	27157	25
3034	Wabaunsee	20197	18
3035	Wadena	27159	25
3036	Wagoner	40145	39
3037	Wahkiakum	53069	52
3038	Wake	37183	35
3039	Wakulla	12129	10
3040	Waldo	23027	21
3041	Walker	48471	47
3042	Walker	13295	11
3043	Walker	1127	0
3044	Walla Walla	53071	52
3045	Wallace	20199	18
3046	Waller	48473	47
3047	Wallowa	41063	40
3048	Walsh	38099	36
3049	Walthall	28147	26
3050	Walton	13297	11
3051	Walton	12131	10
3052	Walworth	55127	54
3053	Walworth	46129	45
3054	Wapello	19179	17
3055	Ward	38101	36
3056	Ward	48475	47
3057	Ware	13299	11
3058	Warren	36113	34
3059	Warren	17187	15
3060	Warren	28149	26
3061	Warren	51187	51
3062	Warren	19181	17
3063	Warren	18171	16
3064	Warren	29219	27
3065	Warren	13301	11
3066	Warren	21227	19
3067	Warren	34041	32
3068	Warren	42123	41
3069	Warren	47177	46
3070	Warren	39165	38
3071	Warren	37185	35
3072	Warrick	18173	16
3073	Wasatch	49051	48
3074	Wasco	41065	40
3075	Waseca	27161	25
3076	Washakie	56043	55
3077	Washburn	55129	54
3078	Washington	5143	4
3079	Washington	20201	18
3080	Washington	21229	19
3081	Washington	22117	20
3082	Washington	47179	46
3083	Washington	36115	34
3084	Washington	39167	38
3085	Washington	29221	27
3086	Washington	40147	39
3087	Washington	48477	47
3088	Washington	24043	22
3089	Washington	1129	0
3090	Washington	18175	16
3091	Washington	19183	17
3092	Washington	50023	49
3093	Washington	23029	21
3094	Washington	17189	15
3095	Washington	49053	48
3096	Washington	42125	41
3097	Washington	16087	14
3098	Washington	41067	40
3099	Washington	28151	26
3100	Washington	31177	29
3101	Washington	44009	43
3102	Washington	51191	51
3103	Washington	12133	10
3104	Washington	55131	54
3105	Washington	37187	35
3106	Washington	27163	25
3107	Washington	13303	11
3108	Washington	8121	6
3109	Washita	40149	39
3110	Washoe	32031	30
3111	Washtenaw	26161	24
3112	Watauga	37189	35
3113	Watonwan	27165	25
3114	Waukesha	55133	54
3115	Waupaca	55135	54
3116	Waushara	55137	54
3117	Wayne	28153	26
3118	Wayne	49055	48
3119	Wayne	29223	27
3120	Wayne	54099	53
3121	Wayne	18177	16
3122	Wayne	37191	35
3123	Wayne	21231	19
3124	Wayne	39169	38
3125	Wayne	19185	17
3126	Wayne	31179	29
3127	Wayne	42127	41
3128	Wayne	26163	24
3129	Wayne	13305	11
3130	Wayne	47181	46
3131	Wayne	36117	34
3132	Wayne	17191	15
3133	Waynesboro city	51820	51
3134	Weakley	47183	46
3135	Webb	48479	47
3136	Weber	49057	48
3137	Webster	19187	17
3138	Webster	29225	27
3139	Webster	54101	53
3140	Webster	28155	26
3141	Webster	13307	11
3142	Webster	31181	29
3143	Webster	21233	19
3144	Webster	22119	20
3145	Weld	8123	6
3146	Wells	18179	16
3147	Wells	38103	36
3148	West Baton Rouge	22121	20
3149	West Carroll	22123	20
3150	West Feliciana	22125	20
3151	Westchester	36119	34
3152	Westmoreland	42129	41
3153	Westmoreland	51193	51
3154	Weston	56045	55
3155	Wetzel	54103	53
3156	Wexford	26165	24
3157	Wharton	48481	47
3158	Whatcom	53073	52
3159	Wheatland	30107	28
3160	Wheeler	31183	29
3161	Wheeler	48483	47
3162	Wheeler	13309	11
3163	Wheeler	41069	40
3164	White	18181	16
3165	White	5145	4
3166	White	17193	15
3167	White	13311	11
3168	White	47185	46
3169	White Pine	32033	30
3170	Whiteside	17195	15
3171	Whitfield	13313	11
3172	Whitley	18183	16
3173	Whitley	21235	19
3174	Whitman	53075	52
3175	Wibaux	30109	28
3176	Wichita	48485	47
3177	Wichita	20203	18
3178	Wicomico	24045	22
3179	Wilbarger	48487	47
3180	Wilcox	1131	0
3181	Wilcox	13315	11
3182	Wilkes	13317	11
3183	Wilkes	37193	35
3184	Wilkin	27167	25
3185	Wilkinson	13319	11
3186	Wilkinson	28157	26
3187	Will	17197	15
3188	Willacy	48489	47
3189	Williams	39171	38
3190	Williams	38105	36
3191	Williamsburg	45089	44
3192	Williamsburg city	51830	51
3193	Williamson	17199	15
3194	Williamson	48491	47
3195	Williamson	47187	46
3196	Wilson	37195	35
3197	Wilson	47189	46
3198	Wilson	48493	47
3199	Wilson	20205	18
3200	Winchester city	51840	51
3201	Windham	50025	49
3202	Windham	9015	7
3203	Windsor	50027	49
3204	Winkler	48495	47
3205	Winn	22127	20
3206	Winnebago	19189	17
3207	Winnebago	55139	54
3208	Winnebago	17201	15
3209	Winneshiek	19191	17
3210	Winona	27169	25
3211	Winston	28159	26
3212	Winston	1133	0
3213	Wirt	54105	53
3214	Wise	51195	51
3215	Wise	48497	47
3216	Wolfe	21237	19
3217	Wood	48499	47
3218	Wood	39173	38
3219	Wood	54107	53
3220	Wood	55141	54
3221	Woodbury	19193	17
3222	Woodford	21239	19
3223	Woodford	17203	15
3224	Woodruff	5147	4
3225	Woods	40151	39
3226	Woodson	20207	18
3227	Woodward	40153	39
3228	Worcester	24047	22
3229	Worcester	25027	23
3230	Worth	13321	11
3231	Worth	19195	17
3232	Worth	29227	27
3233	Wrangell City and Borough	2275	1
3234	Wright	27171	25
3235	Wright	19197	17
3236	Wright	29229	27
3237	Wyandot	39175	38
3238	Wyandotte	20209	18
3239	Wyoming	36121	34
3240	Wyoming	54109	53
3241	Wyoming	42131	41
3242	Wythe	51197	51
3243	Yabucoa	72151	42
3244	Yadkin	37197	35
3245	Yakima	53077	52
3246	Yakutat plus Hoonah-Angoon	2998	1
3247	Yalobusha	28161	26
3248	Yamhill	41071	40
3249	Yancey	37199	35
3250	Yankton	46135	45
3251	Yates	36123	34
3252	Yauco	72153	42
3253	Yavapai	4025	3
3254	Yazoo	28163	26
3255	Yell	5149	4
3256	Yellow Medicine	27173	25
3257	Yellowstone	30111	28
3258	Yoakum	48501	47
3259	Yolo	6113	5
3260	York	31185	29
3261	York	42133	41
3262	York	51199	51
3263	York	23031	21
3264	York	45091	44
3265	Young	48503	47
3266	Yuba	6115	5
3267	Yukon-Koyukuk Census Area	2290	1
3268	Yuma	8125	6
3269	Yuma	4027	3
3270	Zapata	48505	47
3271	Zavala	48507	47
3272	Ziebach	46137	45
\.


--
-- TOC entry 2948 (class 0 OID 16406)
-- Dependencies: 204
-- Data for Name: counts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.counts (id, date, cases, deaths, id_state, id_county) FROM stdin;
\.


--
-- TOC entry 2949 (class 0 OID 16421)
-- Dependencies: 205
-- Data for Name: mask_use; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mask_use (id, never, rarely, sometimes, frequently, always, id_county) FROM stdin;
\.


--
-- TOC entry 2946 (class 0 OID 16385)
-- Dependencies: 202
-- Data for Name: states; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.states (id, name, fips) FROM stdin;
0	Alabama	1
1	Alaska	2
2	American Samoa	60
3	Arizona	4
4	Arkansas	5
5	California	6
6	Colorado	8
7	Connecticut	9
8	Delaware	10
9	District of Columbia	11
10	Florida	12
11	Georgia	13
12	Guam	66
13	Hawaii	15
14	Idaho	16
15	Illinois	17
16	Indiana	18
17	Iowa	19
18	Kansas	20
19	Kentucky	21
20	Louisiana	22
21	Maine	23
22	Maryland	24
23	Massachusetts	25
24	Michigan	26
25	Minnesota	27
26	Mississippi	28
27	Missouri	29
28	Montana	30
29	Nebraska	31
30	Nevada	32
31	New Hampshire	33
32	New Jersey	34
33	New Mexico	35
34	New York	36
35	North Carolina	37
36	North Dakota	38
37	Northern Mariana Islands	69
38	Ohio	39
39	Oklahoma	40
40	Oregon	41
41	Pennsylvania	42
42	Puerto Rico	72
43	Rhode Island	44
44	South Carolina	45
45	South Dakota	46
46	Tennessee	47
47	Texas	48
48	Utah	49
49	Vermont	50
50	Virgin Islands	78
51	Virginia	51
52	Washington	53
53	West Virginia	54
54	Wisconsin	55
55	Wyoming	56
\.


--
-- TOC entry 2811 (class 2606 OID 16400)
-- Name: counties counties_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counties
    ADD CONSTRAINT counties_pkey PRIMARY KEY (id);


--
-- TOC entry 2813 (class 2606 OID 16410)
-- Name: counts counts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts
    ADD CONSTRAINT counts_pkey PRIMARY KEY (id);


--
-- TOC entry 2815 (class 2606 OID 16425)
-- Name: mask_use mask_use_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mask_use
    ADD CONSTRAINT mask_use_pkey PRIMARY KEY (id);


--
-- TOC entry 2809 (class 2606 OID 16392)
-- Name: states states_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.states
    ADD CONSTRAINT states_pkey PRIMARY KEY (id);


--
-- TOC entry 2816 (class 2606 OID 16401)
-- Name: counties counties_id_state_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counties
    ADD CONSTRAINT counties_id_state_fkey FOREIGN KEY (id_state) REFERENCES public.states(id);


--
-- TOC entry 2818 (class 2606 OID 16416)
-- Name: counts counts_id_county_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts
    ADD CONSTRAINT counts_id_county_fkey FOREIGN KEY (id_county) REFERENCES public.counties(id);


--
-- TOC entry 2817 (class 2606 OID 16411)
-- Name: counts counts_id_state_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counts
    ADD CONSTRAINT counts_id_state_fkey FOREIGN KEY (id_state) REFERENCES public.states(id);


--
-- TOC entry 2819 (class 2606 OID 16426)
-- Name: mask_use mask_use_id_county_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mask_use
    ADD CONSTRAINT mask_use_id_county_fkey FOREIGN KEY (id_county) REFERENCES public.counties(id);


-- Completed on 2023-04-20 13:42:14

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.2

-- Started on 2023-04-20 13:42:14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2023-04-20 13:42:16

--
-- PostgreSQL database dump complete
--

-- Completed on 2023-04-20 13:42:16

--
-- PostgreSQL database cluster dump complete
--

