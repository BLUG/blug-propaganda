
###############################################################
                         BLUG HOWTO
###############################################################


Videoopptak
###############################################################

Vi har siden 2009 tatt opp de fleste foredragene som er holdt 
for BLUG. Med en del forskjellig utstyr. Vi har også eksperimentert
en god del med forskjellige løsninger for live-streaming.

Tidligere løsninger
-------------------

Vi har bl.a. brukt et Contour roam 2 actionkamera til opptak.
Det gir bra bilde, også når det er relativt mørkt i rommet,
men det har ingen mulighet for live-streaming. Det har en
vidvinkel linse, slik at en slipper å flytte kameraet om 
foredragsholderen beveger seg mye rundt.

Vi har også prøvd å strømme direkte fra et Samsung Galaxy kamera via
google hangouts. Det fungerte tålelig bra, men hangouts som platform
ga oss lite kontroll på resultatet.

Dagens løsning
-------------------

I dag bruker vi et Panasonic ### videokamera, en Magewell USB Capture
HDMI enhet, og en laptop med OBS (Open Broadcasting Software). Opptak
fra foredragsholders maskin gjøres med FFMPEG, og strømmes til
OBS-laptopen via UDP.

Ønskeliste
-------------------

* Sender/mottager for trådløs mikrofon

OBS Konfigurasjon
-------------------

