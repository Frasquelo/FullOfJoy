# -*- coding: utf-8 -*-
"""Contenuti degli articoli del blog FullOfJoy.

Per modificare un articolo: cambia il testo qui e lancia `python tools/build-blog.py`.
Le pagine in /blog/ vengono rigenerate (non modificarle a mano).
Campi: slug, title (<= 60 car. circa), desc (~150 car.), h1, lead, cat, img, alt, svc (url, etichetta),
related (slug), mins, body (HTML), faq [(domanda, risposta)].
"""

ARTICLES = [
{
"slug": "cucciolo-che-morde",
"title": "Cucciolo che morde: cosa fare e cosa evitare",
"desc": "Il cucciolo morde mani, vestiti e mobili? È normale, ma si può guidare. Ecco cosa fare, cosa evitare e quando chiedere aiuto a un educatore.",
"h1": "Cucciolo che morde: cosa fare e cosa evitare",
"lead": "Mani, caviglie, vestiti, mobili: i cuccioli esplorano il mondo con la bocca. Capire perché lo fanno è il primo passo per insegnargli, con calma, a usarla meglio.",
"cat": "Cuccioli", "img": "percorso-cucciolo.webp", "alt": "Cucciolo di beagle nel prato del campo",
"svc": ("servizi/puppy-training.html", "Scopri il puppy training"),
"related": ["quando-iniziare-puppy-training", "educazione-senza-coercizione", "come-scegliere-educatore-cinofilo-piacenza"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> mordicchiare è normale nei cuccioli. Non serve spaventarli o "metterli a posto": serve offrire alternative, interrompere il gioco quando i denti toccano la pelle e premiare i comportamenti che vuoi vedere.</p></div>
<h2>Perché il cucciolo morde</h2>
<p>Un cucciolo non ha mani: usa la bocca per conoscere oggetti, giocare con i fratelli, calmare il fastidio dei denti che cambiano e attirare la tua attenzione. Nel gioco con gli altri cuccioli impara anche a dosare la forza, perché un morso troppo forte fa finire la partita. Con noi umani questo apprendimento va accompagnato.</p>
<h2>Cosa fare</h2>
<ul>
<li><strong>Interrompi il gioco con calma.</strong> Quando senti i denti sulla pelle, smetti di muoverti e di parlare, o alzati e allontanati per qualche secondo. Il messaggio è: "se mordi, il divertimento finisce".</li>
<li><strong>Offri un'alternativa.</strong> Tieni sempre a portata di mano un gioco da mordere. Appena il cucciolo lo prende, premialo con una festa o con un po' di gioco.</li>
<li><strong>Premia la calma.</strong> Quando è tranquillo, ignoralo meno: attenzione, carezze e un croccantino arrivano proprio nei momenti in cui non morde.</li>
<li><strong>Organizza la giornata.</strong> Un cucciolo stanco e già sfamato morde di più. Sonnellini regolari, passeggiate adatte all'età e giochi di fiuto aiutano molto.</li>
</ul>
<h2>Cosa evitare</h2>
<ul>
<li>Urlare, dare colpetti sul muso o tenergli la bocca chiusa: possono spaventarlo, rendere il gioco più agitato o insegnargli a diffidare delle mani.</li>
<li>Giocare a lottare con le mani come con un altro cane: lo invita a usare i denti.</li>
<li>Rincorrerlo quando scappa con qualcosa in bocca: per lui diventa un gioco.</li>
</ul>
<h2>Quando chiedere aiuto</h2>
<p>Se il morso è intenso, il cucciolo diventa rigido o ringhia quando gli togli qualcosa, o se in casa non riuscite più a gestire la situazione, conviene farsi guardare da un educatore: spesso bastano poche lezioni per cambiare le abitudini della famiglia, che è la parte più importante. Parlane anche con il veterinario se i morsi sembrano legati a dolore o fastidio.</p>
""",
"faq": [
("A che età smettono di mordere i cuccioli?", "Dipende dal cane e da come viene guidato. In genere la fase più intensa coincide con il cambio dei denti, nei primi mesi di vita; con costanza e alternative adatte il morso diminuisce gradualmente."),
("È giusto lasciar fare il cucciolo, tanto gli passa?", "Se non viene guidato, il mordicchiare può trasformarsi in abitudine. Meglio insegnare presto, con calma, cosa si può mordere e cosa no."),
],
},
{
"slug": "quando-iniziare-puppy-training",
"title": "Puppy training: quando iniziare e cosa si fa",
"desc": "Quando iniziare il puppy training, cosa si impara nelle prime lezioni e come scegliere un percorso rispettoso per il tuo cucciolo a Piacenza.",
"h1": "Puppy training: quando iniziare e cosa si fa nelle prime lezioni",
"lead": "I primi mesi sono il momento più prezioso per costruire fiducia, abitudini e serenità. Ecco come si svolge un percorso per cuccioli fatto bene.",
"cat": "Cuccioli", "img": "puppy-training.webp", "alt": "Cucciolo durante una lezione di puppy training",
"svc": ("servizi/puppy-training.html", "Vedi il percorso puppy training"),
"related": ["cucciolo-che-morde", "educazione-senza-coercizione", "cane-reattivo-abbaia-altri-cani"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> puoi iniziare presto, già nelle prime settimane a casa. Il puppy training non è "far fare esercizi" al cucciolo: è dargli esperienze positive, spiegarvi i vostri bisogni e preparare la tua famiglia.</p></div>
<h2>Quando iniziare</h2>
<p>Non esiste un giorno esatto, ma prima si comincia, meglio è: nei primi mesi il cucciolo è particolarmente aperto a conoscere persone, ambienti e rumori. Il momento giusto per iniziare le lezioni di gruppo dipende anche dal piano vaccinale e dalle indicazioni del tuo veterinario: chiedigli quando è possibile frequentare il campo e incontrare altri cani. Una prima consulenza individuale, nel frattempo, è un'ottima base.</p>
<h2>Cosa si fa nelle prime lezioni</h2>
<ul>
<li><strong>Socializzazione guidata:</strong> persone, ambienti, superfici e rumori nuovi, sempre con il giusto ritmo, senza forzare.</li>
<li><strong>Gestione della bocca:</strong> cosa si può mordere, come interrompere il gioco, come manipolare il cucciolo senza stress.</li>
<li><strong>Prime regole di convivenza:</strong> stare tranquilli, aspettare, tornare quando lo chiami, imparare i tempi della giornata.</li>
<li><strong>Richiamo e guinzaglio:</strong> i fondamenti, costruiti con gioco e premi.</li>
<li><strong>Essere lasciati soli:</strong> come abituarlo gradualmente senza ansia.</li>
</ul>
<h2>Il lavoro vero è con te</h2>
<p>Il cucciolo impara dalla tua coerenza quotidiana. Per questo una buona lezione spiega a te cosa fare: come premiare, come gestire il gioco, come evitare errori comuni. Un cucciolo educato con gentilezza impara che le persone sono una fonte di cose belle, ed è la base per un adulto sereno.</p>
<h2>Come scegliere il percorso</h2>
<p>Cerca un educatore che usi solo metodi basati su motivazione e premio, che lavori con gruppi piccoli e che ti spieghi cosa fa e perché. Diffida di chi promette risultati in pochi giorni o usa strumenti di costrizione.</p>
""",
"faq": [
("Un cucciolo può fare lezione prima di finire le vaccinazioni?", "Dipende dalle indicazioni del veterinario. Nel frattempo si possono iniziare consulenze individuali e attività in ambienti sicuri."),
("Il puppy training serve anche se ho già avuto cani?", "Sì: ogni cucciolo è diverso e le lezioni aiutano a prevenire problemi, oltre a offrire un confronto con un professionista."),
],
},
{
"slug": "cane-che-tira-al-guinzaglio",
"title": "Cane che tira al guinzaglio: come cambiare",
"desc": "Perché il cane tira al guinzaglio e come insegnargli a camminare al tuo fianco senza strattoni, con metodi gentili e un po' di allenamento costante.",
"h1": "Cane che tira al guinzaglio: perché succede e come migliorare",
"lead": "La passeggiata dovrebbe essere un piacere, non una lotta. Tirare è un comportamento molto comune e si può cambiare, con pazienza e le tecniche giuste.",
"cat": "Educazione di base", "img": "educazione-base.webp", "alt": "Silvia con tre cani durante l'educazione di base",
"svc": ("servizi/educazione-base.html", "Vedi l'educazione di base"),
"related": ["il-richiamo-non-funziona", "collari-a-strangolo-ed-elettrici", "educazione-senza-coercizione"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> il cane tira perché funziona: tirando arriva dove vuole. Per cambiare serve far diventare più conveniente camminare vicino a te e rendere meno efficace tirare, senza strattoni né punizioni.</p></div>
<h2>Perché tira</h2>
<ul>
<li><strong>Funziona:</strong> ogni volta che tirando raggiunge un albero o un odore, il comportamento viene rinforzato.</li>
<li><strong>Va più veloce di noi:</strong> la sua velocità naturale è più alta della nostra.</li>
<li><strong>È eccitato:</strong> fuori casa c'è tantissimo da annusare e controllare.</li>
<li><strong>Nessuno gli ha insegnato l'alternativa:</strong> camminare al fianco è una competenza, non un istinto.</li>
</ul>
<h2>Come lavorare</h2>
<ol>
<li><strong>Attrezzatura comoda.</strong> Pettorina ben adattata e guinzaglio di lunghezza adeguata; evita strumenti che fanno male per "fermarlo".</li>
<li><strong>Parti dove c'è poca distrazione.</strong> In casa o in giardino, premiando ogni passo vicino a te.</li>
<li><strong>Fermati quando tira.</strong> Il guinzaglio teso non lo porta da nessuna parte: appena torna ad allentarlo, si riparte.</li>
<li><strong>Premia la posizione giusta.</strong> Un piccolo croccantino al fianco, a intervalli frequenti, gli spiega dove ti piace che stia.</li>
<li><strong>Dagli il permesso di annusare.</strong> Annusare è un bisogno: alterna tratti di camminata vicino a te e momenti di "libertà" a comando.</li>
<li><strong>Aumenta le distrazioni a piccoli passi.</strong> Giardino, strada tranquilla, poi zone più vivaci.</li>
</ol>
<h2>Quanto ci vuole</h2>
<p>Dipende dal cane e dalla costanza. Pochi minuti al giorno fatti bene valgono più di passeggiate lunghe con continue lotte. Se il cane è molto eccitato, reattivo o ti trascina via, conviene chiedere aiuto per impostare un percorso su misura.</p>
""",
"faq": [
("Meglio pettorina o collare?", "Per camminare e allenare la pettorina ben fatta è in genere più comoda e riduce lo stress sul collo. Evita collari che stringono o fanno male."),
("Il cane tira solo con me: è normale?", "Sì, cambia con chi lo porta in base a come si è abituato. Per questo è importante che tutta la famiglia segua lo stesso metodo."),
],
},
{
"slug": "il-richiamo-non-funziona",
"title": "Il richiamo non funziona? Come costruirlo davvero",
"desc": "Il cane non torna quando lo chiami? Ecco perché succede e come costruire un richiamo affidabile con gioco, premi e distrazioni graduali.",
"h1": "Il richiamo non funziona? Come costruirlo con metodo",
"lead": "Un richiamo affidabile è una delle cose più utili e sicure che puoi insegnare al tuo cane. Non nasce da un comando, ma da una relazione in cui tornare da te conviene.",
"cat": "Educazione di base", "img": "percorso-sport.webp", "alt": "Cane che corre felice nel prato",
"svc": ("servizi/educazione-base.html", "Vedi l'educazione di base"),
"related": ["cane-che-tira-al-guinzaglio", "cos-e-l-obedience-come-iniziare", "educazione-senza-coercizione"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> il cane non torna se tornare è noioso, spiacevole o se non ha mai davvero imparato. Costruisci il richiamo con premi di valore, giochi e distrazioni crescenti, e non chiamarlo mai per fargli qualcosa che non gradisce.</p></div>
<h2>Perché non torna</h2>
<ul>
<li>Il richiamo è stato insegnato in casa e testato direttamente fuori, dove c'è troppo da fare.</li>
<li>Tornare significa spesso la fine del divertimento (guinzaglio e si va via).</li>
<li>Il segnale è stato usato troppe volte senza premio, o ripetuto senza risposta fino a diventare rumore.</li>
<li>In passato è stato rimproverato al ritorno.</li>
</ul>
<h2>Come costruirlo</h2>
<ol>
<li><strong>Scegli un segnale tutto nuovo</strong> (una parola o un fischietto) e collegalo a qualcosa di bellissimo: un premio speciale o un gioco che ama.</li>
<li><strong>Parti da vicino e senza distrazioni.</strong> Chiama, premia, ripeti con tanti ritorni facili.</li>
<li><strong>Allunga le distanze e le distrazioni</strong> con piccoli passi, usando un lungo filo di sicurezza quando sei fuori.</li>
<li><strong>Premia sempre, generosamente.</strong> Il ritorno deve essere il momento migliore della passeggiata.</li>
<li><strong>Rendi il richiamo anche un invito a continuare.</strong> Dopo averlo chiamato e premiato, lascialo tornare a giocare: capirà che tornare non finisce la festa.</li>
</ol>
<h2>Errori da evitare</h2>
<ul>
<li>Sgridarlo quando arriva, anche se ha tardato.</li>
<li>Chiamarlo per fargli fare qualcosa che non gradisce (bagno, medicazione, fine del gioco) senza prima averlo premiato tante volte.</li>
<li>Lasciarlo libero in zone pericolose finché il richiamo non è davvero solido.</li>
</ul>
""",
"faq": [
("Quanto tempo serve per un richiamo affidabile?", "Settimane o mesi di pratica regolare, a seconda del cane. Un richiamo solido con le distrazioni più forti richiede costanza nel tempo."),
("Posso usare un fischietto?", "Sì: ha il vantaggio di essere sempre uguale e udibile da lontano. Va insegnato come qualsiasi altro segnale."),
],
},
{
"slug": "cane-reattivo-abbaia-altri-cani",
"title": "Cane reattivo: cosa fare se abbaia agli altri",
"desc": "Il cane abbaia, tira o si agita quando vede altri cani? Cos'è la reattività, perché succede e come lavorarci con gradualità e rispetto.",
"h1": "Cane che abbaia o reagisce agli altri cani: cosa fare",
"lead": "Un cane che esplode alla vista di un altro cane non è per forza aggressivo né maleducato. Spesso sta comunicando disagio, eccitazione o paura: capire cosa lo muove è il primo passo.",
"cat": "Supporto specifico", "img": "percorso-supporto.webp", "alt": "Due cani durante una gestione guidata dell'incontro",
"svc": ("servizi/cani-reattivi.html", "Scopri il lavoro con i cani reattivi"),
"related": ["collari-a-strangolo-ed-elettrici", "educazione-senza-coercizione", "come-scegliere-educatore-cinofilo-piacenza"],
"mins": 5,
"body": """
<div class="callout"><p><strong>In breve:</strong> la reattività è una risposta emotiva eccessiva a uno stimolo, spesso altri cani. Non si risolve punendo il cane, ma aumentando la distanza, cambiando le sue emozioni e dandogli strategie alternative.</p></div>
<h2>Cos'è la reattività</h2>
<p>Un cane reattivo abbaia, tira, si impenna o fa il "pazzo" in presenza di un trigger (cani, persone, bici, rumori). Le cause possono essere diverse: paura, frustrazione per non poter raggiungere l'altro cane, eccitazione eccessiva, scarse esperienze o esperienze negative. Dall'esterno sembra spesso aggressività, ma molti cani reattivi non hanno alcuna intenzione di fare del male.</p>
<h2>Cosa non fare</h2>
<ul>
<li><strong>Punire o strattonare.</strong> Può aumentare la tensione e associare l'altro cane a qualcosa di spiacevole, peggiorando il problema.</li>
<li><strong>Forzare l'incontro.</strong> "Così impara" funziona raramente: può aumentare paura e frustrazione.</li>
<li><strong>Tirarlo bruscamente</strong> o usare strumenti che fanno male.</li>
</ul>
<h2>Cosa funziona</h2>
<ol>
<li><strong>Distanza.</strong> Individua la distanza a cui il cane vede l'altro senza reagire e lavora lì.</li>
<li><strong>Cambiare l'emozione.</strong> Quando compare il trigger, arriva un premio di valore; il cane impara che "altro cane" significa "cose buone".</li>
<li><strong>Insegnare alternative.</strong> Guardarti, girarsi, allontanarsi con te: comportamenti premiati e allenati prima in situazioni facili.</li>
<li><strong>Gestire l'ambiente.</strong> Scegliere orari e percorsi tranquilli, evitare le situazioni che superano la sua soglia.</li>
<li><strong>Escludere cause mediche.</strong> Dolore e disagio fisico possono peggiorare le reazioni: un controllo veterinario è utile.</li>
</ol>
<h2>Perché affidarsi a un professionista</h2>
<p>Ogni cane ha la sua storia. Un educatore valuta cosa scatena la reazione, imposta un percorso graduale e ti insegna a leggere i segnali del cane. Se c'è il rischio di morso o il cane è molto sofferente, è importante coinvolgere anche il veterinario o un esperto del comportamento.</p>
""",
"faq": [
("Un cane reattivo può guarire?", "Molti cani migliorano molto con un lavoro graduale e costante. Non sempre diventano cani da incontri liberi: l'obiettivo è che stiano meglio e sappiano gestire la situazione."),
("Meglio evitare gli altri cani?", "Non del tutto: serve gestire le esposizioni. Evitarli sempre non risolve, affrontarli di colpo peggiora: la gradualità è la chiave."),
],
},
{
"slug": "collari-a-strangolo-ed-elettrici",
"title": "Collari a strangolo ed elettrici: perché no",
"desc": "Cosa sono i collari a strangolo, a punte ed elettrici, quali rischi comportano e quali alternative gentili esistono per educare il cane.",
"h1": "Collari a strangolo, a punte ed elettrici: perché non li usiamo",
"lead": "Educare un cane non richiede dolore, paura o intimidazione. Ecco cosa comportano questi strumenti e quali alternative funzionano.",
"cat": "Metodo", "img": "convivenza.webp", "alt": "Cane sereno in una buona convivenza",
"svc": ("metodo.html", "Leggi il nostro metodo"),
"related": ["educazione-senza-coercizione", "cane-che-tira-al-guinzaglio", "cane-reattivo-abbaia-altri-cani"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> questi strumenti funzionano perché il cane evita un fastidio o un dolore. Ma ottengono un comportamento soppresso, non capito, e possono avere effetti collaterali sull'emotività e sulla relazione con te.</p></div>
<h2>Come funzionano</h2>
<ul>
<li><strong>Collare a strangolo (o a scorrimento):</strong> si stringe sul collo quando il cane tira.</li>
<li><strong>Collare a punte:</strong> le punte premono sul collo quando il cane tira.</li>
<li><strong>Collare elettrico:</strong> invia una scossa o uno stimolo quando il cane compie un comportamento "sbagliato".</li>
</ul>
<p>In tutti i casi il cane smette di fare qualcosa per evitare la sensazione spiacevole. Il problema è che non impara cosa fare: impara a stare attento a ciò che gli fa male.</p>
<h2>Quali rischi</h2>
<ul>
<li><strong>Fisici:</strong> il collo è una zona delicata; strattoni e pressioni ripetute possono causare danni.</li>
<li><strong>Emotivi:</strong> paura, ansia e stress possono aumentare, soprattutto se il dolore viene associato ad altri cani, persone o rumori presenti in quel momento.</li>
<li><strong>Relazionali:</strong> il cane può diventare meno fiducioso verso chi usa lo strumento.</li>
<li><strong>Di efficacia:</strong> spesso serve aumentare l'intensità col tempo, e il comportamento riappare quando lo strumento non c'è.</li>
</ul>
<h2>Le alternative</h2>
<ol>
<li><strong>Rinforzo positivo:</strong> premiare i comportamenti giusti, così il cane ha motivo di ripeterli.</li>
<li><strong>Gestione dell'ambiente:</strong> evitare le situazioni che il cane non riesce ancora a gestire.</li>
<li><strong>Pettorina e guinzaglio adatti:</strong> comodi, senza dolore.</li>
<li><strong>Allenamento graduale:</strong> piccoli passi, dal facile al difficile.</li>
<li><strong>Aiuto professionale:</strong> per i casi complicati servono valutazione e piano su misura.</li>
</ol>
<h2>E nello sport?</h2>
<p>Anche nelle discipline sportive come il morso sportivo, l'obedience o la ricerca, si può costruire tutto sulla motivazione, sul gioco e sul rinforzo. È quello che facciamo ogni giorno al campo.</p>
""",
"faq": [
("Funzionano davvero?", "A volte sopprimono il comportamento in fretta, ma non insegnano un'alternativa e possono avere effetti collaterali su emotività e relazione."),
("Cosa uso se il mio cane tira tantissimo?", "Una pettorina ben adattata, un lavoro graduale e, se necessario, il supporto di un educatore. Meglio evitare strumenti che fanno male."),
],
},
{
"slug": "educazione-senza-coercizione",
"title": "Educazione senza coercizione: cosa significa",
"desc": "Cosa vuol dire davvero educare un cane senza coercizione: principi, esempi pratici e perché funziona anche con i cani più difficili.",
"h1": "Educazione senza coercizione: cosa significa davvero",
"lead": "\"Senza coercizione\" non vuol dire senza regole o senza guida. Vuol dire insegnare al cane cosa fare, in modo comprensibile e piacevole, senza ricorrere a paura o dolore.",
"cat": "Metodo", "img": "hero-cani.webp", "alt": "Sei cani di razze diverse che corrono felici nell'acqua",
"svc": ("metodo.html", "Leggi il nostro metodo"),
"related": ["collari-a-strangolo-ed-elettrici", "cucciolo-che-morde", "come-scegliere-educatore-cinofilo-piacenza"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> educare senza coercizione significa dare al cane motivi per scegliere il comportamento giusto: premi, gioco, chiarezza e un ambiente gestito. Le regole ci sono, ma si insegnano e non si impongono con la paura.</p></div>
<h2>I principi di base</h2>
<ul>
<li><strong>Chiarezza:</strong> dire al cane cosa vogliamo in modo che possa capirlo, con segnali coerenti.</li>
<li><strong>Motivazione:</strong> usare ciò che il cane ama (cibo, gioco, relazione) come moneta di scambio.</li>
<li><strong>Gradualità:</strong> aumentare la difficoltà un passo alla volta, senza chiedere troppo troppo presto.</li>
<li><strong>Prevenzione:</strong> organizzare la giornata e l'ambiente per ridurre le occasioni di sbagliare.</li>
<li><strong>Rispetto dei segnali:</strong> leggere paura, stress e disagio e tenerne conto.</li>
</ul>
<h2>Un esempio pratico</h2>
<p>Il cane salta addosso agli ospiti. Con la coercizione si ottiene (a volte) che smetta per paura della punizione. Senza coercizione si insegna un comportamento alternativo, ad esempio sedersi, che viene premiato, e si gestisce l'ingresso degli ospiti per evitare l'eccitazione eccessiva. Il cane impara cosa fare, non solo cosa non fare.</p>
<h2>Funziona anche con i cani "difficili"?</h2>
<p>Sì, anzi: i cani paurosi, reattivi o molto esuberanti traggono i maggiori benefici da un approccio che non aumenta il loro stress. Il lavoro può richiedere più tempo e più gestione, ma i risultati sono più stabili e il rapporto con te resta solido.</p>
<h2>Le regole contano</h2>
<p>Un cane educato con metodi gentili non è un cane senza confini. I limiti ci sono: la differenza è che il cane li impara con la guida, non per paura. Come in ogni relazione, serve coerenza da parte di tutta la famiglia.</p>
""",
"faq": [
("Senza coercizione vuol dire solo premi?", "No: significa anche gestione dell'ambiente, pause, limiti chiari e coerenza. Non si usano dolore, paura o intimidazione."),
("È adatto a tutte le razze?", "Sì: dal cucciolo al cane da sport, la motivazione e il rinforzo valgono per tutti, adattati alle caratteristiche del singolo cane."),
],
},
{
"slug": "cos-e-l-obedience-come-iniziare",
"title": "Obedience: cos'è e come iniziare",
"desc": "Cos'è l'obedience cinofila, quali esercizi prevede, quali cani possono praticarla e come iniziare con un percorso rispettoso e divertente.",
"h1": "Cos'è l'obedience e come iniziare con il tuo cane",
"lead": "L'obedience è uno sport di precisione e collaborazione tra cane e conduttore. Si può iniziare da zero, anche solo per divertirsi e rafforzare il rapporto.",
"cat": "Sport cinofili", "img": "obedience.webp", "alt": "Silvia Guglieri durante una sessione di obedience",
"svc": ("servizi/obedience.html", "Scopri l'obedience a FullOfJoy"),
"related": ["il-richiamo-non-funziona", "brevetti-cae-1-e-bh-differenze", "educazione-senza-coercizione"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> nell'obedience il cane esegue esercizi di obbedienza precisi insieme al conduttore: camminare al fianco, richiamo, resta, posizioni, riporto. Si può praticare per gioco o in gara, con qualsiasi razza.</p></div>
<h2>Di cosa si tratta</h2>
<p>L'obedience è una disciplina cinofila in cui conduttore e cane lavorano in sintonia: il cane segue il conduttore a passo, esegue posizioni, torna al richiamo, rimane fermo e riporta oggetti. Il giudice, in gara, valuta precisione e attitudine; ma anche chi non gareggia trova nell'obedience un modo bellissimo per costruire attenzione e collaborazione.</p>
<h2>Quali cani possono praticarla</h2>
<p>Tutti, di qualsiasi razza e taglia, purché siano in salute e abbiano voglia di collaborare. Non serve un cane "già educato": si parte da basi semplici e si cresce insieme.</p>
<h2>I benefici</h2>
<ul>
<li>Più attenzione e concentrazione sul conduttore.</li>
<li>Un richiamo e un'educazione di base più solidi.</li>
<li>Stimolazione mentale e fisica.</li>
<li>Un rapporto più forte e comunicativo.</li>
</ul>
<h2>Come iniziare</h2>
<ol>
<li><strong>Valuta le basi:</strong> seduto, terra, richiamo e passeggiata tranquilla sono un buon punto di partenza.</li>
<li><strong>Scegli un percorso rispettoso:</strong> l'obedience non richiede strumenti coercitivi; il gioco e il rinforzo sono più efficaci e piacevoli.</li>
<li><strong>Allenati poco ma spesso:</strong> sessioni brevi, divertenti, che finiscono quando il cane è ancora entusiasta.</li>
<li><strong>Sii paziente:</strong> la precisione si costruisce a piccoli passi, un criterio alla volta.</li>
</ol>
""",
"faq": [
("Devo gareggiare?", "No: puoi praticare obedience solo per piacere e per migliorare la relazione con il tuo cane."),
("Serve un cane giovane?", "No, si può iniziare a qualunque età, adattando esercizi e ritmi alle capacità del cane."),
],
},
{
"slug": "ricerca-tartufi-con-il-cane",
"title": "Ricerca tartufi con il cane: come funziona",
"desc": "Cos'è la ricerca tartufi sportiva, quali cani possono praticarla, come si addestra il fiuto e come iniziare con un percorso gentile.",
"h1": "Ricerca tartufi con il cane: come funziona e come iniziare",
"lead": "Il naso è il senso più importante del cane. La ricerca tartufi sportiva è un modo per metterlo al lavoro, in modo naturale e appagante, con qualsiasi razza.",
"cat": "Sport cinofili", "img": "ricerca-tartufi.webp", "alt": "Cane durante la ricerca del tartufo",
"svc": ("servizi/ricerca-tartufi.html", "Scopri la ricerca tartufi"),
"related": ["cos-e-l-obedience-come-iniziare", "brevetti-cae-1-e-bh-differenze", "educazione-senza-coercizione"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> nella ricerca tartufi sportiva il cane impara a individuare l'odore del tartufo e a segnalarlo. È un'attività olfattiva adatta a tutte le razze, anche agli esemplari non da caccia, e può essere praticata per piacere o in competizione.</p></div>
<h2>Di cosa si tratta</h2>
<p>Il cane viene guidato a cercare un odore specifico in un'area e a segnalare il ritrovamento, in genere indicando il punto e ricevendo un premio. In ambito sportivo l'attività si svolge in percorsi dedicati, con regole e valutazioni che tengono conto anche del benessere del cane.</p>
<h2>Quali cani possono farla</h2>
<p>Qualsiasi razza, anche i meticci: l'olfatto è una dote di tutti i cani, ed è una delle attività più democratiche. Va bene anche per cani anziani o con limiti fisici, perché richiede più concentrazione che sforzo.</p>
<h2>Perché fa bene</h2>
<ul>
<li><strong>Appaga il bisogno di annusare</strong>, che in città spesso resta insoddisfatto.</li>
<li><strong>Stanca la mente</strong> più di una corsa: un cane che usa il naso è un cane più sereno.</li>
<li><strong>Rafforza la collaborazione:</strong> il cane lavora in autonomia ma con te accanto.</li>
<li><strong>Costruisce fiducia</strong> nei cani insicuri, che si sentono competenti.</li>
</ul>
<h2>Come si inizia</h2>
<ol>
<li><strong>Scelta della motivazione:</strong> si parte da ciò che il cane ama di più, premio o gioco.</li>
<li><strong>Associazione dell'odore:</strong> il cane impara che quell'odore porta ricompense.</li>
<li><strong>Segnalazione:</strong> si insegna come indicare il ritrovamento.</li>
<li><strong>Aumento della difficoltà:</strong> nascondigli più complicati, superfici diverse, più tempo di ricerca.</li>
</ol>
<p>Come sempre, il lavoro si costruisce con gradualità e senza costrizione: il cane cerca perché gli piace.</p>
""",
"faq": [
("Serve un cane da tartufo?", "No: nella ricerca sportiva può partecipare qualsiasi cane, indipendentemente dalla razza o dal pedigree."),
("È un'attività impegnativa fisicamente?", "In genere è poco faticosa per il fisico e molto stimolante per la mente: adatta anche a cani anziani."),
],
},
{
"slug": "brevetti-cae-1-e-bh-differenze",
"title": "Brevetti CAE-1 e BH: differenze e come prepararsi",
"desc": "Brevetto CAE-1 e brevetto BH (Begleithund): cosa sono, in cosa si differenziano e come prepararsi alla prova con un percorso rispettoso.",
"h1": "Brevetti CAE-1 e BH: differenze e come prepararsi",
"lead": "Due brevetti, due obiettivi: il CAE-1 verifica l'affidabilità del cane nella vita quotidiana, il BH aggiunge esercizi di condotta e obbedienza. Come scegliere e come arrivare pronti.",
"cat": "Brevetti", "img": "cae.webp", "alt": "Prova per il brevetto CAE-1",
"svc": ("servizi/brevetto-cae.html", "Vedi il brevetto CAE-1"),
"related": ["cos-e-l-obedience-come-iniziare", "il-richiamo-non-funziona", "come-scegliere-educatore-cinofilo-piacenza"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> il CAE-1 valuta il comportamento del cane in situazioni di tutti i giorni; il BH (Begleithund, cane da compagnia) comprende anche una parte di esercizi di condotta e obbedienza e una prova in ambiente urbano. Requisiti e regolamenti dipendono dall'organizzatore: verificali sempre prima di iscriverti.</p></div>
<h2>Il brevetto CAE-1</h2>
<p>È un attestato di tipo educativo: osserva come il cane si comporta tra persone, davanti ad altri cani e a rumori e stimoli quotidiani, in un contesto realistico. È pensato per cani che vivono in famiglia e in città, e non richiede doti sportive particolari.</p>
<h2>Il brevetto BH</h2>
<p>Il BH (Begleithund, "cane da compagnia") ha in genere due parti: una serie di esercizi di condotta e obbedienza di base, e una prova in ambiente urbano. È più vicino al mondo sportivo e in molte discipline rappresenta un primo passo verso prove più impegnative.</p>
<h2>Le differenze, in sintesi</h2>
<ul>
<li><strong>Obiettivo:</strong> CAE-1 = affidabilità nella vita quotidiana; BH = affidabilità più precisione negli esercizi.</li>
<li><strong>Prova:</strong> il CAE-1 è centrato su situazioni reali; il BH comprende anche esercizi di campo.</li>
<li><strong>Per chi:</strong> il CAE-1 per qualsiasi cane di famiglia; il BH per chi ha già buone basi o vuole avvicinarsi allo sport.</li>
</ul>
<h2>Come prepararsi</h2>
<ol>
<li><strong>Parti dalle basi:</strong> passeggiata tranquilla, richiamo, seduto, terra e resta con distrazioni.</li>
<li><strong>Allenati in contesti reali:</strong> strade, parcheggi, incontri con persone e altri cani, rumori.</li>
<li><strong>Simula la prova</strong> con una persona che non conosce il cane.</li>
<li><strong>Cura il benessere:</strong> un cane stanco o stressato lavora peggio; programma pause e giochi.</li>
<li><strong>Informati sul regolamento:</strong> date, requisiti e documenti sono dell'ente organizzatore.</li>
</ol>
""",
"faq": [
("Posso fare entrambi i brevetti?", "Sì: molti binomi partono dal CAE-1 e poi proseguono con il BH. Un educatore ti aiuta a scegliere il percorso adatto."),
("Il mio cane deve essere perfetto?", "No: si valutano equilibrio e collaborazione, non la perfezione. Un cane sereno e ben guidato ha buone possibilità."),
],
},
{
"slug": "morso-sportivo-senza-coercizione-miti",
"title": "Morso sportivo senza coercizione: miti e verità",
"desc": "Il morso sportivo rende il cane aggressivo? Miti e verità sul lavoro di morso e su come praticarlo in modo rispettoso, con motivazione e autocontrollo.",
"h1": "Morso sportivo senza coercizione: miti e verità",
"lead": "Il lavoro di morso è spesso frainteso. Fatto bene è un gioco strutturato, con regole chiare e molto autocontrollo, non un addestramento all'aggressività.",
"cat": "Sport cinofili", "img": "morso-hero.webp", "alt": "Cane che morde la manica durante un esercizio di morso sportivo",
"svc": ("servizi/attivita-morso.html", "Vedi le attività di morso"),
"related": ["collari-a-strangolo-ed-elettrici", "educazione-senza-coercizione", "brevetti-cae-1-e-bh-differenze"],
"mins": 5,
"body": """
<div class="callout"><p><strong>In breve:</strong> nel morso sportivo il cane mette a frutto istinti naturali (preda, gioco) in un contesto regolamentato, e impara soprattutto a lasciare e a calmarsi su comando. Si può costruire senza collari elettrici, strangolo o intimidazione.</p></div>
<h2>Mito 1: "Il morso rende il cane aggressivo"</h2>
<p>Falso, se il lavoro è fatto correttamente. Il morso sportivo è un gioco con regole: si morde un oggetto (manica o salsicciotto), su comando, e si lascia su comando. Il cane impara a gestire livelli di eccitazione alti senza perdere ascolto.</p>
<h2>Mito 2: "Serve la costrizione per ottenere controllo"</h2>
<p>Il controllo più affidabile nasce dalla motivazione e dall'abitudine: il "lascia" si costruisce con scambi e rinforzi, finché diventa un riflesso anche in piena attivazione. Con la costrizione si ottiene spesso un cane stressato e meno prevedibile.</p>
<h2>Mito 3: "Va bene per tutti i cani"</h2>
<p>Non è vero: serve un cane con temperamento idoneo, equilibrato e con una buona relazione con il conduttore. Per questo ogni binomio parte da una valutazione individuale, e non tutti i cani vengono ammessi al lavoro.</p>
<h2>Cosa significa lavorare senza coercizione</h2>
<ul>
<li><strong>Motivazione:</strong> il cane lavora perché gli piace, per il gioco e la preda.</li>
<li><strong>Autocontrollo:</strong> prima della manica si lavora su attivazione e calma.</li>
<li><strong>Sessioni brevi e graduali:</strong> si rispettano tempi e segnali del cane.</li>
<li><strong>Nessuno strumento che fa male:</strong> niente collari elettrici, a strangolo o a punte.</li>
</ul>
<h2>E la sicurezza?</h2>
<p>Il lavoro avviene in un ambiente controllato, con persone esperte (figuranti) e regole chiare. Non è un'attività da improvvisare o fare in autonomia: serve un percorso guidato.</p>
""",
"faq": [
("Posso iniziare con un cane adulto?", "Dipende dal cane: ogni caso va valutato. L'età non è l'unico fattore, contano temperamento, salute e relazione."),
("Si può fare lavoro di morso senza gareggiare?", "Sì: molti binomi lo praticano per passione e per benessere del cane, senza obiettivi di gara."),
],
},
{
"slug": "come-scegliere-educatore-cinofilo-piacenza",
"title": "Come scegliere un educatore cinofilo a Piacenza",
"desc": "Come scegliere un educatore cinofilo a Piacenza: qualifiche, metodo, domande da fare e segnali d'allarme per affidare bene il tuo cane.",
"h1": "Come scegliere un educatore cinofilo a Piacenza",
"lead": "Il mondo dell'educazione cinofila è vario: scegliere bene vuol dire proteggere il benessere del tuo cane. Ecco su cosa basarsi e quali domande fare.",
"cat": "Consigli", "img": "classi-socializzazione.webp", "alt": "Cani durante una classe di socializzazione al campo",
"svc": ("contatti.html", "Richiedi l'incontro conoscitivo"),
"related": ["educazione-senza-coercizione", "collari-a-strangolo-ed-elettrici", "quando-iniziare-puppy-training"],
"mins": 4,
"body": """
<div class="callout"><p><strong>In breve:</strong> cerca un professionista con formazione riconosciuta, che usi metodi senza dolore né paura, ti spieghi cosa fa e perché, e ti proponga un percorso su misura dopo aver conosciuto il cane.</p></div>
<h2>1. Controlla formazione e qualifiche</h2>
<p>In Italia il settore non è regolato da un unico albo: contano i percorsi formativi e i riconoscimenti di enti e federazioni cinofile. Chiedi quali titoli ha, da quanto tempo lavora e come si aggiorna. Un professionista serio ne parla volentieri.</p>
<h2>2. Chiedi quali strumenti e metodi usa</h2>
<p>Domande utili:</p>
<ul>
<li>Usa collari a strangolo, a punte o elettrici?</li>
<li>Come reagisce quando il cane sbaglia?</li>
<li>Cosa fa se il mio cane ha paura o è molto agitato?</li>
</ul>
<p>Le risposte dicono molto: un buon educatore lavora con rinforzi, gestione dell'ambiente e gradualità.</p>
<h2>3. Fai un primo incontro</h2>
<p>Un incontro conoscitivo serve a osservare il cane, ascoltare le tue esigenze e capire se c'è sintonia. Diffida di chi promette risultati garantiti o rapidissimi senza aver visto il cane.</p>
<h2>4. Valuta come lavora con te</h2>
<p>Il lavoro vero è sul binomio: una buona lezione ti spiega cosa fare a casa, ti lascia esercizi pratici e ti rende autonomo.</p>
<h2>Segnali d'allarme</h2>
<ul>
<li>Strumenti o tecniche che causano dolore o spavento.</li>
<li>Spiegazioni basate su "dominanza" o sul dover mostrare al cane chi comanda.</li>
<li>Rifiuto di rispondere a domande o di farti assistere a una lezione.</li>
<li>Promesse di risultati identici per ogni cane.</li>
</ul>
<h2>Vicino a casa: perché conta</h2>
<p>Se vivi a Piacenza o provincia, un campo raggiungibile rende più facile la costanza, che è ciò che fa funzionare davvero un percorso. Il nostro è a Podenzano, a circa 15 minuti da Piacenza.</p>
""",
"faq": [
("Quanto costa una lezione con un educatore?", "I prezzi variano; da noi trovi il listino con lezioni singole e pacchetti nella pagina prezzi."),
("Educatore, istruttore, addestratore: sono la stessa cosa?", "I termini si sovrappongono. Più della parola conta il metodo: chiedi sempre come lavora e quali strumenti usa."),
],
},
]
